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
                        <button class="btn w-100 font-weight-bold">Buscar</button>
                    </div>
                </div>
            </div>
            <!-- Select de salas disponibles -->
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
            <div class="col-auto">
                <a href="#" class="mx-1 px-2 border text-white bg-secondary" style="border-radius: 20px;" disabled>
                    todos
                </a>
            </div>
            <div class="col-auto">
                <a href="#" class="mx-1 px-2 border text-dark" style="border-radius: 20px;">
                    participantes
                </a>
            </div>
            <div class="col-auto">
                <a href="#" class="mx-1 px-2 border text-dark" style="border-radius: 20px;">
                    evaluadores
                </a>
            </div>
        </div>

        <!-- tabla -->
        <div class="table-responsive">
            <table id="basic-datatables" class="display table table-striped table-hover text-dark">
                <thead>
                    <tr>
                        <th>N° de documento</th>
                        <th>Nombres</th>
                        <th>Institucion</th>
                        <th>CHECK</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(asistente, index) in asistentes" :key="index">
                        <td>{{ asistente.documento }}</td>
                        <td>{{ asistente.nombres }} {{ asistente.apellidos }}</td>
                        <td>{{ asistente.institucion }}</td>
                        <td colspan="1">
                            <input type="checkbox" class="form-check-input ml-4" :checked="asistente.asistencia">
                        </td>

                    </tr>
                </tbody>
            </table>
        </div>

        <!-- paginador  -->
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
import {asistenciaEvento} from '../../../../services/delegadoService';

export default{
    data() {
        return {
            asistentes: []
        }
    },
    methods: {
        async fetchAsistentes() {
            try {
                const responde = await asistenciaEvento();
                this.asistentes = responde.data.asistentes;
                console.log(this.asistentes);
            } catch (error) {
                alert("Error al obtener asistentes: ", error);
            }
        }
    },
    mounted() {
        this.fetchAsistentes();
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

#basic-datatables{
    text-align: start;
}

th, button{
    background: rgb(255, 182, 6) !important;
}
</style>