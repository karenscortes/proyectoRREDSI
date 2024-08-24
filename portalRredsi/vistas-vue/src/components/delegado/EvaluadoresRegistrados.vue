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
                            <button class="btn w-100 font-weight-bold" style="background: rgb(255, 182, 6)
;">Buscar</button>
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
                            <th>Identificación</th>
                            <th>Evaluador</th>
                            <th>Area de conocimiento</th>
                            <th>Institucion</th>
                            <th>Estado</th>
                            <th>Detalle</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>1000000001</td>
                            <td>Pepe Rodrigo Sanchez</td>
                            <td>Ciencias naturales</td>
                            <td>SENA</td>
                            <td>
                                <div class="custom-control custom-switch d-flex justify-content-center">
                                    <input type="checkbox" class="custom-control-input" id="customSwitch1">
                                    <label class="custom-control-label" for="customSwitch1"></label>
                                </div>
                            </td>
                            <td>
                                <a href="#" class="btn-sm font-weight-bold text-dark" type="button"
                                    data-bs-toggle="modal" data-bs-target="#delegateInformation">
                                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960"
                                        width="24px" fill="#00000">
                                        <path
                                            d="M560-440h200v-80H560v80Zm0-120h200v-80H560v80ZM200-320h320v-22q0-45-44-71.5T360-440q-72 0-116 26.5T200-342v22Zm160-160q33 0 56.5-23.5T440-560q0-33-23.5-56.5T360-640q-33 0-56.5 23.5T280-560q0 33 23.5 56.5T360-480ZM160-160q-33 0-56.5-23.5T80-240v-480q0-33 23.5-56.5T160-800h640q33 0 56.5 23.5T880-720v480q0 33-23.5 56.5T800-160H160Zm0-80h640v-480H160v480Zm0 0v-480 480Z" />
                                    </svg>
                                </a>
                            </td>
                        </tr>
                        <tr v-for="(evaluador, index) in evaluadores" :key="index">
                            <td>{{ evaluador.identificacion }}</td>
                            <td>{{ evaluador.nombre }}</td>
                            <td>{{ evaluador.areaConocimiento }}</td>
                            <td>{{ evaluador.institucion }}</td>
                            <td>
                                <div class="custom-control custom-switch d-flex justify-content-center">
                                    <input type="checkbox" class="custom-control-input" :id="index"
                                        :checked="evaluador.estado">
                                    <label class="custom-control-label" :for="index"></label>
                                </div>
                            </td>
                            <td>
                                <a href="#" @click="obtenerEvaluadorActual(evaluador)" class="btn-sm font-weight-bold text-dark" type="button"
                                    data-bs-toggle="modal" data-bs-target="#delegateInformation">
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
        <div class="mt-2">
            <div aria-label="Page navigation example mb-5">
                <ul class="pagination justify-content-center">
                    <li class="page-item disabled m-1">
                        <a class="page-link" href="#" tabindex="-1"
                            style="border-radius: 20px; color: black;">Previous</a>
                    </li>
                    <li class="page-item rounded m-1">
                        <a class="page-link rounded-circle" href="#" style="color: black;">1</a>
                    </li>
                    <li class="page-item m-1">
                        <a class="page-link rounded-circle" href="#" style="color: black;">2</a>
                    </li>
                    <li class="page-item m-1">
                        <a class="page-link rounded-circle" href="#" style="color: black;">3</a>
                    </li>
                    <li class="page-item m-1">
                        <a class="page-link" href="#" style="border-radius: 20px; color: black;">Next</a>
                    </li>
                </ul>
            </div>
        </div>

        <!-- Modal datos delegados -->
        <div class="modal fade" id="delegateInformation" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content border border-dark border-5 rounded-5 text-dark">
                    <div class="modal-header text-center">
                        <h3 class="modal-title mt-5 w-100" id="modalLabel">{{ console.log(evaluadorActual) }}</h3>
                        <button type="button" class="btn-close mr-3 mt-3" data-bs-dismiss="modal"
                            aria-label="Close"></button>
                    </div>
                    <div class="modal-body mt-3">
                        <div class="row mx-auto justify-content-center">
                            <div class="col-5 text-dark font-weight-bold px-3">Tipo de Documento:</div>
                            <div class="col-5 border mb-3 px-3">
                                <span class="text-dark">Cedula</span>
                            </div>
                            <div class="col-5 text-dark font-weight-bold px-3">Documento:</div>
                            <div class="col-5 border mb-3 px-3">
                                <span class="text-dark">2102156348</span>
                            </div>
                            <div class="col-5 text-dark font-weight-bold px-3">Nombre Completo:</div>
                            <div class="col-5 border mb-3 px-3">
                                <span class="text-dark">Maria Luisa</span>
                            </div>
                            <div class="col-5 text-dark font-weight-bold px-3">Área de conocimiento:</div>
                            <div class="col-5 border mb-3 px-3">
                                <span class="text-dark">Sistemas</span>
                            </div>
                            <div class="col-5 text-dark font-weight-bold px-3">Institución:</div>
                            <div class="col-5 border mb-3 px-3">
                                <span class="text-dark">SENA</span>
                            </div>
                            <div class="col-5 text-dark font-weight-bold px-3">Teléfono:</div>
                            <div class="col-5 border mb-3 px-3">
                                <span class="text-dark">3204562023</span>
                            </div>
                            <div class="col-5 text-dark font-weight-bold px-3">Correo:</div>
                            <div class="col-5 border mb-3 px-3">
                                <span class="text-dark">maria60@gmail.com</span>
                            </div>
                            <div class="text-center mt-3">
                                <a href="../delegado/pruebas_documentos/constancia_NotasAprendiz.pdf"
                                    class="btn btn-outline-primary" target="_blank">
                                    Ver Títulos
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>



    </div>

</template>

<script>
export default {
    data() {
        return {
            evaluadores: [
                {
                    identificacion: "24644221",
                    nombre: "Sebastian usma",
                    areaConocimiento: "Tecnologia",
                    institucion: "SENA",
                    estado: false
                },
                {
                    identificacion: "246415441",
                    nombre: "Luisa Lopez Agudelo",
                    areaConocimiento: "Ciencias naturales",
                    institucion: "SENA",
                    estado: true
                },
                {
                    identificacion: "104644221",
                    nombre: "Miguel Alzate",
                    areaConocimiento: "Quimica",
                    institucion: "SENA",
                    estado: false
                }
            ]
        }
    },
    methods:{
        obtenerEvaluadorActual(evaluador){
            const personaActual = evaluador;
            console.log(personaActual);
            return { personaActual }
        }
    }
}
</script>