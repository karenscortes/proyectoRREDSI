<template>
    <div class="container pt-5 mt-5">
        <div class="row mb-4 mt-5">
            <div class="col">
                <div class="section_title text-center">
                    <h1>Asignar proyectos</h1>
                </div>
            </div>
        </div>
        <div class="accordion accordion-flush border-bottom" id="accordionFlushExample">

            <AcordeonProyecto v-for="(proyecto, index) in proyectos" :key="index" :proyecto="proyecto" :index="index" />

        </div>
        <!-- Paginador -->
        <div v-if="totalPages > 1" class="mt-5">
            <div aria-label="Page navigation example mb-5">
                <ul class="pagination justify-content-center">
                    <li class="page-item m-1">
                        <button @click="prevPage" :disabled="current_page == 1" class="page-link"
                            style="border-radius: 20px; color: black;">Previous</button>
                    </li>
                    <li v-for="i in totalPages" class="page-item rounded m-1">
                        <button @click="paginaSeleted(i)" class="page-link rounded-circle" style="color: black;">{{ i
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
</template>

<script>
import AcordeonProyecto from './AcordeonProyecto.vue';
import { proyectosSinAsignar } from '../../../../services/delegadoService'

export default {
    data() {
        return {
            proyectos: [],
            current_page: 1,
            totalPages: 0
        }
    },
    methods: {
        async fetchProyectos() {
            try {
                const response = await proyectosSinAsignar(this.current_page);
                this.proyectos = response.data.projects;
                this.totalPages = response.data.total_pages;

            } catch (error) {
                alert("Error al obtener proyectos: ", error);
            }
        },
        nextPage() {
            if (this.current_page < this.totalPages) {
                this.current_page++;
                this.fetchProyectos();
            }
        },
        prevPage() {
            if (this.current_page > 1) {
                this.current_page--;
                this.fetchProyectos();
            }
        },
        paginaSeleted(pagina) {
            this.current_page = pagina;
            this.fetchProyectos();
        }
    },
    components: {
        AcordeonProyecto
    }, // Final de los metodos
    mounted() {
        this.fetchProyectos();
    }
}

</script>
<style>
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