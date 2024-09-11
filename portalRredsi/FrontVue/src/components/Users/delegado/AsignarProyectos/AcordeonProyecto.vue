<template>
    <div class="accordion-item">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                :data-bs-target="`#flush-collapseProyecto${index}`" aria-expanded="false"
                aria-controls="flush-collapseProyecto1">
                <h4 class="h5">{{ proyecto.titulo }}</h4>
            </button>
        </h2>
        <div :id="`flush-collapseProyecto${index}`" class="accordion-collapse collapse"
            data-bs-parent="#accordionFlushExample">
            <div class="accordion-body text-dark text-start">
                <div class="row">
                    <div class="col-md-4 col-12">
                        <p class="mb-2 text-dark"><strong>Modalidad:</strong></p>
                        <p class="text-dark">{{ proyecto.modalidad }}</p>
                    </div>
                    <div class="col-md-4 col-12">
                        <p class="mb-2 text-dark"><strong>Institución:</strong></p>
                        <p class="text-dark">{{ proyecto.institucion }}</p>
                    </div>
                    <div class="col-md-4 col-12">
                        <p class="mb-2 text-dark"><strong>Autores:</strong></p>
                        <span class="text-dark" v-for="(autor, i) in autores" :key="i">{{ i > 0 ?
                            `,
                            ${autor.nombre}` : autor.nombre }}</span>
                    </div>
                </div>
                <div class="row">
                    <div class="col-md-4 col-12">
                        <p class="mb-2 text-dark"><strong>Área de conocimiento:</strong></p>
                        <p class="text-dark">{{ proyecto.area_conocimiento }}</p>
                    </div>
                </div>
                <div class="row mt-4 justify-content-center">
                    <div class="col-md-6 col-12">
                        <label for="" class="Text-dark fw-bold">Seleccionar evaluador:</label>
                        <select class="form-select text-dark">
                            <option selected>Seleccionar evaluador</option>
                            <option v-for="(posibleEvaluador, index) in posiblesEvaluadores.data" :key="index"
                                :value="posibleEvaluador">
                                {{ posibleEvaluador.nombres }} {{ posibleEvaluador.apellidos }}</option>
                        </select>
                    </div>
                    <div class="col-md-6 col-12 mb-5">
                        <label for="" class="text-dark fw-bold">Otro evaluador diferente a los sugeridos:</label>
                        <div class="d-flex align-items-center position-relative">
                            <input type="text" class="form-control text-dark"
                                placeholder="Identificación del evaluador">
                            <p class="d-inline-flex gap-1 mb-0">
                                <a data-bs-toggle="collapse" :href="`#collapseExample${index}`" role="button"
                                    aria-expanded="false" :aria-controls="`collapseExample${index}`"
                                    style="background: white; border: none;">
                                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960"
                                        width="24px" fill="#000000" class="ms-2">
                                        <path
                                            d="M440-280h80v-240h-80v240Zm40-320q17 0 28.5-11.5T520-640q0-17-11.5-28.5T480-680q-17 0-28.5 11.5T440-640q0 17 11.5 28.5T480-600Zm0 520q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z" />
                                    </svg>
                                </a>
                            </p>
                        </div>
                        <div class="collapse" :id="`collapseExample${index}`">
                            <div class="card card-body mt-2">
                                Este campo es opcional.
                                Visita la lista de evaluadores si deseas tener más clara tu selección
                                <a href="lista_evaluadores.html" target="_blank">Haz click aquí</a>
                            </div>
                        </div>
                    </div>
                    <div class=" col-md-6 col-12 text-center">
                        <a href="#" class="btn w-100 mt-1 fw-bold" style="background: rgb(255, 182, 6);">ASIGNAR</a>
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { obtenerAutoresProyecto, obtenerIdAreaConocimiento, obtenerPosiblesEvaluadores, obtenerIdInstitucion, obtenerListaEvaluadores } from '../../../../services/delegadoService'

export default {
    props: {
        proyecto: Object,
        index: Number
    },
    data() {
        return {
            posiblesEvaluadores: [],
            autores : [] 
        }
    },
    methods: {
        async asignarAutoresAProyectos() {
            try {
                const autores_cant = await obtenerAutoresProyecto(this.proyecto.id_proyecto);
            
                if (autores_cant){
                    this.autores = autores_cant.data; 
                }
            } catch (error) {
                console.log(`Proyecto ${this.proyecto.titulo} Sin autores`)
            }

        },
        async fetchPosiblesEvaluadores() {
            try {
                const id_area_conocimiento = await obtenerIdAreaConocimiento(this.proyecto.area_conocimiento);
                const id_institucion = await obtenerIdInstitucion(this.proyecto.institucion)

                const response = await obtenerPosiblesEvaluadores(id_area_conocimiento.data.id_area_conocimiento, id_institucion.data.id_institucion);

                this.posiblesEvaluadores = response.data;

                if(this.posiblesEvaluadores.detail == "No hay evaluadores disponibles"){
                    this.posiblesEvaluadores = await obtenerListaEvaluadores();
                }

            } catch (error) {
                alert("Error al obtener proyectos: ", error);
            }
        },
    },
    mounted() {
        this.asignarAutoresAProyectos();
        this.fetchPosiblesEvaluadores();
    }
}
</script>

<style scoped>
.accordion-button:not(.collapsed) {
    background-color: rgb(255, 182, 6);
    /* Color amarillo */
    color: #000;
    /* Color del texto en la cabecera expandida */
}

.accordion-button {
    color: #000;
    /* Color del texto en la cabecera no expandida */
}

.accordion-button::after {
    filter: invert(0);
    /* Mantiene el color del icono de colapso en negro */
}
</style>