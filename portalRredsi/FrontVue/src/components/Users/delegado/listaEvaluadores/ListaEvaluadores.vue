<template>
    <div>
        <div class="container pt-5">
            <div class="row mb-5 mt-2">
                <div class="col">
                    <div class="section_title text-center">
                        <h1>Evaluadores Registrados</h1>
                    </div>
                </div>
            </div>
            <!-- buscador -->
            <div class="row mb-4 justify-content-end">
                <div class="col-8 col-sm-6 justify-content-end">
                    <div class="row justify-content-end">
                        <div class="col-8">
                            <input type="text" id="busqueda" class="form-control" placeholder="Buscar...">
                        </div>
                        <div class="col-4">
                            <button class="btn btn-buscar w-100 font-weight-bold">Buscar</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- tabla -->
            <div class="table-responsive">
                <table id="basic-datatables" class="display table table-striped table-hover text-dark">
                    <thead style="background: rgb(255, 182, 6)
;">
                        <tr>
                            <th>Evaluador</th>
                            <th>Area de conocimiento</th>
                            <th>Institucion</th>
                            <th>Estado</th>
                            <th>Detalle</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(evaluador, index) in evaluadores" :key="index">
                            <td>{{ evaluador.nombres }} {{ evaluador.apellidos  }}</td>
                            <td>{{ evaluador.area_conocimiento }}</td>
                            <td>{{ evaluador.nombre_institucion }}</td>
                            <td class="pl-4">
                                <div class="custom-control custom-switch d-flex">
                                    <input type="checkbox" class="custom-control-input" :id="index"
                                        :checked="evaluador.estado == 'activo' ? true : false" @click="actualizarEvaluador(evaluador.id_usuario,evaluador.estado)">
                                    <label class="custom-control-label" :for="index"></label>
                                </div>
                            </td>
                            <td>
                                <a href="#" @click="obtenerEvaluadorActual(evaluador)"
                                    class="btn-sm font-weight-bold text-dark" type="button" data-bs-toggle="modal"
                                    data-bs-target="#delegateInformation">
                                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960"
                                        width="24px" fill="#00000">
                                        <path
                                            d="M560-440h200v-80H560v80Zm0-120h200v-80H560v80ZM200-320h320v-22q0-45-44-71.5T360-440q-72 0-116 26.5T200-342v22Zm160-160q33 0 56.5-23.5T440-560q0-33-23.5-56.5T360-640q-33 0-56.5 23.5T280-560q0 33 23.5 56.5T360-480ZM160-160q-33 0-56.5-23.5T80-240v-480q0-33 23.5-56.5T160-800h640q33 0 56.5 23.5T880-720v480q0 33-23.5 56.5T800-160H160Zm0-80h640v-480H160v480Zm0 0v-480 480Z" />
                                    </svg>
                                </a>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
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

        <!-- Modal datos -->
        <div class="modal fade" id="delegateInformation" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content border border-dark border-5 rounded-5 text-dark">
                    <div class="modal-header text-center">
                        <h3 class="modal-title mt-5 w-100" id="modalLabel">{{ evaluadorActual.nombres }}</h3>
                        <button type="button" class="btn-close mr-3 mt-3" data-bs-dismiss="modal"
                            aria-label="Close"></button>
                    </div>
                    <div class="modal-body mt-3">
                        <div class="row justify-content-center text-start">
                            <div class="col-5 text-dark font-weight-bold px-3">Nombre Completo:</div>
                            <div class="col-5 border mb-3 px-3">
                                <span class="text-dark">{{ evaluadorActual.nombres }}</span>
                            </div>
                            <div class="col-5 text-dark font-weight-bold px-3">Institución:</div>
                            <div class="col-5 border mb-3 px-3">
                                <span class="text-dark">{{ evaluadorActual.institucion }}</span>
                            </div>
                            <div class="col-5 text-dark font-weight-bold px-3">Teléfono:</div>
                            <div class="col-5 border mb-3 px-3">
                                <span class="text-dark">{{ evaluadorActual.telefono }}</span>
                            </div>
                            <div class="col-5 text-dark font-weight-bold px-3">Correo:</div>
                            <div class="col-5 border mb-3 px-3">
                                <span class="text-dark">{{ evaluadorActual.correo }}</span>
                            </div>
                            <div class="col-5 text-dark font-weight-bold px-3">Área de conocimiento:</div>
                            <div class="col-5 border mb-3 px-3">
                                <span class="text-dark">{{ evaluadorActual.areaConocimiento }}</span>
                            </div>
                            <div class="col-5 text-dark font-weight-bold px-3">Otra área de conocimiento:</div>
                            <div class="col-5 border mb-3 px-3">
                                <span class="text-dark">{{ evaluadorActual.otraAreaConocimiento }}</span>
                            </div>
                            <div class="text-center mt-3">
                                <button :href="evaluadorActual.urlArchivo" class="btn text-dark fw-semibold" target="_blank">
                                    Ver Títulos
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>

</template>

<script>
import { reactive } from 'vue';
import { obtenerListaEvaluadores, actualizarEstadoEvaluador } from '@/services/listaEvaluadoresService';
export default {
    data() {
        return {
            evaluadores: [],
            current_page: 1,
            totalPages: 0
        }
    },
    setup() {
        const evaluadorActual = reactive({
            id_usuario: "",
            nombres: "",
            areaConocimiento: "",
            institucion: "",
            estado: false,
            telefono: "",
            correo: "",
            otraAreaConocimiento: "",
        });

        const obtenerEvaluadorActual = (evaluador) => {
            evaluadorActual.id_usuario = evaluador.id_usuario;
            evaluadorActual.nombres = `${evaluador.nombres} ${evaluador.apellidos}`;
            evaluadorActual.areaConocimiento = evaluador.area_conocimiento;
            evaluadorActual.institucion = evaluador.nombre_institucion;
            evaluadorActual.estado = evaluador.estado;
            evaluadorActual.telefono = evaluador.celular;
            evaluadorActual.correo = evaluador.correo;
            evaluadorActual.otraAreaConocimiento = evaluador.otra_area;

            console.log(evaluadorActual);
        };

        return {
            evaluadorActual,
            obtenerEvaluadorActual
        }
    },
    methods:{
        async fecthEvaluadores() {
            try {
                const respuesta = await obtenerListaEvaluadores(this.current_page);
                this.evaluadores = respuesta.data.evaluators;
                this.totalPages = respuesta.data.total_pages;

            } catch (error) {
                alert("Aún no hay Evaluadores registrados");
            }
        },
        async actualizarEvaluador(id_evaluador,estado) {
            try {
                let nuevoEstado = "inactivo";

                if(estado === "activo"){
                    nuevoEstado = "inactivo";
                }else{
                    nuevoEstado = "activo";
                }

                await actualizarEstadoEvaluador(id_evaluador, nuevoEstado);
                alert("Actualizado con exito");
                this.fecthEvaluadores();
            } catch (error) {
                alert("Error al actualizar el estado del evaluador");
            }
        },
        nextPage() {
            if (this.current_page < this.totalPages) {
                this.current_page++;
                this.fecthEvaluadores();
            }
        },
        prevPage() {
            if (this.current_page > 1) {
                this.current_page--;
                this.fecthEvaluadores();
            }
        },
        paginaSeleted(pagina) {
            this.current_page = pagina;
            this.fecthEvaluadores();
        }
    },
    mounted() {
        this.fecthEvaluadores();
    }
}
</script>

<style scoped>
.section_title h1 {
    display: block;
    color: #1a1a1a;
    font-weight: 500;
    padding-top: 60px;
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

.page-link {
    color: black;
}

#basic-datatables {
    text-align: start;
}

th,
.btn-buscar {
    background: rgb(255, 182, 6) !important;
}
</style>