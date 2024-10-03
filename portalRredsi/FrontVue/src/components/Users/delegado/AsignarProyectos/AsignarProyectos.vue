<template>
    <div class="container">
        <div class="row mb-4">
            <div class="col">
                <div class="section_title text-center">
                    <h1>Asignar proyectos</h1>
                </div>
            </div>
        </div>
        <div class="accordion accordion-flush border-bottom mb-4" id="accordionFlushExample">

            <AcordeonProyecto v-for="proyecto in proyectos" :key="proyecto.id_proyecto" :proyecto="proyecto"  />

        </div>
        <!-- Paginador -->
        <PaginatorBody :totalPages="totalPages" @page-changed="cambiarPagina" v-if="totalPages > 1" />


    </div>
</template>

<script>
import PaginatorBody from '../../../UI/PaginatorBody.vue';
import AcordeonProyecto from './AcordeonProyecto.vue';
import { proyectosSinAsignar } from '@/services/delegadoService'

export default {
    data() {
        return {
            proyectos: [],
            totalPages: 0
        }
    },
    methods: {
        async fetchProyectos(pagina_actual) {
            try {
                const response = await proyectosSinAsignar(pagina_actual);
                this.proyectos = response.data.projects;
                this.totalPages = response.data.total_pages;

            } catch (error) {
                alert("Error al obtener proyectos: ", error);
            }
        },
        cambiarPagina(pagina){
            this.fetchProyectos(pagina);
        }
    },// Final de los metodos
    components: {
        AcordeonProyecto,
        PaginatorBody
    }, 
    mounted() {
        this.fetchProyectos();
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
    -webkit-transform: translateX(-50%);
    -moz-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    -o-transform: translateX(-50%);
    transform: translateX(-50%);
    width: 55px;
    height: 4px;
    content: '';
    background: #ffb606;
}
</style>