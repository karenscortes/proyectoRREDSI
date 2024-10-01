<template>

    <!-- Mostrar el componente seleccionado si 'showCalificarProyecto' es verdadero -->
    <component 
        v-if="showCalificarProyecto && selectedComponent" 
        :is="selectedComponent" 
        :proyectoSeleccionado="selectedProyecto" 
        @volver="handleVolver" 
    />
    
    <!-- Mostrar la lista de proyectos si 'showCalificarProyecto' es falso -->
    <div v-else>
        <!-- Sección de botones y proyectos -->
        <div class="row mb-5 mt-2">
            <div class="col">
                <div class="section_title text-center">
                    <h1>Proyectos Asignados</h1>
                    <h2 class="text-muted">{{ tituloEtapa }}</h2> 
                </div>
            </div>
        </div>

        <!-- Contenedor para los proyectos -->
        <div class="row justify-content-center mt-3">
            <div class="col-xl-10 col-lg-8 col-md-8">
                <div class="row text-center">
                    <!-- Botones de navegación -->
                    <div class="col-2 d-flex justify-content-center align-items-center">
                        <button 
                            class="btn cards__buttons w-100"
                            @click="prevPage"
                            :disabled="currentPage === 1"
                        >
                            <i class="fa-solid fa-circle-arrow-left fa-2xl"></i>
                        </button>
                    </div>

                    <div class="col-8">
                        <div class="d-flex justify-content-around">
                            <button
                                class="btn cards__buttons border"
                                :class="{ 'active-button': selectedState === '' }"
                                @click="fetchProyectos(1)"
                                :disabled="selectedState === ''"
                            >
                                Todos
                            </button>
                            <button
                                class="btn cards__buttons border"
                                :class="{ 'active-button': selectedState === 'Calificado' }"
                                @click="fetchProyectosPorEstado('Calificado')"
                                :disabled="selectedState === 'Calificado'"
                            >
                                Calificados
                            </button>
                            <button
                                class="btn cards__buttons border"
                                :class="{ 'active-button': selectedState === 'Pendiente' }"
                                @click="fetchProyectosPorEstado('Pendiente')"
                                :disabled="selectedState === 'Pendiente'"
                            >
                                Pendientes
                            </button>
                        </div>
                    </div>

                    <!-- Botón de navegación derecha -->
                    <div class="col-2 d-flex justify-content-center align-items-center">
                        <button 
                            class="btn cards__buttons w-100"
                            @click="nextPage"
                            :disabled="currentPage === totalPages"
                        >
                            <i class="fa-solid fa-circle-arrow-right fa-2xl"></i>
                        </button>
                    </div>
                </div>     
            </div>
        </div>

        <div class="row">
            <div class="col-12">   
                <p v-if="hasProyectos" class="text-center text-dark mt-3 fs-5">
                    Página {{ currentPage }} de {{ totalPages }}
                </p>
            </div>
            <div v-if="hasProyectos" class="col-12 text-center"> 
                <a  href="#" v-if="currentEtapa == 'Presencial'"  class="textohorario btn fw-semibold border" type="button" data-bs-toggle="modal"
                data-bs-target="#modalHorario">Ver horario</a>
            </div>
          
        </div>
      

        <div v-if="!hasProyectos" class="row justify-content-center mt-5">
            <p class="text-muted text-center fs-4">{{ mensajeSinProyectos }}</p>
        </div>

        
        <!-- Creación de cards con el proyecto -->
        <div v-else class="row justify-content-center mt-3">
            <ProyectosAsignados 
                v-for="(proyecto, index) in proyectos" 
                :key="index" 
                :proyecto="proyecto" 
                :index="(currentPage - 1) * itemsPerPage + index + 1" 
                @component-selected="changeComponent" 
            />
        </div>


        <!-- Modal con los datos del horario -->
        <div class="modal fade" id="modalHorario" tabindex="-1" aria-labelledby="modalHorarioLabel" aria-hidden="true">
            <div class="modal-dialog modal-lg modal-dialog-centered">
                <div class="modal-content border border-dark border-5 rounded-5 text-dark">
                    <div class="modal-header text-center">
                        <h3 class="modal-title mt-3 w-100 fs-4  mr-1" id="modalLabel">Horario</h3>
                        <button type="button" class="btn-close mr-1 mt-3" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body mt-3">
                        <!-- Tabla de horarios -->
                        <div class="table-responsive">
                            <table id="basic-datatables" class="display table table-striped table-hover text-dark">
                                <thead>
                                    <tr>
                                        <th>Título del proyecto</th>
                                        <th>Nombre de la sala</th>
                                        <th>N° de la sala</th>
                                        <th>Hora inicio</th>
                                        <th>Hora fin</th>
                                        <th>Fecha</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="(horario, index) in listaHorario" :key="index">
                                        <td>{{ horario.titulo }} </td>
                                        <td>{{ horario.nombre_sala }}</td>
                                        <td>{{ horario.numero_sala }}</td>
                                        <td>{{ formatearHora(horario.hora_inicio) }}</td>
                                        <td>{{ formatearHora(horario.hora_fin) }}</td>
                                        <td>{{ horario.fecha }}</td>   
                                    </tr>
                                </tbody>
                            </table>
                        </div>

                        <!-- Paginador -->
                        <PaginatorBody :totalPages="totalPagesHorario" @page-changed="cambiarPagina" v-if="totalPagesHorario > 1" />
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
    import { obtenerProyectosAsignados, obtenerProyectosPorEstado, obtenerEtapaActual, obtenerHorarios } from '../services/evaluadorService';
    import ProyectosAsignados from '../components/Users/evaluador/ProyectosAsignados.vue';
    import CalificarProyectoEvaluadorView from './CalificarProyectoEvaluadorView.vue'; 
    import PaginatorBody from '@/components/UI/PaginatorBody.vue';
    import { useAuthStore } from '@/store';     
    import { useToastUtils } from '@/utils/toast'; 

    const { showErrorToast } = useToastUtils();

    export default {
        
        components: {
            ProyectosAsignados,
            CalificarProyectoEvaluadorView ,
            PaginatorBody
        },
        data() {
            return {
                proyectos: [],
                currentPage: 1,
                totalPages: 1,
                itemsPerPage: 6,
                selectedState: '',
                selectedComponent: '',
                selectedProyecto: null, 
                showCalificarProyecto: false,
                currentEtapa: '',
                listaHorario: [],
                totalPagesHorario: 1,
                currentPageHorario: 1,

            };
        },
        computed: {
            hasProyectos() {
                return this.proyectos.length > 0; 
            },

            mensajeSinProyectos() {
                if (!this.selectedState) {
                    return "No tienes proyectos asignados por el momento...";
                } else if (this.selectedState === 'Calificado') {
                    return "No tienes proyectos calificados...";
                } else if (this.selectedState === 'Pendiente') {
                    return "No tienes proyectos pendientes...";
                }
                return "No hay proyectos disponibles.";
            },

            tituloEtapa() {
                return this.currentEtapa === 'Virtual' ? 'Primera Etapa' : 'Segunda Etapa';
            }
        },
        methods: {

            async obtenerHorarios(pagina) {
                try {
                    const authStore = useAuthStore();
                    const user = authStore.user;

                    const response = await obtenerHorarios(user.id_usuario, pagina, 5);

                    this.listaHorario = response.data; 
                    this.totalPagesHorario = response.total_pages; 
                    
                } catch (error) {
                    showErrorToast("Error al obtener los horarios");
                }
            },
       
            async obtenerEtapa() {
                try {
                    const authStore = useAuthStore();
                    const user = authStore.user;

                    const response = await obtenerEtapaActual(user.id_usuario);
                    this.currentEtapa = response.nombre_etapa;

                    this.fetchProyectos();
                } catch (error) {
                    showErrorToast("Error al obtener la etapa actual");
                }
            },

            async fetchProyectos(page = 1) {
                try {
                    this.selectedState = ''; 
    

                    const authStore = useAuthStore();
                    const user = authStore.user;

                    const response = await obtenerProyectosAsignados(this.currentEtapa, user.id_usuario, page, this.itemsPerPage);

                    this.proyectos = response.data; 
                    this.totalPages = response.total_pages; 
                    this.currentPage = page;

                } catch (error) {
                    showErrorToast("Error al obtener proyectos");
                }
            },

            async fetchProyectosPorEstado(estado) {
                try {
                    const authStore = useAuthStore();
                    const user = authStore.user;

                    // Guardar el valor temporal de la página antes de hacer la solicitud
                    let pageToFetch = this.currentPage;

                    // Si el estado seleccionado ha cambiado, resetear la página a 1
                    if (this.selectedState !== estado) {
                        pageToFetch = 1;
                    }

                    this.selectedState = estado;
                    console.log(this.selectedState);

                    // Mapear estado según la etapa actual
                    const estadoMap = {
                        'Calificado': this.currentEtapa === 'Virtual' ? 'C_virtual' : 'C_presencial',
                        'Pendiente': this.currentEtapa === 'Virtual' ? 'P_virtual' : 'P_presencial'
                    };

                    const estadoEnvio = estadoMap[estado] || '';

                    // Hacer la solicitud de proyectos con el estado y página temporales
                    const response = await obtenerProyectosPorEstado(this.currentEtapa, estadoEnvio, user.id_usuario, pageToFetch, this.itemsPerPage);

                    // Actualizar los proyectos y las páginas solo después de recibir la respuesta
                    this.proyectos = response.data.data;
                    this.totalPages = response.data.total_pages;

                    // Si todo es correcto, actualizar la página actual
                    this.currentPage = pageToFetch;

                } catch (error) {
                    showErrorToast("Error al obtener proyectos por estado");
                }
            },

            async nextPage() {
                if (this.currentPage < this.totalPages) {
                    const nextPage = this.currentPage + 1; 
                    if (this.selectedState) {
                        await this.fetchProyectosPorEstado(this.selectedState);
                        this.currentPage++; 
                    } else {
                        await this.fetchProyectos(nextPage);
                    }
                }
            },

            async prevPage() {
                if (this.currentPage > 1) {
                    const prevPage = this.currentPage - 1; 
                    if (this.selectedState) {
                        await this.fetchProyectosPorEstado(this.selectedState);
                        this.currentPage--; 
                    } else {
                        await this.fetchProyectos(prevPage);
                    }
                }
            },

            changeComponent({ componentName, proyecto }) {
                this.selectedComponent = componentName;
                this.selectedProyecto = proyecto; 
                this.showCalificarProyecto = true; 
            },

            handleVolver() {
                this.showCalificarProyecto = false;
                this.fetchProyectos(1);
            },

            cambiarPagina(pagina){
                this.currentPageHorario = pagina;
                this.obtenerHorarios(pagina);
            },

            formatearHora(hora24) {
                // Crear un objeto Date ficticio con la hora recibida
                const [hora, minutos] = hora24.split(':');
                const date = new Date();
                date.setHours(hora);
                date.setMinutes(minutos);

                // Obtener la hora en formato 12 horas
                const horas12 = date.getHours() % 12 || 12; // Si es 0, convertir a 12
                const ampm = date.getHours() >= 12 ? 'P.M.' : 'A.M.'; // Determinar A.M. o P.M.

                // Retornar la hora formateada
                return `${horas12}:${date.getMinutes().toString().padStart(2, '0')} ${ampm}`;
            }
        },
        mounted() {
            this.obtenerEtapa();
            this.obtenerHorarios();
        }
    };
</script>


<style scoped>

    .textohorario{
        background-color: #ffffff;
        width: 30%;
        text-decoration: none;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }
    
    .textohorario:hover {
        background-color: #ffb521;
        transform: scale(1.02); 
        cursor: pointer; 
    }


    thead th {
        white-space: nowrap; /* Evitar que los títulos se apilen */
        font-size: 0.9rem; /* Tamaño de los títulos */
        padding: 8px;
        text-align: center;
    }

    tbody td {
        padding: 6px;
        text-align: center;
        vertical-align: middle;
    }

    td:nth-child(1) {
        width: 25%; 
    }

    td:nth-child(2),
    td:nth-child(3) {
        width: 17%; 
    }

    td:nth-child(4),
    td:nth-child(5) {
        width: 12%; 
    }
    
    .btn-close{
        width: 6px;
        height: 6px;
    }
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

        
    /* Media query para pantallas entre 998px y 766px */
    @media (min-width: 766px) and (max-width: 1920px) {
        .textohorario{
            width: 12%;
        }

        
    }

    /* Media query para pantallas pequeñas */
    @media (max-width: 576px) {
        
        .textohorario{
            font-size: 0.8rem;
            padding: 0.5rem; 
            
        }

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
        .textohorario{
            font-size: 0.8rem;
            padding: 0.5rem; 
        }

        .cards__buttons {
            font-size: 0.9rem;
            padding: 0.5rem; 
        }
        
    }
</style>
