<template>
    <div class="container mt-5">
        <div class="row mb-3">
            <div class="col">
                <div class="section_title text-center">
                    <h1>Salas Asignadas</h1>
                </div>
            </div>
        </div>

        <!-- Buscador -->
        <div class="row justify-content-end align-items-center mr-4">
            <div class="col-8 col-sm-4">
                <input v-model="valorBusqueda" type="text" id="busqueda" class="form-control text-dark w-100" 
                       style="height: 100%; padding: 0.5rem;" placeholder="Ingresa numero de sala">
            </div>
            <div class="col-4 col-sm-3">
                <button class="btn w-100 font-weight-bold" 
                        style="background: rgb(255, 182, 6); color: #000000" 
                        @click="buscarSala">Buscar</button>
            </div>
        </div>

        <!-- Cards Salas -->
        <div class="teachers my-4">
            <div class="row">
                <CardSalas v-for="(sala, index) in salasFiltradas" :key="index" :sala="sala"/>
            </div>
        </div>
    </div>
</template>

<script>
import CardSalas from "./CardSalas.vue";
import { obtenerSalas } from '@/services/delegadoService';

export default {
    name: "ListaSalasDelegado",
    components: {
        CardSalas,
    },
    data() {
        return {
            salas: [], // Almacena todas las salas originales
            salasFiltradas: [], // Almacena las salas filtradas
            valorBusqueda: ""
        }
    },
    methods: {
        async listarSalas() {
            try {
                const response = await obtenerSalas();
                this.salas = response.data.salas;
                this.salasFiltradas = [...this.salas]; // Inicialmente muestra todas las salas
            } catch (error) {
                alert("Error al consultar salas");
            }
        },
        buscarSala() {
            if (this.valorBusqueda.trim() != "") {
                // Buscar salas espeficicas 
                this.salasFiltradas = this.salas.filter(sala => 
                    sala.numero_sala.toLowerCase().includes(this.valorBusqueda.toLowerCase()) ||
                    sala.nombre_area_conocimiento.toLowerCase().includes(this.valorBusqueda.toLowerCase()) ||
                    sala.nombres_delegado.toLowerCase().includes(this.valorBusqueda.toLowerCase())
                );
            } else {
                this.salasFiltradas = [...this.salas]; // Si no hay búsqueda, muestra todas las salas
            }
        }
    },
    mounted() {
        this.listarSalas();
    }
}
</script>

<style scoped>
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
    transform: translateX(-50%);
    width: 55px;
    height: 4px;
    content: '';
    background: #ffb606;
}

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
