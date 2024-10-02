<template>
    <!-- Contenido principal -->
    <div class="container">
        <div class="row mb-5 mt-2">
            <div class="col">
                <div class="section_title text-center">
                    <h1>Calificar Proyecto</h1>
                    <h2 class="text-muted">{{ tituloEtapa }}</h2> <!-- Título dinámico -->
                </div>
            </div>
        </div>
    </div>
    
    <!-- Pasar el proyecto seleccionado al componente CalificarProyecto -->
    <CalificarProyecto 
        :proyecto="proyectoSeleccionado" 
        @volver="$emit('volver')"
    />
    
    <div class="text-center mb-3">
        <button @click="$emit('volver')" class="btn btn-warning font-weight-bold text-dark">Volver a Proyectos Asignados</button>
    </div>
    <!-- Fin contenido principal -->
</template>

<script>
    import CalificarProyecto from '../components/Users/evaluador/CalificarProyecto.vue';
    import { obtenerEtapaActual } from '../services/evaluadorService';
    import { useAuthStore } from '@/store';  
    import { useToastUtils } from '@/utils/toast'; 

    const { showErrorToast } = useToastUtils();

    export default {
        components: {
            CalificarProyecto
        },
        props: {
            proyectoSeleccionado: {
                type: Object,
                required: true
            }
        },
        data() {
            return {
                currentEtapa: '', // Almacena la etapa actual
            };
        },
        computed: {
            // Computed para el título dinámico
            tituloEtapa() {
                return this.currentEtapa === 'Virtual' ? 'Primera Etapa' : 'Segunda Etapa';
            }
        },
        methods: {
            async obtenerEtapa() {
                try {
                    const authStore = useAuthStore();
                    const user = authStore.user;

                    const response = await obtenerEtapaActual(user.id_usuario);
                    this.currentEtapa = response.nombre_etapa; // Asignar la etapa
                } catch (error) {
                    showErrorToast("Error al obtener la etapa actual");
                }
            }
        },
        mounted() {
            // Obtener la etapa actual al montar el componente
            this.obtenerEtapa();
        },
        emits: ['volver'], 
    };
</script>

<style scoped>

    .text-muted {
        font-size: 1.2rem;
        color: #999;
    }

    .btn-warning {
        width: 300px;
    }
    
</style>