<template>
    <!-- Contenido principal -->
    <div class="container pt-5">
        <div class="row mb-5 mt-2">
            <div class="col">
                <div class="section_title text-center">
                    <h1>Proyectos Asignados</h1>
                    <h2 class="text-muted">Primera Etapa</h2>
                </div>
            </div>
        </div>

        <div class="row justify-content-center mt-3">
            <div class="col-xl-10 col-lg-8 col-md-8">
                <div class="row row-cols-3 row-cols-sm-3 row-cols-md-4">
                    <div class="col text-left">
                        <button 
                            class="btn cards__buttons w-100 h-100"
                            @click="prevPage"
                            :disabled="currentPage === 1"
                        >
                            <i class="fa-solid fa-circle-arrow-left fa-2xl"></i>
                        </button>
                    </div>
                    <div class="col text-center pt-1 mid_tab">
                        <button
                            class="btn cards__buttons border"
                            :class="{ 'active-button': selectedState === 'Calificado' }"
                            @click="fetchProyectosPorEstado('Calificado')"
                        >
                            Calificados
                        </button>
                    </div>
                    <div class="col text-center pt-1">
                        <button
                            class="btn cards__buttons border"
                            :class="{ 'active-button': selectedState === 'Pendiente' }"
                            @click="fetchProyectosPorEstado('Pendiente')"
                        >
                            Pendientes
                        </button>
                    </div>
                    <div class="col text-right">
                        <button 
                            class="btn cards__buttons w-100 h-100"
                            @click="nextPage"
                            :disabled="currentPage === totalPages"
                        >
                            <i class="fa-solid fa-circle-arrow-right fa-2xl"></i>
                        </button>
                    </div>
                </div>     
            </div>
        </div>

        <p v-if="hasProyectos" class="text-center mt-4 fs-5">
            Página {{ currentPage }} de {{ totalPages }}
        </p>

        <div v-if="!hasProyectos" class="row justify-content-center mt-5">
            <p class="text-muted text-center fs-4">{{ mensajeSinProyectos }}</p>
        </div>

        <div v-else class="row justify-content-center mt-3">
            <ProyectosAsignados v-for="(proyecto, index) in proyectos" :key="index" :proyecto="proyecto" />
        </div>
    </div>
    <!-- Fin contenido principal -->
</template>

<script>
    import { obtenerProyectosAsignados, obtenerProyectosPorEstado } from '../services/evaluadorService';
    import ProyectosAsignados from '../components/Users/evaluador/ProyectosAsignados.vue';
    import { useAuthStore } from '@/store';    

    export default {
        components: {
            ProyectosAsignados,
        },
        data() {
            return {
                proyectos: [],         
                currentPage: 1,       
                totalPages: 1,         
                itemsPerPage: 6,      
                selectedState: '',    
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
            }
        },
        methods: {
            async fetchProyectos(page = 1) {
                try {
                    const authStore = useAuthStore();
                    const user = authStore.user;

                    const response = await obtenerProyectosAsignados(user.id_usuario, page, this.itemsPerPage);

                    this.proyectos = response.data.data; 
                    this.totalPages = response.data.total_pages; 
                    this.currentPage = page;

                } catch (error) {
                    console.error("Error al obtener proyectos: ", error);
                    alert("Error al obtener proyectos");
                }
            },

            async fetchProyectosPorEstado(estado) {
                try {
                    const authStore = useAuthStore();
                    const user = authStore.user;
                    
                    this.selectedState = estado;

                    const response = await obtenerProyectosPorEstado(estado, user.id_usuario, this.currentPage, this.itemsPerPage);

                    this.proyectos = response.data.data;
                    this.totalPages = response.data.total_pages;

                } catch (error) {
                    console.error("Error al obtener proyectos por estado: ", error);
                    alert("Error al obtener proyectos por estado");
                }
            },

            nextPage() {
                if (this.currentPage < this.totalPages) {
                    if (this.selectedState) {
                        this.fetchProyectosPorEstado(this.selectedState);
                    } else {
                        this.fetchProyectos(this.currentPage + 1);
                    }
                }
            },
            prevPage() {
                if (this.currentPage > 1) {
                    if (this.selectedState) {
                        this.fetchProyectosPorEstado(this.selectedState);
                    } else {
                        this.fetchProyectos(this.currentPage - 1);
                    }
                }
            }
        },
        mounted() {
            this.fetchProyectos();
        }
    };
</script>


<style scoped>
    .cards__buttons {
        background-color: #fff;
        width: 100%;
        transition: background-color 0.3s ease, transform 0.2s ease;
    }

    .cards__buttons:hover {
        background-color: #f3f3f3;
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
</style>
