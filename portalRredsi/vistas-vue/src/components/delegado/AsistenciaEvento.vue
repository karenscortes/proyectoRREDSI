<template>

    <div class="container pt-5">
        <div class="row mb-5">
            <div class="col">
                <div class="section_title text-center">
                    <h1>Asistencia</h1>
                </div>
            </div>
        </div>
        <!-- buscador -->
        <div class="row mb-5 justify-content-between">
            <div class="col-8 col-sm-6">
                <div class="row">
                    <div class="col-8">
                        <input type="text" id="busqueda" class="form-control" placeholder="Buscar...">
                    </div>
                    <div class="col-4">
                        <button class="btn w-100 font-weight-bold" style="background: rgb(255, 182, 6)
;">Buscar</button>
                    </div>
                </div>
            </div>
            <div class="col-4 col-sm-2">
                <select type="select" class="form-select text-dark">
                    <option :value="Sala" selected>Sala</option>
                    <option v-for="opcion in opciones_select" :value="opcion" :key="opcion">
                        {{ opcion }}
                    </option>
                </select>
            </div>
        </div>

        <!-- Filtros -->
        <div class="row ml-1 mb-2 justify-content-start mt-3">
            <div class="col-1">
                <a href="#" class="mx-1 px-2 border text-white bg-secondary" style="border-radius: 20px; " disabled>
                todos
                </a>
            </div>
            <div class="col-1">
                <a href="#" class="mx-1 px-2 border text-dark" style="border-radius: 20px; ">
                participantes
                </a>
            </div>
            <div class="col-1">
                <a href="#" class="mx-1 px-2 border text-dark" style="border-radius: 20px; ">
                evaluadores
                </a>
            </div>
        </div>
        <!-- tabla -->
        <div class="table-responsive">
            <table id="basic-datatables" class="display table table-striped table-hover text-dark">
                <thead style="background: rgb(255, 182, 6);">
                    <tr>
                        <th>N° de documento</th>
                        <th>Nombres</th>
                        <th>Institucion</th>
                        <th>CHECK</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1089564222</td>
                        <td>Pepe Rodrigo Sanchez</td>
                        <td>SENA</td>
                        <td colspan="1">
                            <input type="checkbox" class="ml-3 check_asistencia">
                        </td>
                    </tr>
                    <tr>
                        <td>1089564223</td>
                        <td>Maria Lopez Gomez</td>
                        <td>Universidad Nacional</td>
                        <td>
                            <input type="checkbox" class="ml-3 check_asistencia">
                        </td>
                    </tr>
                    <tr>
                        <td>1089564224</td>
                        <td>Juan Carlos Perez</td>
                        <td>Universidad de Antioquia</td>
                        <td>
                            <input type="checkbox" class="ml-3 check_asistencia">
                        </td>
                    </tr>
                    <tr>
                        <td>1089564225</td>
                        <td>Laura Fernandez</td>
                        <td>Universidad Javeriana</td>
                        <td>
                            <input type="checkbox" class="ml-3 check_asistencia">
                        </td>
                    </tr>
                    <tr>
                        <td>1089564226</td>
                        <td>Pedro Martinez</td>
                        <td>Universidad de los Andes</td>
                        <td>
                            <input type="checkbox" class="ml-3 check_asistencia">
                        </td>
                    </tr>
                    <tr>
                        <td>1089564227</td>
                        <td>Angela Ramirez</td>
                        <td>Politécnico Gran Colombiano</td>
                        <td>
                            <input type="checkbox" class="ml-3 check_asistencia">
                        </td>
                    </tr>
                    <tr>
                        <td>1089564228</td>
                        <td>Ricardo Castillo</td>
                        <td>Universidad del Rosario</td>
                        <td>
                            <input type="checkbox" class="ml-3 check_asistencia">
                        </td>
                    </tr>
                    <tr>
                        <td>1089564229</td>
                        <td>Sofia Rodriguez</td>
                        <td>Universidad del Norte</td>
                        <td>
                            <input type="checkbox" class="ml-3 check_asistencia">
                        </td>
                    </tr>
                    <tr>
                        <td>1089564230</td>
                        <td>Felipe Moreno</td>
                        <td>Universidad Industrial de Santander</td>
                        <td>
                            <input type="checkbox" class="ml-3 check_asistencia">
                        </td>
                    </tr>
                    <tr>
                        <td>1089564231</td>
                        <td>Catalina Gutierrez</td>
                        <td>Universidad Pontificia Bolivariana</td>
                        <td>
                            <input type="checkbox" class="ml-3 check_asistencia">
                        </td>
                    </tr>
                    <tr>
                        <td>1089564232</td>
                        <td>Daniela Ortiz</td>
                        <td>Universidad de la Sabana</td>
                        <td>
                            <input type="checkbox" class="ml-3 check_asistencia">
                        </td>
                    </tr>
                    <tr>
                        <td>1089564233</td>
                        <td>Andres Herrera</td>
                        <td>Universidad del Valle</td>
                        <td>
                            <input type="checkbox" class="ml-3 check_asistencia">
                        </td>
                    </tr>
                    <tr>
                        <td>1089564234</td>
                        <td>Paula Castro</td>
                        <td>Universidad EAFIT</td>
                        <td>
                            <input type="checkbox" class="ml-3 check_asistencia">
                        </td>
                    </tr>
                    <tr>
                        <td>1089564235</td>
                        <td>Diego Torres</td>
                        <td>Universidad Externado</td>
                        <td>
                            <input type="checkbox" class="ml-3 check_asistencia">
                        </td>
                    </tr>
                    <tr>
                        <td>1089564236</td>
                        <td>Valentina Suarez</td>
                        <td>Universidad Sergio Arboleda</td>
                        <td>
                            <input type="checkbox" class="ml-3 check_asistencia">
                        </td>
                    </tr>

                </tbody>

            </table>
        </div>
        <div class="mt-5">
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
    </div>
</template>

<script>
export default {
    data() {
        return {
            opciones_select: ["Sala 1", "Sala 2", "Sala 3", "Sala 4"],
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