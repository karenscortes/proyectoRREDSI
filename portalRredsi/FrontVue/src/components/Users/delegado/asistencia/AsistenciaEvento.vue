<template>
    <div>
        <div class="container pt-3">
            <div class="row mb-3 mt-2">
                <div class="col">
                    <div class="section_title text-center">
                        <h1>Asistencia</h1>
                    </div>
                </div>
            </div>

            <!-- Buscador -->
            <div class="row mb-5 justify-content-between">
                <div class="col-8 col-sm-6">
                    <div class="row">
                        <div class="col-8">
                            <input type="text" v-model="busqueda" id="busqueda" class="form-control"
                                placeholder="Ingresa número de documento">
                        </div>
                        <div class="col-4">
                            <button class="btn w-100 font-weight-bold" @click="buscarPorDocumento">Buscar</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Filtros -->
            <div class="row ml-1 mb-2 justify-content-start mt-3">
                <div class="col-auto">
                    <a href="#" @click.prevent="fetchFiltrar('Todos')"
                        :class="['mx-1 px-2 border', filtroActivo === 'Todos' ? 'bg-secondary text-white' : 'text-dark']"
                        style="border-radius: 20px;">
                        Todos
                    </a>
                </div>
                <div class="col-auto">
                    <a href="#" @click.prevent="fetchFiltrar('Ponentes')"
                        :class="['mx-1 px-2 border', filtroActivo === 'Ponentes' ? 'bg-secondary text-white' : 'text-dark']"
                        style="border-radius: 20px;">
                        Ponentes
                    </a>
                </div>
                <div class="col-auto">
                    <a href="#" @click.prevent="fetchFiltrar('Evaluadores')"
                        :class="['mx-1 px-2 border', filtroActivo === 'Evaluadores' ? 'bg-secondary text-white' : 'text-dark']"
                        style="border-radius: 20px;">
                        Evaluadores
                    </a>
                </div>
                <div v-if="asistentes.length > 0" class="col-auto ml-auto d-flex align-items-center">
                    <span class="text-dark fs-8">Fecha: </span>
                    <span class="text-muted ml-3">{{asistentes[0].fecha }}</span>
                </div>
            </div>

            <!-- Tabla -->
            <div class="table-responsive">
                <table id="basic-datatables" class="display table table-striped table-hover text-dark">
                    <thead>
                        <tr>
                            <th>N° de documento</th>
                            <th>Nombres</th>
                            <th>Apellidos</th>
                            <th>CHECK</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(asistente, index) in asistentes" :key="index">
                            <td>{{ asistente.documento }}</td>
                            <td>{{ asistente.nombres }}</td>
                            <td>{{ asistente.apellidos }}</td>
                            <td colspan="1">
                                <input type="checkbox" class="form-check-input ml-4" :checked="asistente.asistencia"
                                    @change="toggleActualizarAsistencia(asistente)">
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Paginador -->
            <PaginatorBody 
                :totalPages="totalPages" @page-changed="selectedPage" v-if="totalPages > 1" 
            />
        </div>
    </div>
</template>

<script>
import { asistenciaEvento, actualizarAsistencia, obtenerAsistentesPorSala, obtenerAsistentesPorRol, obtenerAsistentePorDocumento, obtenerSalas, obtenerConvocatoria } from '@/services/delegadoService';
import PaginatorBody from '../../../UI/PaginatorBody.vue';

export default {
    components: {
        PaginatorBody, 
    },
    data() {
        return {
            asistentes: [], 
            busqueda: '',
            salaSeleccionada: '',
            opciones: [], 
            currentPage: 1,
            totalPages: 0,
            filtroActivo: 'Todos', 
        };
    },
    methods: {
        async fetchAsistentes() {
            try {
                const response = await asistenciaEvento(this.currentPage, this.fechaInicio, this.fechaFin);
                this.asistentes = response.data.asistentes;
                this.totalPages = response.data.total_pages;
                this.filtroActivo = 'Todos';
                this.busqueda = '';
                this.salaSeleccionada = '';
            } catch (error) {
                alert("Error al obtener asistentes: " + error);
            }
        },

        async fetchAsistentesSalas() {
            try {
                const response = await obtenerSalas(this.currentPage);
                this.opciones = response.data.salas;
            } catch (error) {
                alert("Error al obtener las salas: " + error);
            }
        },

        async fetchFiltrar(filtro) {
            this.filtroActivo = filtro;
            this.currentPage = 1; 

            if (filtro === 'Ponentes') {
                await this.filtrarPonentes();
            } else if (filtro === 'Evaluadores') {
                await this.filtrarEvaluadores();
            } else {
                await this.fetchAsistentes();
            }
        },

        async filtrarPonentes() {
            try {
                const response = await obtenerAsistentesPorRol('Ponente', this.currentPage);
                this.asistentes = response.data.asistentes;
                this.totalPages = response.data.total_pages;
            } catch (error) {
                alert("Error al filtrar ponentes: " + error);
            }
        },

        async filtrarEvaluadores() {
            try {
                const response = await obtenerAsistentesPorRol('Evaluador', this.currentPage);
                this.asistentes = response.data.asistentes;
                this.totalPages = response.data.total_pages;
            } catch (error) {
                alert("Error al filtrar evaluadores: " + error);
            }
        },

        async buscarPorDocumento() {
            try {
                if (this.busqueda.trim() == "") {
                    alert("Debes ingresar un valor");
                } else {
                    const response = await obtenerAsistentePorDocumento(this.busqueda);
                    this.asistentes = [response.data];
                }
            } catch (error) {
                this.fetchAsistentes();
            }
        },

        async toggleActualizarAsistencia(asistente) {
            try {
                asistente.asistencia = asistente.asistencia ? 0 : 1;
                await actualizarAsistencia(asistente.id_asistente, asistente.id_usuario, asistente.asistencia);
                alert('Actualizado exitosamente');
            } catch (error) {
                alert("Error al actualizar la asistencia: " + error.message);
            }
        },

        async selectedPage(pagina) {
            this.currentPage = pagina;
            if (this.filtroActivo === 'Ponentes') {
                await this.filtrarPonentes();
            } else if (this.filtroActivo === 'Evaluadores') {
                await this.filtrarEvaluadores();
            } else {
                await this.fetchAsistentes();
            }
        },

        async fetchConvocatoriaActual() {
            try {
                const response = await obtenerConvocatoria();
                const convocatoria = response.convocatoria;
                if (!convocatoria) {
                    throw new Error("No se encontró la convocatoria.");
                }
                this.fechaInicio = convocatoria.fecha_inicio;
                this.fechaFin = convocatoria.fecha_fin;
                this.fetchAsistentes();
            } catch (error) {
                alert("Error al obtener la convocatoria actual: " + error.message);
            }
        },
    },
    mounted() {
        const obtenerDatos = async () => {
            await this.fetchConvocatoriaActual();
            await this.fetchAsistentesSalas();
        };
        obtenerDatos();
    }
}
</script>




<style scoped>
.section_title h1 {
    display: block;
    color: #1a1a1a;
    font-weight: 500;
    padding-top: 24px;
}

.section_title h1::before {
    display: block;
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 55px;
    height: 4px;
    content: '';
    background: #ffb606;
}

.page-link {
    color: black;
}

#basic-datatables {
    text-align: start;
}

th,
button {
    background: rgb(255, 182, 6) !important;
}

.mx-1.px-2.border {
    cursor: pointer;
}

.mx-1.px-2.border.text-dark:hover {
    background-color: rgba(0, 0, 0, 0.1);
}
</style>
