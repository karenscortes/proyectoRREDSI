<template>
    <div>
        <div class="container pt-5">
            <div class="row mb-5 mt-2">
                <div class="col">
                    <div class="section_title text-center">
                        <h1>Información delegados</h1>
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
                            <button class="btn w-100 font-weight-bold" style="background: rgb(255, 182, 6);">Buscar</button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- tabla -->
            <div class="table-responsive">
                <table id="basic-datatables" class="display table table-striped table-hover text-dark">
                    <thead class="bg-warning">
                        <tr>
                            <th class="bg-warning">Identificación</th>
                            <th class="bg-warning">Delegado</th>
                            <th class="bg-warning">Área de conocimiento</th>
                            <th class="bg-warning">Institución</th>
                            <th class="bg-warning">Estado</th>
                            <th class="bg-warning">Detalle</th>
                            <th class="bg-warning">Historial</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(delegado, index) in delegados" :key="index">
                            <td style="font-size: 16px;">{{ delegado.identificacion }}</td>
                            <td style="font-size: 16px;">{{ delegado.delegado }}</td>
                            <td style="font-size: 16px;">{{ delegado.areaConocimiento }}</td>
                            <td style="font-size: 16px;">{{ delegado.institucion }}</td>
                            <td>
                                <div class="form-check form-switch">
                                    <input class="form-check-input bg-warning border-warning" type="checkbox" role="switch" id="index"
                                        :checked="delegado.estado">

                                    <label class="form-check-label" :for="index"></label>
                                </div>
                            </td>
                            <td>
                                <a @click="obtenerDelegadoActual(delegado)" type="button" data-bs-toggle="modal" data-bs-target="#detalleModal">
                                    <i class="far fa-eye" style="font-size: 25px;"></i>
                                </a>
                            </td>
                            <td>
                                <a @click="obtenerDelegadoActual(delegado)" type="button" data-bs-toggle="modal" data-bs-target="#historialModal">
                                    <i class="far fa-list-alt" style="font-size: 25px;"></i>
                                </a>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div class="mt-2 text-dark">
            <div aria-label="Page navigation example mb-5">
                <ul class="pagination justify-content-center">
                    <li class="page-item disabled m-1">
                        <a class="page-link text-dark" href="#" tabindex="-1" style="border-radius: 20px;">Anterior</a>
                    </li>
                    <li class="page-item rounded m-1 text-dark">
                        <a class="page-link rounded-circle text-dark" href="#">1</a>
                    </li>
                    <li class="page-item m-1">
                        <a class="page-link rounded-circle text-dark" href="#">2</a>
                    </li>
                    <li class="page-item m-1">
                        <a class="page-link rounded-circle text-dark" href="#">3</a>
                    </li>
                    <li class="page-item m-1">
                        <a class="page-link text-dark" href="#" style="border-radius: 20px;">Siguiente</a>
                    </li>
                </ul>
            </div>
        </div>

        
    </div>


    <!-- Modal datos delegados -->
    <div class="modal fade" id="detalleModal" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content border border-dark border-5 rounded-5 text-dark">
                <div class="modal-header">
                    <h3 class="modal-title" id="modalLabel">{{ delegadoActual.delegado }}</h3>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">

                    <div class="row mx-auto justify-content-center">
                        <div class="col-4 text-dark fw-bold">Rol:</div>
                        <div class="col-6 mb-3">
                            <select class="form-select" name="role" id="roleSelect">
                                <option value="" disabled selected>Selecciona un rol</option>
                                <option value="administrador">Administrador</option>
                                <option value="delegado">Delegado</option>
                            </select>
                        </div>
                        <div class="col-5 text-dark fw-bold">Tipo de Documento:</div>
                        <div class="col-5 border mb-3">
                            <span class="text-dark">Cedula</span>
                        </div>
                        <div class="col-5 text-dark fw-bold">Documento:</div>
                        <div class="col-5 border mb-3">
                            <span class="text-dark">{{ delegadoActual.identificacion }}</span>
                        </div>
                        <div class="col-5 text-dark fw-bold">Nombre Completo:</div>
                        <div class="col-5 border mb-3">
                            <span class="text-dark">{{ delegadoActual.delegado }}</span>
                        </div>
                        <div class="col-5 text-dark fw-bold">Área de conocimiento:</div>
                        <div class="col-5 border mb-3">
                            <span class="text-dark">{{ delegadoActual.areaConocimiento }}</span>
                        </div>
                        <div class="col-5 text-dark fw-bold">Institución:</div>
                        <div class="col-5 border mb-3">
                            <span class="text-dark">{{ delegadoActual.institucion }}</span>
                        </div>
                        <div class="col-5 text-dark fw-bold">Teléfono:</div>
                        <div class="col-5 border mb-3">
                            <span class="text-dark">{{ delegadoActual.telefono }}</span>
                        </div>
                        <div class="col-5 text-dark fw-bold">Correo:</div>
                        <div class="col-5 border mb-3">
                            <span class="text-dark">{{ delegadoActual.correo }}</span>
                        </div>
                    </div>

                    <div class="text-center mt-3">
                        <a :href="delegadoActual.urlArchivo" class="btn btn-outline-primary" target="_blank">
                            Ver Títulos
                        </a>
                    </div>

                    <div class="row text-center mt-3">
                        <div class="col-6 mb-2">
                            <button type="button" class="btn btn-secondary w-100" data-bs-dismiss="modal" aria-label="Close">
                                Cerrar
                            </button>
                        </div>
                        <div class="col-6">
                            <button type="button" class="btn btn-warning w-100">
                                Guardar cambios
                            </button>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>


    <!-- Modal historial de acciones -->
    <div class="modal fade" id="historialModal" tabindex="-1" aria-labelledby="historialLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-lg">
            <div class="modal-content border border-dark border-5 rounded-4 text-dark">
                <div class="modal-header bg-warning">
                    <h3 class="modal-title mx-auto" id="historialLabel">Historial acciones {{ delegadoActual.delegado }} </h3>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body p-4">
                    <div class="table-responsive">
                        <table class="table table-bordered">
                            <thead class="bg-warning">
                                <tr>
                                    <th>Tipo de Acción</th>
                                    <th>Módulo</th>
                                    <th>Descripción</th>
                                    <th>Fecha</th>
                                    <th>Hora</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="(actividad, index) in historialActual.actividades" :key="index">
                                    <td>{{ actividad.tipoAccion }}</td>
                                    <td>{{ actividad.modulo }}</td>
                                    <td>{{ actividad.detalle }}</td>
                                    <td>{{ actividad.fecha }}</td>
                                    <td>{{ actividad.hora }}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>


</template>

<script>
import { reactive } from 'vue';

export default {
    setup() {
        const delegados = [
            {
                identificacion: "1012356",
                delegado: "Juan Pérez",
                areaConocimiento: "Ciencias Naturales",
                institucion: "Universidad Nacional",
                estado: true,
                telefono: "8432848",
                correo: "Juan.perez@gmail.com",
                urlArchivo: "ruta/al/archivo.pdf"
            },
            {
                identificacion: "1012357",
                delegado: "Ana Gómez",
                areaConocimiento: "Biología",
                institucion: "Universidad de Antioquia",
                estado: true,
                telefono: "66435",
                correo: "ana.gomez@gmail.com",
                urlArchivo: "ruta/al/archivo.pdf"
            },
            {
                identificacion: "1012358",
                delegado: "Carlos Ruiz",
                areaConocimiento: "Química",
                institucion: "Universidad del Valle",
                estado: false,
                telefono: "567423424",
                correo: "carlos.ruiz@gmail.com",
                urlArchivo: "ruta/al/archivo.pdf"
            },
            {
                identificacion: "1012359",
                delegado: "Lucía Fernández",
                areaConocimiento: "Historia",
                institucion: "Universidad de los Andes",
                estado: true,
                telefono: "67577",
                correo: "lucia.fernandez@gmail.com",
                urlArchivo: "ruta/al/archivo.pdf"
            },
            {
                identificacion: "1012360",
                delegado: "Andrés Bustamante",
                areaConocimiento: "Geografía",
                institucion: "Pontificia Universidad Javeriana",
                estado: true,
                telefono: "676576",
                correo: "andres.bustamante@gmail.com",
                urlArchivo: "ruta/al/archivo.pdf"
            },
            {
                identificacion: "10145360",
                delegado: "Diego Parra",
                areaConocimiento: "Geografía",
                institucion: "Pontificia Universidad Javeriana",
                estado: true,
                telefono: "3205856846",
                correo: "diego.parra@gmail.com",
                urlArchivo: "ruta/al/archivo.pdf"
            }
        ];

        const historialActividades = [
            {
                tipoAccion: "Actualizar",
                modulo: "Editar perfil",
                detalle: "Actualizacion de documentos de Ciencias Naturales",
                fecha: "2024-08-30",
                hora: "12:45 PM"
            },
            {
                tipoAccion: "Evaluar",
                modulo: "Proyecto Biología",
                detalle: "Evaluación de proyecto de Biología",
                fecha: "2024-08-29",
                hora: "09:30 AM"
            },
            {
                tipoAccion: "Revisar",
                modulo: "Revisión Química",
                detalle: "Revisión de documentos de Química",
                fecha: "2024-08-28",
                hora: "11:15 AM"
            },
            {
                tipoAccion: "Actualizar",
                modulo: "Historia Antigua",
                detalle: "Actualización de datos en Historia",
                fecha: "2024-08-27",
                hora: "02:00 PM"
            },
            {
                tipoAccion: "Evaluar",
                modulo: "Geografía",
                detalle: "Evaluación de documentos de Geografía",
                fecha: "2024-08-26",
                hora: "03:45 PM"
            },
            {
                tipoAccion: "Revisar",
                modulo: "Geografía",
                detalle: "Revisión de mapas en Geografía",
                fecha: "2024-08-25",
                hora: "10:30 AM"
            }
        ];

        const delegadoActual = reactive({
            identificacion: "",
            delegado: "",
            areaConocimiento: "",
            institucion: "",
            estado: false,
            telefono: "",
            correo: "",
            urlArchivo: ""
        });

        const historialActual = reactive({
            actividades: [] 
        });

        const obtenerDelegadoActual = (delegado) => {
            delegadoActual.identificacion = delegado.identificacion;
            delegadoActual.delegado = delegado.delegado;
            delegadoActual.areaConocimiento = delegado.areaConocimiento;
            delegadoActual.institucion = delegado.institucion;
            delegadoActual.estado = delegado.estado;
            delegadoActual.telefono = delegado.telefono;
            delegadoActual.correo = delegado.correo;
            delegadoActual.urlArchivo = delegado.urlArchivo;

            console.log(delegadoActual);

            // Filtrar historial para el delegado seleccionado
            historialActual.actividades = historialActividades.filter(actividad => 
                actividad.modulo.includes(delegado.areaConocimiento)
            );
        };

        return {
            delegadoActual,
            obtenerDelegadoActual,
            historialActual,
            delegados, // Para usar en el template si es necesario
            historialActividades // Para usar en el template si es necesario
        }
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

.page-link {
    color: black;
}
</style>


