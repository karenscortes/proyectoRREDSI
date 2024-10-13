<template>
    <!-- Mostrar el componente seleccionado si 'showCalificarProyecto' es verdadero -->
    <component v-if="state.showCalificarProyecto && state.selectedComponent" :is="state.selectedComponent" :proyecto="state.selectedProyecto"
        @volver="handleVolver" />

    <!-- Mostrar la lista de proyectos si 'showCalificarProyecto' es falso -->
    <div v-else>
        <!-- Sección de botones y proyectos -->
        <div class="row mb-5 mt-2">
            <div class="col">
                <div class="section_title text-center">
                    <h1>Listado de proyectos</h1>
                    <h2 class="text-muted">{{ tituloEtapa }}</h2>
                </div>
            </div>
        </div>

        <!-- Contenedor para los proyectos -->
        <div class="row justify-content-center mt-2">
            <div class="col-xl-10 col-lg-8 col-md-8">
                <div class="row text-center">
                    <!-- Botones de navegación -->
                    <div class="col-2 d-flex justify-content-center align-items-center">
                        <button class="btn cards__buttons w-100" @click="prevPage" :disabled="state.currentPage === 1">
                            <i class="fa-solid fa-circle-arrow-left fa-2xl"></i>
                        </button>
                    </div>

                    <div class="col-8">
                        <div class="d-flex justify-content-around">
                            <button class="btn cards__buttons border" :class="{ 'active-button': state.selectedState === '' }"
                                @click="fetchProyectos(1)" :disabled="state.selectedState === ''">
                                Todos
                            </button>
                            <button class="btn cards__buttons border"
                                :class="{ 'active-button': state.selectedState === 'Calificado' }"
                                @click="fetchProyectosPorEstado('Calificado')"
                                :disabled="state.selectedState === 'Calificado'">
                                Calificados
                            </button>
                            <button class="btn cards__buttons border"
                                :class="{ 'active-button': state.selectedState === 'Pendiente' }"
                                @click="fetchProyectosPorEstado('Pendiente')" :disabled="state.selectedState === 'Pendiente'">
                                Pendientes
                            </button>
                        </div>
                    </div>

                    <!-- Botón de navegación derecha -->
                    <div class="col-2 d-flex justify-content-center align-items-center">
                        <button class="btn cards__buttons w-100" @click="nextPage"
                            :disabled="state.currentPage === state.totalPages">
                            <i class="fa-solid fa-circle-arrow-right fa-2xl"></i>
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <!-- Creación de cards con el proyecto -->
        <p v-if="hasProyectos" class="text-center mt-2 fs-5">
            Página {{ state.currentPage }} de {{ state.totalPages }}
        </p>

        <div v-if="!hasProyectos" class="row justify-content-center mt-5">
            <p class="text-muted text-center fs-4">{{ mensajeSinProyectos }}</p>
        </div>

        <div v-else class="row justify-content-center mt-3">
            <CardListaProyectos v-for="(proyecto, index) in state.proyectos" :key="index" :proyecto="proyecto"
                :currentEtapa="state.currentEtapa" :id_etapa_actual="state.id_etapa_actual" :index="(state.currentPage - 1) * state.itemsPerPage + index + 1"  @component-selected="changeComponent" />
        </div>
    </div>
</template>

<script>
import { reactive, computed } from 'vue';
import { obtenerEtapaActual } from '../../../../services/evaluadorService';
import { obtenerListaProyectos, obtenerProyectosPorEstado } from '../../../../services/delegadoService';
import CalificarProyectoEvaluadorView from '../../../../views/CalificarProyectoEvaluadorView.vue';
import { useAuthStore } from '@/store';
import { useToastUtils } from '@/utils/toast';
import CardListaProyectos from './CardListaProyectos.vue';
import DetalleProyecto from './componentsDetalleProyecto/DetalleProyecto.vue';

export default {
    components: {
        CardListaProyectos,
        CalificarProyectoEvaluadorView,
        DetalleProyecto
    },
    setup() {
        const { showSuccessToast, showErrorToast, showInfoToast } = useToastUtils();

        const state = reactive({
            proyectos: [],
            currentPage: 1,
            totalPages: 1,
            itemsPerPage: 6,
            selectedState: '',
            selectedComponent: '',
            selectedProyecto: null,
            id_etapa_actual: '',
            showCalificarProyecto: false,
            currentEtapa: ''
        });

        const hasProyectos = computed(() => {
            return state.proyectos.length > 0;
        });

        const mensajeSinProyectos = computed(() => {
            if (!state.selectedState) {
                return "No tienes proyectos asignados por el momento...";
            } else if (state.selectedState === 'Calificado') {
                return "No tienes proyectos calificados...";
            } else if (state.selectedState === 'Pendiente') {
                return "No tienes proyectos pendientes...";
            }
            return "No hay proyectos disponibles.";
        });

        const tituloEtapa = computed(() => {
            return state.currentEtapa === 'Virtual' ? 'Primera Etapa' : 'Segunda Etapa';
        });

        const obtenerEtapa = async () => {
            try {
                const authStore = useAuthStore();
                const user = authStore.user;
                const response = await obtenerEtapaActual(user.id_usuario);
                state.currentEtapa = response.nombre_etapa;
                state.id_etapa_actual = response.id_etapa;
                fetchProyectos();
            } catch (error) {
                showErrorToast("Error al obtener la etapa actual. ");
            }
        };

        const fetchProyectos = async (page = 1) => {
            try {
                state.selectedState = '';

                const response = await obtenerListaProyectos(state.currentEtapa, page, state.itemsPerPage);
                state.proyectos = response.data;
                state.totalPages = response.total_pages;
                state.currentPage = page;

            } catch (error) {
                showErrorToast("Error al obtener proyectos.");
            }
        };

        const fetchProyectosPorEstado = async (estado) => {
            try {
                let pageToFetch = state.currentPage;

                if (state.selectedState !== estado) {
                    pageToFetch = 1;
                }

                state.selectedState = estado;

                const estadoMap = {
                    'Calificado': state.currentEtapa === 'Virtual' ? 'C_virtual' : 'C_presencial',
                    'Pendiente': state.currentEtapa === 'Virtual' ? 'P_virtual' : 'P_presencial'
                };

                const estadoEnvio = estadoMap[estado];

                if (!estadoEnvio) {
                    console.warn("Estado no válido seleccionado:", estado);
                    return;
                }

                const response = await obtenerProyectosPorEstado(state.currentEtapa, estadoEnvio, pageToFetch, state.itemsPerPage);
                state.proyectos = response.data.data;
                state.totalPages = response.data.total_pages;
                state.currentPage = pageToFetch;
            } catch (error) {
                console.error("Error al obtener proyectos por estado: ", error);
            }
        };

        const nextPage = () => {
            if (state.currentPage < state.totalPages) {
                const nextPage = state.currentPage + 1;
                if (state.selectedState) {
                    state.currentPage++;
                    fetchProyectosPorEstado(state.selectedState);
                } else {
                    fetchProyectos(nextPage);
                }
            }
        };

        const prevPage = () => {
            if (state.currentPage > 1) {
                const prevPage = state.currentPage - 1;
                if (state.selectedState) {
                    state.currentPage--;
                    fetchProyectosPorEstado(state.selectedState);
                } else {
                    fetchProyectos(prevPage);
                }
            }
        };

        const changeComponent = ({ componentName, proyecto }) => {
            state.selectedComponent = componentName;
            state.selectedProyecto = proyecto;
            state.showCalificarProyecto = true;
        };

        const handleVolver = () => {
            state.showCalificarProyecto = false;
        };

        return {
            state,
            hasProyectos,
            mensajeSinProyectos,
            tituloEtapa,
            obtenerEtapa,
            fetchProyectos,
            fetchProyectosPorEstado,
            nextPage,
            prevPage,
            changeComponent,
            handleVolver
        };
    },
    mounted() {
        this.obtenerEtapa();
    }
};
</script>




<style scoped>
.cards__buttons {
    background-color: #fff;
    width: 30%;
    transition: background-color 0.3s ease, transform 0.2s ease;
}

.cards__buttons:hover {
    background-color: #ffb521;
    transform: scale(1.02);
    cursor: pointer;
}

.cards__buttons:disabled {
    background-color: #f9f9f9;
    border: none;
    cursor: default;
}

.active-button {
    background-color: #e0e0e0;
    border-color: #c0c0c0;
}

.text-muted {
    font-size: 1.2rem;
    color: #999;
}

/* Media query para pantallas pequeñas */
@media (max-width: 576px) {
    .cards__buttons {
        font-size: 0.8rem;
        padding: 0.5rem;
    }

    .d-flex.justify-content-around {
        flex-wrap: wrap;
    }

    .d-flex.justify-content-center {
        margin-bottom: 0.5rem;
    }
}


/* Media query para pantallas entre 998px y 766px */
@media (min-width: 766px) and (max-width: 998px) {
    .cards__buttons {
        font-size: 0.9rem;
        padding: 0.5rem;
    }
}
</style>
