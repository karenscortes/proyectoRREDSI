<template>
    <div class="container mt-5">

        <component v-if="habilitarComponente" :is="selectedComponent" :sala="SalaSeleccionada"
            @volver="volverListaSalas" />
        <div v-else>
            <div class="row mb-3">
                <div class="col">
                    <div class="section_title text-center">
                        <h1>Salas Registradas</h1>
                    </div>
                </div>
            </div>

            <!-- Cards Salas -->
            <div class="my-4">

                <!-- Buscador -->
                <div class="row align-items-center justify-content-center mb-4">
                    <div class="col-4 col-sm-3">
                        <button v-if="salaAsignada" class="boton_gestion_sala btn btn-dark text-white"
                            @click="changeComponent('GestionSala', miSala)">Mi sala <svg
                                xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                                fill="#FFFFFF">
                                <path
                                    d="M480-240q-97 0-166-66t-74-162l84 25q13 54 56 88.5T480-320q66 0 113-47t47-113q0-57-34.5-100T517-636l-25-84q96 5 162 74t66 166q0 100-70 170t-170 70Zm0 160q-83 0-156-31.5T197-197q-54-54-85.5-127T80-480v-18q0-9 2-18l78 24v12q0 134 93 227t227 93q134 0 227-93t93-227q0-134-93-227t-227-93h-12l-24-78q9-2 18-2h18q83 0 156 31.5T763-763q54 54 85.5 127T880-480q0 83-31.5 156T763-197q-54 54-127 85.5T480-80Zm-59-380L250-631l-50 151L80-880l400 120-151 50 171 171-79 79Z" />
                            </svg></button>
                        <p v-else>Sin sala asignada</p>
                    </div>
                    <div class="col-8 col-sm-8">
                        <div class="row justify-content-end">
                            <div class="col-8 col-sm-6">
                                <input v-model="valorBusqueda" type="text" id="busqueda"
                                    class="form-control text-dark w-100" style="height: 100%; padding: 0.5rem;"
                                    placeholder="Ingresa nombre de la sala">
                            </div>
                            <div class="col-4 col-sm-4">
                                <button class="btn w-100 font-weight-bold"
                                    style="background: rgb(255, 182, 6); color: #000000"
                                    @click="buscarSalaEspecifica">Buscar</button>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="row">
                    <CardSalas v-for="(sala, index) in salas" :key="index" :sala="sala"
                        @component-selected="changeComponent" />
                </div>

                <PaginatorBody :totalPages="totalPages" @page-changed="cambiarPagina" v-if="totalPages > 1" />
            </div>
        </div>
    </div>
</template>

<script>
import CardSalas from "./CardSalas.vue";
import { obtenerSalas } from '@/services/delegadoService';
import { obtenerDatosSalaAsignada, buscarSala} from '@/services/salasDelegadoService';
import { useAuthStore } from '@/store';
import GestionSala from "./GestionSala.vue";
import DetalleSala from "./DetalleSala.vue";
import PaginatorBody from "../../../UI/PaginatorBody.vue";
import { obtenerProgramacionFases } from '@/services/evaluadorService';
import { useToastUtils } from '@/utils/toast';

export default {
    components: {
        CardSalas,
        GestionSala,
        DetalleSala,
        PaginatorBody
    },
    data() {
        const { showSuccessToast, showErrorToast, showWarningToast, showInfoToast } = useToastUtils();
        return {
            salas: [], // Almacena todas las salas originales
            salasFiltradas: [], // Almacena las salas filtradas
            valorBusqueda: "",
            selectedComponent: '',
            habilitarComponente: false,
            salaDetalle: [],
            salaAsignada: false,
            miSala: {},
            SalaSeleccionada: {},
            totalPages: 0,
            fechasEvento: {
                fecha_inicio:"",
                fecha_fin:"",
            },
            showErrorToast,
            showInfoToast,
            showWarningToast
        }
    },
    setup() {
        const authStore = useAuthStore();

        const user = authStore.user;

        return {
            user,
        };
    },
    methods: {
        async listarSalas(pagina) {
            try {
                const response = await obtenerSalas(pagina);
                this.salas = response.data.salas;
                this.totalPages = response.data.total_pages;
                this.salasFiltradas = [...this.salas];

                // Obtengo las fechas del evento y se las agrego al detalle de las salas
                await this.obtenerFechasEvento();
                this.salas.forEach(sala =>{
                    sala.fechasEvento = "";
                    sala.fechasEvento = this.fechasEvento;
                });
            } catch (error) {
                this.showErrorToast("Error al consultar salas");
            }
        },
        async buscarSalaEspecifica() {
            try {
                if (this.valorBusqueda.trim() != "") {
                // Buscar salas espeficicas 
                const responseBuscarSala = await buscarSala(this.valorBusqueda);
                this.salas = responseBuscarSala.data.salas;
                
                this.valorBusqueda = "";
                this.totalPages = 0;
                
                // Obtengo las fechas del evento y se las agrego al detalle de las salas
                await this.obtenerFechasEvento();
                this.salas.forEach(sala =>{
                    sala.fechasEvento = "";
                    sala.fechasEvento = this.fechasEvento;
                });
            } else {
                await this.listarSalas();
                this.showInfoToast("Por favor, ingresa un valor de búsqueda");
            }
            } catch (error) {
                this.showInfoToast("No se ha podido encontrar la sala");
                await this.listarSalas();
            }
            this.valorBusqueda = "";
        },
        changeComponent(componentName, p_sala_seleccionada) {
            this.selectedComponent = componentName;
            this.habilitarComponente = true;
            this.SalaSeleccionada = p_sala_seleccionada;
        },
        async volverListaSalas() {
            await this.listarSalas();
            this.habilitarComponente = false;
        },
        async obtenerSalaAsignada(id_delegado) {
            try {
                const datosSalaAsignada = await obtenerDatosSalaAsignada(id_delegado);
                this.miSala = datosSalaAsignada.data;
                this.salaAsignada = true;
            } catch (error) {
                this.salaAsignada = false;
            }

        },
        async obtenerFechasEvento() {
            try {
                const response = await obtenerProgramacionFases("presencial");
                for (let i = 0; i < response.data.length; i++) {
                    if(response.data[i].nombre_fase == "Evento"){
                        this.fechasEvento.fecha_inicio = response.data[i].fecha_inicio;
                        this.fechasEvento.fecha_fin = response.data[i].fecha_fin;
                        this.miSala.fechasEvento = this.fechasEvento;
                        this.SalaSeleccionada.fechasEvento = this.fechasEvento;
                        break;
                    }
                }
            } catch (error) {
                console.log(error);
                this.showErrorToast("Error al obtener las fases de la convocatoria");
            }
        },
        cambiarPagina(pagina) {
            this.listarSalas(pagina);
        }

    },
    mounted() {
        this.obtenerSalaAsignada(this.user.id_usuario);
        this.listarSalas();
    }
}
</script>

<style scoped>
.boton_gestion_sala {
    background: black !important;
    color: white !important;
}

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
