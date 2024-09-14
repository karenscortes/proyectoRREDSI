<template>
    <div>
        <div class="container pt-5">
            <div class="row mb-5 mt-2">
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
                                placeholder="Buscar...">
                        </div>
                        <div class="col-4">
                            <button class="btn w-100 font-weight-bold" @click="buscarPorDocumento">Buscar</button>
                        </div>
                    </div>
                </div>

                <!-- Select de salas disponibles -->
                <div class="col-4 col-sm-2">
                    <select class="form-select text-dark" v-model="salaSeleccionada" @change="filtrarPorSala">
                        <option value="Sala" selected>Sala</option>
                        <option v-for="opcion in opciones" :value="opcion.numero" :key="opcion.id">
                            {{ opcion.numero }}
                        </option>
                    </select>
                </div>
            </div>

            <!-- Filtros -->
            <div class="row ml-1 mb-2 justify-content-start mt-3">
                <div class="col-auto">
                    <a href="#" @click.prevent="fetchAsistentes"
                        :class="['mx-1 px-2 border', filtroActivo === 'Todos' ? 'bg-secondary text-white' : 'text-dark']"
                        style="border-radius: 20px;">
                        Todos
                    </a>
                </div>
                <div class="col-auto">
                    <a href="#" @click.prevent="filtrarPonentes"
                        :class="['mx-1 px-2 border', filtroActivo === 'Ponentes' ? 'bg-secondary text-white' : 'text-dark']"
                        style="border-radius: 20px;">
                        Ponentes
                    </a>
                </div>
                <div class="col-auto">
                    <a href="#" @click.prevent="filtrarEvaluadores"
                        :class="['mx-1 px-2 border', filtroActivo === 'Evaluadores' ? 'bg-secondary text-white' : 'text-dark']"
                        style="border-radius: 20px;">
                        Evaluadores
                    </a>
                </div>
            </div>

            <!-- Tabla -->
            <div class="table-responsive">
                <table id="basic-datatables" class="display table table-striped table-hover text-dark">
                    <thead>
                        <tr>
                            <th>N° de documento</th>
                            <th>Nombres</th>
                            <th>Institución</th>
                            <th>CHECK</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(asistente, index) in asistentes" :key="index">
                            <td>{{ asistente.documento }}</td>
                            <td>{{ asistente.nombres }} {{ asistente.apellidos }}</td>
                            <td>{{ asistente.institucion }}</td>
                            <td colspan="1">
                                <input type="checkbox" class="form-check-input ml-4" :checked="asistente.asistencia"
                                    @change="toggleActualizarAsistencia(asistente)">
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- Paginador -->
            <div class="mt-5">
                <div aria-label="Page navigation example mb-5">
                    <ul class="pagination justify-content-center">
                        <li class="page-item" :class="{ disabled: currentPage === 1 }">
                            <a class="page-link" href="#" @click.prevent="prevPage"
                                style="border-radius: 20px; color: black;">Previous</a>
                        </li>
                        <li class="page-item" v-for="n in totalPages" :key="n" :class="{ active: currentPage === n }">
                            <a class="page-link rounded-circle" href="#"
                                @click.prevent="currentPage = n; fetchAsistentes()">{{ n }}</a>
                        </li>
                        <li class="page-item" :class="{ disabled: currentPage === totalPages }">
                            <a class="page-link" href="#" @click.prevent="nextPage"
                                style="border-radius: 20px; color: black;">Next</a>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { asistenciaEvento, actualizarAsistencia, obtenerAsistentesPorSala, obtenerAsistentesPorRol, obtenerAsistentePorDocumento, obtenerSalas } from '@/services/delegadoService';

export default {
    data() {
        return {
            asistentes: [], // Lista de asistentes
            busqueda: '',
            salaSeleccionada: 'Sala',
            opciones: [], // Lista de salas
            currentPage: 1,
            totalPages: 0,
            filtroActivo: 'Todos' // filtro
        };
    },
    methods: {
        async fetchAsistentes() {
            try {
                const response = await asistenciaEvento(this.currentPage);
                this.asistentes = response.data.asistentes;
                this.totalPages = response.data.totalPages;
                this.filtroActivo = 'Todos'; // Restablecer a 'Todos'
            } catch (error) {
                alert("Error al obtener asistentes: " + error);
            }
        },

        async fetchAsistentesSalas() {
            try {
                const response = await obtenerSalas(this.currentPage, 10); // Asegúrate de pasar page y page_size si es necesario
                this.opciones = response.data.salas;
            } catch (error) {
                alert("Error al obtener las salas: " + error);
            }
        },

        async filtrarPonentes() {
            try {
                const response = await obtenerAsistentesPorRol('Ponente', this.currentPage);
                this.asistentes = response.data.asistentes;
                this.filtroActivo = 'Ponentes'; // Cambiar filtro a 'Ponentes'
            } catch (error) {
                alert("Error al filtrar ponentes: " + error);
            }
        },

        async filtrarEvaluadores() {
            try {
                const response = await obtenerAsistentesPorRol('Evaluador', this.currentPage);
                this.asistentes = response.data.asistentes;
                this.filtroActivo = 'Evaluadores'; // Cambiar filtro a 'Evaluadores'
            } catch (error) {
                alert("Error al filtrar evaluadores: " + error);
            }
        },

        async filtrarPorSala() {
            try {
                if (this.salaSeleccionada !== 'Sala') {
                    const response = await obtenerAsistentesPorSala(this.salaSeleccionada.numero, this.currentPage);
                    this.asistentes = response.data.asistentes;
                } else {
                    this.fetchAsistentes(); // Restablecer si se selecciona "Sala"
                }
            } catch (error) {
                alert("Error al filtrar por sala: " + error);
            }
        },

        async buscarPorDocumento() {
            try {
                const response = await obtenerAsistentePorDocumento(this.busqueda);
                this.asistentes = [response.data];
            } catch (error) {
                alert("Error al buscar asistente: " + error);
            }
        },

        async toggleActualizarAsistencia(asistente) {
            try {
                asistente.asistencia = asistente.asistencia ? 0 : 1;
                await actualizarAsistencia(asistente.id_asistente, asistente.id_usuario, asistente.asistencia);
            } catch (error) {
                alert("Error al actualizar la asistencia: " + error.message);
            }
        },

        nextPage() {
            if (this.currentPage < this.totalPages) {
                this.currentPage++;
                this.fetchAsistentes();
            }
        },

        prevPage() {
            if (this.currentPage > 1) {
                this.currentPage--;
                this.fetchAsistentes();
            }
        }
    },
    mounted() {
        this.fetchAsistentes();
        this.fetchAsistentesSalas();
        this.filtrarPorSala();
    }
};
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
