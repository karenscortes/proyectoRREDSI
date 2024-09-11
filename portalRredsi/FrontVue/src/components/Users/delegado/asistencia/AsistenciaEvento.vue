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
                        <input type="text" v-model="busqueda" id="busqueda" class="form-control" placeholder="Buscar...">
                    </div>
                    <div class="col-4">
                        <button class="btn w-100 font-weight-bold" @click="fetchAsistentes">Buscar</button>
                    </div>
                </div>
            </div>

            <!-- Select de salas disponibles -->
            <div class="col-4 col-sm-2">
                <select class="form-select text-dark" v-model="salaSeleccionada" @change="fetchAsistentes">
                    <option :value="'Sala'" selected>Sala</option>
                    <option v-for="opcion in opciones" :value="opcion" :key="opcion">
                        {{ opcion.numero }} 
                    </option>
                </select>
            </div> 
        </div>

        <!-- Filtros -->
        <div class="row ml-1 mb-2 justify-content-start mt-3">
            <div class="col-auto">
                <a href="#" @click.prevent="fetchAsistentes()" class="mx-1 px-2 border text-white bg-secondary" style="border-radius: 20px;">
                    Todos
                </a>
            </div>
            <div class="col-auto">
                <a href="#" @click.prevent="filtrarParticipantes" class="mx-1 px-2 border text-dark" style="border-radius: 20px;">
                    Participantes
                </a>
            </div>
            <div class="col-auto">
                <a href="#" @click.prevent="filtrarEvaluadores" class="mx-1 px-2 border text-dark" style="border-radius: 20px;">
                    Evaluadores
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
                        <th>Institución</th>
                        <th>CHECK</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(asistente, index) in asistentes" :key="index">
                        <td>{{ asistente.documento }}</td>
                        <td>{{ asistente.nombres }} {{ asistente.apellidos }}</td>
                        <td>{{ asistente.institucion }}</td>
                        <td colspan="1">
                            <input type="checkbox" class="form-check-input ml-4" :checked="asistente.asistencia" @change="toggleActualizarAsistencia(asistente)">
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- paginador  -->
        <div class="mt-5">
            <div aria-label="Page navigation example mb-5">
                <ul class="pagination justify-content-center">
                    <li class="page-item" :class="{ disabled: currentPage === 1 }">
                        <a class="page-link" href="#" @click.prevent="prevPage" style="border-radius: 20px; color: black;">Previous</a>
                    </li>
                    <li class="page-item" v-for="n in totalPages" :key="n" :class="{ active: currentPage === n }">
                        <a class="page-link rounded-circle" href="#" @click.prevent="currentPage = n; fetchAsistentes()">{{ n }}</a>
                    </li>
                    <li class="page-item" :class="{ disabled: currentPage === totalPages }">
                        <a class="page-link" href="#" @click.prevent="nextPage" style="border-radius: 20px; color: black;">Next</a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
import { asistenciaEvento, actualizarAsistencia } from '@/services/delegadoService';

export default {
    data() {
        return {
            asistentes: [], // Lista de asistentes
            busqueda: '', 
            salaSeleccionada: 'Sala', 
            opciones: [], // Lista de salas
            currentPage: 1, 
            totalPages: 0, 
        };
    },
    methods: {
        async fetchAsistentes() {
            try {
                const response = await asistenciaEvento(this.currentPage); 
                const listaAsistentes = response.data.asistentes;

                this.asistentes = listaAsistentes;
                this.totalPages = response.data.totalPages; // Actualizar el número total de páginas (asumiendo que la API lo devuelve)
            } catch (error) {
                alert("Error al obtener asistentes: " + error);
            }
        },

        // Obtener salas disponibles
        // async fetchSalas() {
        //     try {
        //         const response = await obtenerSalas(); 
        //         this.opciones_select = response.data.salas; 
        //     } catch (error) {
        //         alert("Error al obtener las salas: " + error);
        //     }
        // },


    
        async toggleActualizarAsistencia(asistente) {
            try {
                asistente.asistencia = !asistente.asistencia; 
                await actualizarAsistencia(asistente.id_asistente,asistente.id_usuario, asistente.asistencia); 
            } catch (error) {
                alert("Error al actualizar la asistencia: " + error);
            }
        },

        // página siguiente
        nextPage() {
            if (this.currentPage < this.totalPages) {
                this.currentPage++;
                this.fetchAsistentes();
            }
        },

        // página anterior
        prevPage() {
            if (this.currentPage > 1) {
                this.currentPage--;
                this.fetchAsistentes();
            }
        }
    },
    mounted() {
        this.fetchAsistentes(); 
    }
};
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

.page-link {
    color: black;
}

#basic-datatables {
    text-align: start;
}

th, button {
    background: rgb(255, 182, 6) !important;
}
</style>
zz