<template>
    <div class="container mt-5">
        <div class="row mb-3">
            <div class="col">
                <div class="section_title text-center">
                    <h1>Salas Asignadas</h1>
                </div>
            </div>
        </div>

        <!--Buscador-->
        <div class="row justify-content-end align-items-center">
            <div class="col-8 col-sm-4">
                <input type="text" id="busqueda" class="form-control  w-100" style="height: 100%; padding: 0.5rem;"
                    placeholder="Buscar">
            </div>
            <div class="col-4 col-sm-2">
                <button class="btn w-90 font-weight-bold"
                    style="background-color: #000000; color: #ffffff">Buscar</button>
            </div>
        </div>

        <!--Cards Salas-->
        <div class="teachers my-4 ">
            <div class="row">
                <CardSalas v-for="(sala, index) in salas" :key="index" :numeroSala="sala.numero_sala"
                    :nombreDelegado="sala.nombreDelegado" :areaConocimiento="sala.areaConocimiento" />   
            </div>
        </div>
    </div>

    <!-- Paginador -->
    <div class="mt-2">
        <div aria-label="Page navigation example mb-5">
            <ul class="pagination justify-content-center">
                <li class="page-item  m-1">
                    <a class="page-link" href="#" tabindex="-1" style="border-radius: 20px; color: black;">Previous</a>
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
</template>

<script>
import CardSalas from "./CardSalas.vue";
import { obtenerSalas} from '@/services/delegadoService';
export default {
    components: {
        CardSalas,
    },
    data() {
        return {
            salas: []
        }
    },
    methods:{
        async listarSalas(){
            try {
                const response = await obtenerSalas();
                this.salas = response.data.salas;
                console.log(this.salas)
            } catch (error) {
                alert("Error al consultar salas")
            }
        },
        async obtenerDatosDelegado(){
            
        }
    },
    mounted(){
        this.listarSalas()
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

/* Estilos para el paginador */
.pagination .page-item .page-link {
    font-size: 18px;
    padding: 10px 20px;
    border-radius: 50px;
}

.pagination .page-item .page-link:hover {
    background-color: rgb(255, 182, 6);
    color: #ffffff;
}
</style>