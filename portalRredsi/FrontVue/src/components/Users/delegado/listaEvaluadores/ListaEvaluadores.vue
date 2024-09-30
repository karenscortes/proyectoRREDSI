<template>
    <div>
        <div class="container">
            <div class="row mb-5">
                <div class="col">
                    <div class="section_title text-center">
                        <h1>Evaluadores Registrados</h1>
                    </div>
                </div>
            </div>
            <!-- buscador -->
            <div class="row mb-4 justify-content-end">
                <div class="col-10 col-sm-6 justify-content-end">
                    <div class="row justify-content-end">
                        <div class="col-7">
                            <input v-model="documento_evaluador" type="text" id="busqueda" class="form-control text-dark" placeholder="Ingrese documento del evaluador">
                        </div>
                        <div class="col-5">
                            <button class="btn btn-buscar w-100 font-weight-bold" @click="buscarEvaluador">Buscar</button>
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
                                    data-bs-target="#evaluatorInformation">
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
        <PaginatorBody :totalPages="totalPages" @page-changed="cambiarPagina" v-if="totalPages > 1" />

        <!-- Modal datos -->
        <div class="modal fade" id="evaluatorInformation" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content border border-dark border-5 rounded-5 text-dark">
                    <div class="modal-header text-center">
                        <h3 class="modal-title mt-4 w-100" id="modalLabel">{{ evaluadorActual.nombres }}</h3>
                        <button type="button" class="btn-close mr-3 mt-3" data-bs-dismiss="modal"
                            aria-label="Close"></button>
                    </div>
                    <div class="modal-body mt-3">
                        <div class="row justify-content-center text-start">
                            <div class="col-5 text-dark font-weight-bold px-3">Nombre Completo:</div>
                            <div class="col-5 mb-3 px-3">
                                <span class="text-dark">{{ evaluadorActual.nombres }}</span>
                            </div>
                            <div class="col-5 text-dark font-weight-bold px-3">Institución:</div>
                            <div class="col-5 mb-3 px-3">
                                <span class="text-dark">{{ evaluadorActual.institucion }}</span>
                            </div>
                            <div class="col-5 text-dark font-weight-bold px-3">Teléfono:</div>
                            <div class="col-5 mb-3 px-3">
                                <span class="text-dark">{{ evaluadorActual.telefono }}</span>
                            </div>
                            <div class="col-5 text-dark font-weight-bold px-3">Correo:</div>
                            <div class="col-5 mb-3 px-3">
                                <span class="text-dark">{{ evaluadorActual.correo }}</span>
                            </div>
                            <div class="col-5 text-dark font-weight-bold px-3">Área de conocimiento:</div>
                            <div class="col-5 mb-3 px-3">
                                <span class="text-dark">{{ evaluadorActual.areaConocimiento }}</span>
                            </div>
                            <div class="col-5 text-dark font-weight-bold px-3">Otra área de conocimiento:</div>
                            <div class="col-5 mb-3 px-3">
                                <span class="text-dark">{{ evaluadorActual.otraAreaConocimiento }}</span>
                            </div>
                            <div class="text-center mt-3">
                                <button @click="modalTitulos" class="btn text-dark fw-semibold" target="_blank">
                                    Ver Títulos
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Modal titulos -->
        <div class="modal fade" id="modal_titulos" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                    <div class="row text-center justify-content-end mt-2">
                        <div class="col-2">
                            <button type="button" class="btn-close justify-contet-end" data-bs-dismiss="modal"
                                aria-label="Close"></button>
                        </div>
                        <div class="col-12">
                            <h1 class="modal-title fs-5 text-dark" id="exampleModalLabel">Programas Académicos<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#00000"><path d="M480-120 200-272v-240L40-600l440-240 440 240v320h-80v-276l-80 44v240L480-120Zm0-332 274-148-274-148-274 148 274 148Zm0 241 200-108v-151L480-360 280-470v151l200 108Zm0-241Zm0 90Zm0 0Z"/></svg></h1>
                        </div>
                    </div>
                    <div class="modal-body">
                        <div class="list-group">
                            <a v-for="(certificate,index) in certificates"  :key="index" :href="certificate.url_titulo" class="list-group-item list-group-item-action" target="_blank">{{certificate.nivel}}</a>
                        </div>
                    </div>
                    <div class="row justify-content-center mb-2">
                        <button type="button" class="btn btn-dark fw-bold col-4 text-center" data-bs-dismiss="modal">Cerrar</button>
                    </div>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import { reactive } from 'vue';
import { obtenerListaEvaluadores, actualizarEstadoEvaluador } from '@/services/listaEvaluadoresService';
import { obtenerIdEvaluador } from '@/services/delegadoService';
import PaginatorBody from '../../../UI/PaginatorBody.vue';
import { useToastUtils } from '@/utils/toast';
import { getCertificatesById } from '@/services/postulacionService';

export default {
    data() {
        return {
            evaluadores: [],
            totalPages: 0,
            current_page: 1,
            documento_evaluador:"",
            certificates : []
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
        const { showSuccessToast, showErrorToast, showWarningToast, showDefaultToast, showInfoToast } = useToastUtils();

        const obtenerEvaluadorActual = (evaluador) => {
            evaluadorActual.id_usuario = evaluador.id_usuario;
            evaluadorActual.nombres = `${evaluador.nombres} ${evaluador.apellidos}`;
            evaluadorActual.areaConocimiento = evaluador.area_conocimiento;
            evaluadorActual.institucion = evaluador.nombre_institucion;
            evaluadorActual.estado = evaluador.estado;
            evaluadorActual.telefono = evaluador.celular;
            evaluadorActual.correo = evaluador.correo;
            evaluadorActual.otraAreaConocimiento = evaluador.otra_area;

        };

        return {
            evaluadorActual,
            obtenerEvaluadorActual,
            showSuccessToast,
            showErrorToast,
            showInfoToast,
            showWarningToast
        }
    },
    components:{
        PaginatorBody
    },
    methods:{
        async fecthEvaluadores(pagina_actual) {
            try {
                const respuesta = await obtenerListaEvaluadores(pagina_actual);
                this.evaluadores = respuesta.data.evaluators;
                this.totalPages = respuesta.data.total_pages;
            } catch (error) {
                // Configuración de la alerta 
                this.showInfoToast("Aún no hay Evaluadores registrados");
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
                
                // Configuración de la alerta 
                this.showSuccessToast("El estado del evaluador se ha cambiado con exito");

                this.fecthEvaluadores(this.current_page);
            } catch (error) {
                // Configuración de la alerta
                showErrorToast("El estado del evaluador no se ha podido cambiar");
            }
        },
        async buscarEvaluador(){
            try {
                if(this.documento_evaluador.trim() != ""){
                    const evaluador = await obtenerIdEvaluador(this.documento_evaluador);
                    this.obtenerEvaluadorActual(evaluador.data);
                    this.evaluadores = [evaluador.data];

                    console.log(this.evaluadores)
                    $('#delegateInformation').modal('show');
                }
                if(this.documento_evaluador.trim() == ""){
                    this.fecthEvaluadores();
                }
                
            } catch (error) {
                this.showWarningToast("El evaluador no se ha encontrado");
                this.fecthEvaluadores();
            }
        },
        cambiarPagina(pagina){
            this.current_page = pagina;
            this.fecthEvaluadores(pagina);
        },
        async modalTitulos(){
            try {
                const response = await getCertificatesById(this.evaluadorActual.id_usuario);
                console.log(response.data);
                this.certificates = response.data;
                $('#modal_titulos').modal('show');
            } catch (error) {
                this.showInfoToast("No se registraron títulos académicos");
            }
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

.btn-close {
    width: 8px;
    height: 8px;
}
</style>