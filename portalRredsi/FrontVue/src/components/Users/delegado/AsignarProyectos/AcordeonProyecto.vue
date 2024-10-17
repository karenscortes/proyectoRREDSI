<template>
    <div class="accordion-item">
        <h2 class="accordion-header">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse"
                :data-bs-target="`#flush-collapseProyecto${proyecto.id_proyecto}`" aria-expanded="false"
                aria-controls="flush-collapseProyecto1" @click="abrirAcordeon">
                <h4 class="h5">{{ proyecto.titulo }}</h4>
            </button>
        </h2>
        <div :id="`flush-collapseProyecto${proyecto.id_proyecto}`" class="accordion-collapse collapse"
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
                        <span class="text-dark" v-for="(autor, i) in autores" :key="i">
                            {{ i > 0 ?
                                `,
                            ${autor.nombre}` : autor.nombre }}
                        </span>
                        <span v-if="autores.length == 0"> No se registraron autores </span>

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
                        <select class="form-select text-dark" v-model="evaluadorSeleccionado">
                            <option :value="null" disabled selected>Seleccionar evaluador</option>
                            <option v-if="evaluadoresEspecificos"
                                v-for="(posibleEvaluador, index) in posiblesEvaluadores" :key="index"
                                :value="posibleEvaluador.id">
                                {{ posibleEvaluador.nombre }} {{ posibleEvaluador.apellido }}
                            </option>

                            <option v-else v-for="(posibleEvaluador, i) in posiblesEvaluadores" :key="i"
                                :value="posibleEvaluador.id_usuario">
                                {{ posibleEvaluador.nombres }} {{ posibleEvaluador.apellidos }}
                            </option>
                            <option :value="'otro'">Otro:</option>
                        </select>
                    </div>
                    <div class="col-md-6 col-12 mb-5">
                        <label for="" class="text-dark fw-bold">Otro evaluador diferente a los sugeridos:</label>
                        <div class="d-flex align-items-center position-relative">

                            <input type="text" class="form-control text-dark" placeholder="Nombre del evaluador"
                                v-model="valor_buscado" @keyup="buscarEvaluador" @keyup.delete="buscarEvaluador">
                            <select v-model="evaluadorBuscado" class="ml-2 form-select text-dark p-1 w-50"
                                id="evaluadorSelect" required :disabled="buscoEvaluadorOpcionales">
                                <option :value="null" disabled selected>Seleccionar</option>
                                <option v-for="(evaluador, index) in otrosEvaluadores" :key="evaluador.id_usuario"
                                    :value="evaluador.id_usuario">
                                    {{ evaluador.nombres }} {{ evaluador.apellidos }}
                                </option>
                            </select>
                            <p class="d-inline-flex gap-1 mb-0">
                                <a data-bs-toggle="collapse" :href="`#collapseExample${proyecto.id_proyecto}`"
                                    role="button" aria-expanded="false"
                                    :aria-controls="`collapseExample${proyecto.id_proyecto}`"
                                    style="background: white; border: none;">
                                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960"
                                        width="24px" fill="#000000" class="ms-2">
                                        <path
                                            d="M440-280h80v-240h-80v240Zm40-320q17 0 28.5-11.5T520-640q0-17-11.5-28.5T480-680q-17 0-28.5 11.5T440-640q0 17 11.5 28.5T480-600Zm0 520q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480q0-83 31.5-156T197-763q54-54 127-85.5T480-880q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm0-80q134 0 227-93t93-227q0-134-93-227t-227-93q-134 0-227 93t-93 227q0 134 93 227t227 93Zm0-320Z" />
                                    </svg>
                                </a>
                            </p>
                        </div>
                        <div class="collapse" :id="`collapseExample${proyecto.id_proyecto}`">
                            <div class="card card-body mt-2">
                                Este campo es opcional.
                                Visita la lista de evaluadores si deseas tener más clara tu selección.
                            </div>
                        </div>
                    </div>
                    <div class=" col-md-6 col-12 text-center">
                        <a @click="asignarProyecto()" class="btn w-100 mt-1 fw-bold"
                            style="background: rgb(255, 182, 6);">ASIGNAR</a>
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { obtenerAutoresProyecto, obtenerIdAreaConocimiento, obtenerPosiblesEvaluadores, obtenerIdInstitucion, obtenerListaEvaluadores, obtenerProyectoConvocatoria, asignarProyectoEtapaVirtual, obtenerIdEvaluador, actualizarEstadoProyecto } from '@/services/delegadoService'
import { ref } from 'vue'
import { useToastUtils } from '@/utils/toast';

export default {
    props: {
        proyecto: Object,
    },
    data() {
        return {
            posiblesEvaluadores: [],
            evaluadoresEspecificos: true,
            evaluadorSeleccionado: ref(null),
            evaluadorBuscado: ref(null),
            valor_buscado: ref(""),
            desplegarAcordeon: false,
            otrosEvaluadores: [],
            autores: [],
            buscoEvaluadorOpcionales: true
        }
    },
    setup() {
        const { showSuccessToast, showErrorToast, showWarningToast, showInfoToast } = useToastUtils();
        return {
            showSuccessToast,
            showErrorToast,
            showWarningToast,
            showInfoToast
        }
    },

    methods: {
        async asignarAutoresAProyectos(id_proyecto) {
            try {
                const autores_cant = await obtenerAutoresProyecto(id_proyecto);
                this.autores = autores_cant.data;
            } catch (error) {
                console.log("Sin autores registrados");
            }

        },
        async fetchPosiblesEvaluadores(p_area_conocimiento, p_institucion) {
            try {
                const id_area_conocimiento = await obtenerIdAreaConocimiento(p_area_conocimiento);
                const id_institucion = await obtenerIdInstitucion(p_institucion)

                const response = await obtenerPosiblesEvaluadores(id_area_conocimiento.data.id_area_conocimiento, id_institucion.data.id_institucion);

                this.posiblesEvaluadores = response.data.posibles_evaluadores;
                console.log(this.posiblesEvaluadores)
                if (this.posiblesEvaluadores == undefined) {
                    const lista_completa_evaluadores = await obtenerListaEvaluadores();
                    this.posiblesEvaluadores = lista_completa_evaluadores.data.evaluators;
                    this.evaluadoresEspecificos = false;
                }
                // console.log(this.posiblesEvaluadores)

            } catch (error) {
                this.showInfoToast("No se pudo obtener evaluadores");
            }
        },
        async obtenerIdProyectoConvocatoria() {
            try {
                const response = await obtenerProyectoConvocatoria(this.proyecto.id_proyecto);
                let id_proyecto_convocatoria = response.data.proyecto_convocatoria.id_proyecto_convocatoria
                    ;
                return id_proyecto_convocatoria;

            } catch (error) {
                console.error("Error al obtener id de proyecto convocatoria");
            }
        },
        async asignarProyecto() {

            let id_evaluador = null;
            let id_proyecto_convocatoria = await this.obtenerIdProyectoConvocatoria();

            // validaciones para que se ingrese un evaluador correctamente
            if (this.evaluadorSeleccionado == null && this.evaluadorBuscado == null ||
                this.evaluadorSeleccionado == "otro" && this.evaluadorBuscado == null) {
                this.showWarningToast("Debes seleccionar un evaluador");
                return;
            } else if (this.evaluadorSeleccionado != null && this.evaluadorSeleccionado != "otro" &&
                this.evaluadorBuscado != null) {
                this.showWarningToast("Debes seleccionar un solo evaluador");
                return;
            }else if (this.evaluadorSeleccionado == null && this.evaluadorBuscado != null) {
                this.showWarningToast("Debes seleccionar 'Otro' en la primera opción, intenta de nuevo");
                return;
            
            } else if (this.evaluadorSeleccionado == "otro" && this.evaluadorBuscado != null) {
                // try {
                //     const response = await obtenerIdEvaluador(this.evaluadorBuscado);
                    id_evaluador = this.evaluadorBuscado;

                // } catch (error) {
                //     this.showWarningToast("Evaluador no encontrado, intenta de nuevo");
                //     return;
                // }
            } else if (this.evaluadorSeleccionado != null && this.evaluadorBuscado == null) {
                id_evaluador = this.evaluadorSeleccionado;
            }

            try {
                const datosAsignacion = {
                    "id_usuario": id_evaluador,
                    "id_proyecto": this.proyecto.id_proyecto,
                    "id_etapa": 2,
                    "id_proyecto_convocatoria": id_proyecto_convocatoria
                }
                console.log(datosAsignacion)
                await asignarProyectoEtapaVirtual(datosAsignacion);

                // Actualiza el estado del proyecto a asignado para que salga de la vista
                await actualizarEstadoProyecto(this.proyecto.id_proyecto);

                this.showSuccessToast("Proyecto asignado con exito");
                this.actualizarListaProyectos();
            } catch (error) {
                this.showErrorToast("Error al asignar proyecto");
            }
            this.evaluadorSeleccionado = null;
            this.evaluadorBuscado == null;
        },
        async ProyectoSelecionado() {
            await this.obtenerIdProyectoConvocatoria();
            await this.fetchPosiblesEvaluadores(this.proyecto.area_conocimiento, this.proyecto.institucion);
            await this.asignarAutoresAProyectos(this.proyecto.id_proyecto);
        },
        async buscarEvaluador() {
            try {
                if (this.valor_buscado.trim() != "") {
                    const evaluador = await obtenerIdEvaluador(this.valor_buscado);
                    this.otrosEvaluadores = evaluador.data;
                    this.totalPages = 0;
                    this.buscoEvaluadorOpcionales = false;
                }
                if(this.valor_buscado.trim() == ""){
                    this.otrosEvaluadores = '';
                    this.totalPages = 0;
                    this.buscoEvaluadorOpcionales = true;
                }

            } catch (error) {
                this.showWarningToast("No se ha podido encontrar el evaluador");
            }
        },
        abrirAcordeon() {
            this.desplegarAcordeon = !this.desplegarAcordeon;
            if (this.desplegarAcordeon) {
                this.ProyectoSelecionado();
            }
        },
        actualizarListaProyectos() {
            // Emitir evento para que el padre actualice la lista de proyectos sin asignar
            this.$emit('actualizarListaProyectos');
        }
    },
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