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
            <div class="row justify-content-center mb-4">
                <div class="col-3 col-sm-3">
                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                        fill="#00000">
                        <path
                            d="M240-840h440v520L400-40l-50-50q-7-7-11.5-19t-4.5-23v-14l44-174H120q-32 0-56-24t-24-56v-80q0-7 2-15t4-15l120-282q9-20 30-34t44-14Zm360 80H240L120-480v80h360l-54 220 174-174v-406Zm0 406v-406 406Zm80 34v-80h120v-360H680v-80h200v520H680Z" />
                    </svg>
                    <span class="text-dark">Rechazar Evaluador</span>
                </div>
                <div class="col-3 col-sm-3">
                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                        fill="#00000">
                        <path
                            d="M720-120H280v-520l280-280 50 50q7 7 11.5 19t4.5 23v14l-44 174h258q32 0 56 24t24 56v80q0 7-2 15t-4 15L794-168q-9 20-30 34t-44 14Zm-360-80h360l120-280v-80H480l54-220-174 174v406Zm0-406v406-406Zm-80-34v80H160v360h120v80H80v-520h200Z" />
                    </svg>
                    <span class="text-dark"> Aceptar Evaluador</span>
                </div>
            </div>
            <div class="accordion accordion-flush" id="accordionFlushExample">
                <AcordeonPostulaciones v-for="(evaluator,index) in evaluators" :key="index" :evaluator="evaluator" :index="index"/>
            </div>
        </div>
    </div>
</template>

<script>
import { getApplicationsByPage} from '@/services/PostulacionService';
import AcordeonPostulaciones from "'../components/Users/delegado/postulaciones/AcordeonPostulaciones.vue'";

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

        // Actualiza un usuario llamando a la API
        async updateUser() {
            try {
                await updateUser(this.currentUser.user_id, this.currentUser.full_name, this.currentUser.mail, this.currentUser.user_role);
                alert('Usuario actualizado exitosamente');
                this.fetchUsers(); // Refresca la lista de usuarios después de actualizar
                $('#userModal').modal('hide'); // Cierra el modal
            } catch (error) {
                // Maneja el error utilizando un método auxiliar
                alert(error.data.detail);
            }
        },

    }, // end-methods
    mounted() {
        this.fetchUsers(); // Llama al método para obtener al cargar este componente
    },
};
</script>
