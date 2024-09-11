<template>
    <div class="container mt-5">
        <!-- Título de la sección -->
        <div class="row mb-3 mt-2">
            <div class="col">
                <div class="section_title text-center">
                    <h1>Postulaciones</h1>
                </div>
            </div>
        </div>

        <!-- Información evaluadores -->
        <div class="container mt-5">
            <div class="row justify-content-center text-center mb-4">
                <div class="col-3 col-sm-3">
                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                        fill="#f50c0c">
                        <path
                            d="M240-840h440v520L400-40l-50-50q-7-7-11.5-19t-4.5-23v-14l44-174H120q-32 0-56-24t-24-56v-80q0-7 2-15t4-15l120-282q9-20 30-34t44-14Zm360 80H240L120-480v80h360l-54 220 174-174v-406Zm0 406v-406 406Zm80 34v-80h120v-360H680v-80h200v520H680Z" />
                    </svg>
                    <span class="text-dark">Rechazar Evaluador</span>
                </div>
                <div class="col-3 col-sm-3">
                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                        fill="#12d336">
                        <path
                            d="M720-120H280v-520l280-280 50 50q7 7 11.5 19t4.5 23v14l-44 174h258q32 0 56 24t24 56v80q0 7-2 15t-4 15L794-168q-9 20-30 34t-44 14Zm-360-80h360l120-280v-80H480l54-220-174 174v406Zm0-406v406-406Zm-80-34v80H160v360h120v80H80v-520h200Z" />
                    </svg>
                    <span class="text-dark"> Aceptar Evaluador</span>
                </div>
            </div>
            <div class="accordion accordion-flush" id="accordionFlushExample">
                <AcordeonPostulaciones v-for="(evaluator,index) in evaluators" :key="index" :evaluator="evaluator" :index="index" @notify="handleNotification"/>
            </div>

            <!-- Paginador -->
            <div v-if="totalPages > 1" class="mt-5">
                <div aria-label="Page navigation example mb-5">
                    <ul class="pagination justify-content-center">
                        <li class="page-item m-1">
                            <button @click="prevPage" :disabled="current_page == 1" class="page-link"
                                style="border-radius: 20px; color: black;">Previous</button>
                        </li>
                        <li v-for="i in totalPages"  :key="i" class="page-item rounded m-1">
                            <button @click="selectedPage(i)" class="page-link rounded-circle" style="color: black;">{{ i
                                }}</button>
                        </li>
                        <li class="page-item m-1">
                            <button @click="nextPage" :disabled="current_page == totalPages" class="page-link"
                                style="border-radius: 20px; color: black;">Next</button>
                        </li>
                    </ul>
                </div>
        </div>
        </div>
    </div>
</template>

<script>
import { getApplicationsByPage} from '@/services/PostulacionService';
import AcordeonPostulaciones from './AcordeonPostulaciones.vue';

export default {
    components: {
        AcordeonPostulaciones,
    },
    data() {
        return {
            evaluators: [],  
            currentEvaluator: {},  
            currentPage: 1, 
            totalPages: 0,
        };
    },
    methods: {
        handleNotification() {
            this.fetchEvaluators();
        },
        async fetchEvaluators() {
            try {
                const response = await getApplicationsByPage(this.currentPage);
                this.evaluators = response.data.applications; 
                this.totalPages = response.data.total_pages;
            } catch (error) {
                console.log(error);
            }
        },

        nextPage() {
            if (this.currentPage < this.totalPages) {
                this.currentPage++; 
                this.fetchEvaluators(); 
            }
        },

        prevPage() {
            if (this.currentPage > 1) {
                this.currentPage--;
                this.fetchEvaluators(); 
            }
        },

        selectedPage(pagina) {
            this.current_page = pagina;
            this.fetchProyectos();
        },
    }, 
    mounted() {
        this.fetchEvaluators(); // Llama al método para obtener al cargar este componente
    },
};
</script>
