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
                        fill="#12d336">
                        <path
                            d="M720-120H280v-520l280-280 50 50q7 7 11.5 19t4.5 23v14l-44 174h258q32 0 56 24t24 56v80q0 7-2 15t-4 15L794-168q-9 20-30 34t-44 14Zm-360-80h360l120-280v-80H480l54-220-174 174v406Zm0-406v406-406Zm-80-34v80H160v360h120v80H80v-520h200Z" />
                    </svg>
                    <span class="text-dark">Evaluador Aceptado</span>
                </div>
                <div class="col-3 col-sm-3">
                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                        fill="#f50c0c">
                        <path
                            d="M240-840h440v520L400-40l-50-50q-7-7-11.5-19t-4.5-23v-14l44-174H120q-32 0-56-24t-24-56v-80q0-7 2-15t4-15l120-282q9-20 30-34t44-14Zm360 80H240L120-480v80h360l-54 220 174-174v-406Zm0 406v-406 406Zm80 34v-80h120v-360H680v-80h200v520H680Z" />
                    </svg>
                    <span class="text-dark">Evaluador Rechazado</span>
                </div>
                <div class="col-3 col-sm-3">
                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                        fill="#00000">
                        <path
                            d="M720-120H280v-520l280-280 50 50q7 7 11.5 19t4.5 23v14l-44 174h258q32 0 56 24t24 56v80q0 7-2 15t-4 15L794-168q-9 20-30 34t-44 14Zm-360-80h360l120-280v-80H480l54-220-174 174v406Zm0-406v406-406Zm-80-34v80H160v360h120v80H80v-520h200Z" />
                    </svg>
                    <span class="text-dark">Evaluador Pendiente</span>
                </div>
            </div>
            <div class="accordion accordion-flush" id="accordionFlushExample">
                <AcordeonPostulaciones v-for="(evaluador, index) in evaluadores" :key="index" :evaluador="evaluador"
                    :index="index" />
            </div>
        </div>
    </div>
</template>

<script>
import { getApplicationsByPage} from '@/services/PostulacionService';
import AcordeonPostulaciones from "./AcordeonPostulaciones.vue";

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
        // Obtiene los usuarios de la página actual
        async fetcEvaluators() {
            try {
                const response = await getApplicationsByPage(this.currentPage);
                this.users = response.data.users; // Asigna los usuarios obtenidos
                this.totalPages = response.data.total_pages; // Asigna el total de páginas
            } catch (error) {
                console.log(error);
            }
        },

        // Función para ir a la página siguiente
        nextPage() {
            if (this.currentPage < this.totalPages) {
                this.currentPage++; // incrementa el valor
                this.fetchUsers(); // Recarga la lista de usuarios para la nueva página
            }
        },

        // Función para ir a la página anteior
        prevPage() {
            if (this.currentPage > 1) {
                this.currentPage--; // disminuye el valor
                this.fetchUsers(); // Recarga la lista de usuarios para la nueva página
            }
        },

        // Formatea una fecha para mostrarla de manera legible
        formatDate(dateString) {
            const options = {
                year: 'numeric',
                month: 'numeric',
                day: 'numeric',
                hour: '2-digit',
                minute: '2-digit'
            };
            return new Date(dateString).toLocaleDateString('es-ES', options);
        },

        // Elimina un usuario
        async deleteUserMethod(userId) {
            if (confirm('¿Estás seguro de que deseas eliminar este usuario?')) {
                try {
                    await deleteUser(userId); // Llama a la API para eliminar el usuario
                    alert('Usuario eliminado exitosamente');
                    this.fetchUsers(); // Refresca la lista de usuarios después de eliminar
                } catch (error) {
                    // Maneja el error utilizando un método auxiliar
                    alert(error.data.detail);
                }
            }
        },

        // Abre el modal para registrar un nuevo usuario
        openCreateModal() {
            // Inicializa los campos vacios
            this.currentUser = { full_name: '', mail: '', user_role: '', passhash: '' }; // Inicializa el usuario vacío
            this.isEditMode = false; // Cambia el modo a editar a falso
            $('#userModal').modal('show'); // Abre el modal
        },

        // Abre el modal para editar un usuario
        openEditModal(user) {
            this.currentUser = { ...user }; // Clona el usuario seleccionado
            this.isEditMode = true; // Cambia el modo a editar a verdadero
            $('#userModal').modal('show'); // Abre el modal
        },

        // Registra un nuevo usuario llamando a la API
        async registerUser() {
            try {
                // Usa la función createUser (llamando a la API) para crear un nuevo usuario 
                await createUser(this.currentUser.full_name, this.currentUser.mail, this.currentUser.user_role, this.currentUser.passhash);
                alert('Usuario registrado exitosamente');
                this.fetchUsers(); // Refresca la lista de usuarios después de registrar
                $('#userModal').modal('hide'); // Cierra el modal
            } catch (error) {
                // Maneja el error utilizando un método auxiliar
                alert(error.data.detail);
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
