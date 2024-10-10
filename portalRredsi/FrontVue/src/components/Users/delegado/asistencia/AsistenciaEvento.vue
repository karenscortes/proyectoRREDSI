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

            <!-- Filtros y Buscador -->
            <div class="row mb-2 justify-content-between align-items-center">
                <!-- Filtros -->
                <div class="col-auto">
                    <a href="#" @click.prevent="fetchFiltrar('Todos')"
                        :class="['mx-1 px-2 border', filtroActivo === 'Todos' ? 'bg-secondary text-white' : 'text-dark']"
                        style="border-radius: 20px;">
                        Todos
                    </a>
                    <a href="#" @click.prevent="fetchFiltrar('Ponentes')"
                        :class="['mx-1 px-2 border', filtroActivo === 'Ponentes' ? 'bg-secondary text-white' : 'text-dark']"
                        style="border-radius: 20px;">
                        Ponentes
                    </a>
                    <a href="#" @click.prevent="fetchFiltrar('Evaluadores')"
                        :class="['mx-1 px-2 border', filtroActivo === 'Evaluadores' ? 'bg-secondary text-white' : 'text-dark']"
                        style="border-radius: 20px;">
                        Evaluadores
                    </a>
                </div>

                <!-- Buscador -->
                <div class="col-8 col-sm-8">
                    <div class="row justify-content-end">
                        <div class="col-8 col-sm-6">
                            <input v-model="busqueda" type="text" id="busqueda"
                                class="form-control text-dark w-100" style="height: 100%; padding: 0.5rem;"
                                placeholder="Ingresa número de documento"
                                @keyup.enter="buscarPorDocumento" >
                        </div>
                        <div class="col-4 col-sm-4">
                            <button class="btn w-100 font-weight-bold"
                                style="background: rgb(255, 182, 6); color: #000000" @click="buscarPorDocumento">
                                Buscar
                            </button>
                        </div>
                    </div>
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

            <PaginatorBody v-if="!buscando && totalPages > 1" :totalPages="totalPages" @page-changed="selectedPage" />
        </div>
    </div>
</template>


<script>
import { ref, onMounted } from 'vue';
import { asistenciaEvento, actualizarAsistencia, obtenerAsistentesPorRol, obtenerAsistentePorDocumento, obtenerSalas, obtenerConvocatoria } from '@/services/delegadoService';
import PaginatorBody from '../../../UI/PaginatorBody.vue';
import { useToastUtils } from '@/utils/toast';

export default {
    components: {
        PaginatorBody,
    },
    setup() {
        const asistentes = ref([]);
        const busqueda = ref(''); 
        const currentPage = ref(1);
        const totalPages = ref(0);
        const filtroActivo = ref('Todos');
        const buscando = ref(false); 

        const { showSuccessToast, showErrorToast, showInfoToast, showWarningToast } = useToastUtils();

        const fetchAsistentes = async () => {
            try {
                const response = await asistenciaEvento(currentPage.value);
                asistentes.value = response.data.asistentes;
                totalPages.value = response.data.total_pages;
                filtroActivo.value = 'Todos';
                buscando.value = false;
            } catch (error) {
                console.log("Error al obtener los asistentes.");
            }
        };

        const fetchFiltrar = async (filtro) => {
            filtroActivo.value = filtro;
            currentPage.value = 1;

            try {
                if (filtro === 'Ponentes') {
                    await filtrarPonentes();
                } else if (filtro === 'Evaluadores') {
                    await filtrarEvaluadores();
                } else {
                    await fetchAsistentes();
                }
            } catch (error) {
                console.log("Error al filtrar asistentes.");
            }
        };

        const filtrarPonentes = async () => {
            try {
                const response = await obtenerAsistentesPorRol('Ponente', currentPage.value);
                asistentes.value = response.data.asistentes;
                totalPages.value = response.data.total_pages;
                buscando.value = false;
            } catch (error) {
                console.log("Error al filtrar ponentes.");
            }
        };

        const filtrarEvaluadores = async () => {
            try {
                const response = await obtenerAsistentesPorRol('Evaluador', currentPage.value);
                asistentes.value = response.data.asistentes;
                totalPages.value = response.data.total_pages;
                buscando.value = false;
            } catch (error) {
                console.log("Error al filtrar evaluadores.");
            }
        };

        const buscarPorDocumento = async () => {
            try {
                if (busqueda.value.trim() === "") {
                    showInfoToast("Debes ingresar un número de documento.");
                } else {
                    const response = await obtenerAsistentePorDocumento(busqueda.value);
                    asistentes.value = [response.data]; 
                    buscando.value = true; 
                    totalPages.value = 0; 
                }
            } catch (error) {
                showWarningToast("El documento ingresado no existe, verifica nuevamente.");
                fetchAsistentes(); 
            } finally {
                busqueda.value = ""; 
            }
        };

        const toggleActualizarAsistencia = async (asistente) => {
            try {
                asistente.asistencia = asistente.asistencia ? 0 : 1;
                await actualizarAsistencia(asistente.id_asistente, asistente.id_usuario, asistente.asistencia);
                showSuccessToast("Asistencia actualizada exitosamente.");
            } catch (error) {
                showErrorToast("Error al actualizar la asistencia.");
            }
        };

        const selectedPage = async (pagina) => {
            currentPage.value = pagina;
            if (filtroActivo.value === 'Ponentes') {
                await filtrarPonentes();
            } else if (filtroActivo.value === 'Evaluadores') {
                await filtrarEvaluadores();
            } else {
                await fetchAsistentes();
            }
        };

        onMounted(() => {
            fetchAsistentes();
        });

        return {
            asistentes,
            busqueda,
            currentPage,
            totalPages,
            filtroActivo,
            fetchFiltrar,
            buscarPorDocumento,
            toggleActualizarAsistencia,
            selectedPage,
            buscando
        };
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
