<template>
    <!-- Título de la sección -->
    <div class="row mb-3 mt-2">
        <div class="col">
            <div class="section_title text-center">
                <h1>Gestionar Asistentes</h1>
            </div>
        </div>
    </div>

    <div class="row justify-content-center">
        <!-- tabla -->
        <div class="table-responsive row d-flex justify-content-center">
            <table class="display table table-striped table-hover text-dark">
                <thead class="text-center">
                    <tr class="cabecero">
                        <th class="thTable" colspan="5">
                        <!-- Buscador -->
                        <div class="row justify-content-start">
                            <div class="col-md-5 col-6">
                            <input
                                type="text"
                                id="busqueda"
                                v-model="busqueda"
                                class="form-control"
                                placeholder="Buscar..."
                                @keyup="keyboardActions"
                            />
                            </div>
                            <div class="col-md-2 col-4">
                            <button class="btn btn-dark w-100 font-weight-bold"  @click="searchAttendee()">
                                Buscar
                            </button>
                            </div>
                        </div>
                        </th>
                        <th class="thTable">
                        <a
                            class="btn-sm font-weight-bold text-dark"
                            @click="showAddModal()"
                            type="button"
                            ><i class="fas fa-plus extra-bold-icon"></i>
                        </a>
                        </th>
                    </tr>
                    <tr>
                        <th>Documento</th>
                        <th>Nombre</th>
                        <th>celular</th>
                        <th>Correo</th>
                        <th>Pago</th>
                        <th>Editar</th>
                    </tr>
                </thead>
                <tbody class="text-center">
                    <AttendeesTableRow
                        v-for="(asistente, index) in attendees"
                        :key="index"
                        :index="index"
                        :infoAsistente="asistente"
                        @open="showEditModal($event)"
                    />
                </tbody>
            </table>
        </div>
        <!-- Paginador -->
        <div v-if="totalPages > 1" class="mt-5">
            <div aria-label="Page navigation example mb-5">
                <ul class="pagination justify-content-center">
                    <li class="page-item m-1">
                        <button @click="prevPage" :disabled="currentPage == 1" class="page-link"
                            style="border-radius: 20px; color: black;">Anterior</button>
                    </li>
                    <li v-for="i in totalPages"  :key="i" class="page-item rounded m-1">
                        <button @click="selectedPage(i)" class="page-link rounded-circle" style="color: black;">{{ i
                            }}</button>
                    </li>
                    <li class="page-item m-1">
                        <button @click="nextPage" :disabled="currentPage == totalPages" class="page-link"
                            style="border-radius: 20px; color: black;">Siguiente</button>
                    </li>
                </ul>
            </div>
        </div>
    </div>
      
    <!-- Modales -->
    <AddAttendeesModal @close="closeAddModal()" v-if="isAddModalOpen"></AddAttendeesModal>
    <EditAttendeeModal v-if="isEditModalOpen" @closeEditModal="closeEditModal()" :infoModal="EditModalInfo"></EditAttendeeModal>
    

</template>
<script>
import { getAttendeesByPage, getAttendeeByDocument } from '@/services/asistenciaService';
import { onMounted, ref, reactive } from "vue";
import { useToastUtils } from '@/utils/toast';
import AddAttendeesModal from './AddAttendeesModal.vue';
import EditAttendeeModal from './EditAttendeeModal.vue';
import AttendeesTableRow from './AttendeesTableRow.vue';



export default {
    components: {
        AttendeesTableRow,
        AddAttendeesModal,
        EditAttendeeModal
    },
    setup() {
        const { showErrorToast,showInfoToast} = useToastUtils();
        const isEditModalOpen = ref(false);
        const isAddModalOpen = ref(false);
        const currentPage = ref(1);
        const totalPages = ref(0);
        const busqueda = ref("");
        const attendees = ref(null);
        const AttendeesArray= reactive([]);

        const EditModalInfo = reactive({
            id_usuario: "",
            documento:"",
            nombres: "",
            apellidos: "",
            celular: "",
            correo: "",
            url_comprobante_pago: "",
        });

        const fetchAttendees = async() => {
            try {

                const response = await getAttendeesByPage(currentPage.value);
                attendees.value = response.data.attendees; 
                totalPages.value = response.data.total_pages;

            } catch (error) {

                showErrorToast(`Error en cargar asistentes`);
            }
        }

        const searchAttendee = async() => {
            try {

                const response = await getAttendeeByDocument(busqueda.value);
                console.log(`logitud coincidencias: ${response.data.attendees.length}`);
                if(response.data.attendees.length > 0){
                    attendees.value = response.data.attendees;
                    totalPages.value = response.data.total_pages;
                }else{
                    showInfoToast('No se encontró ningún asistente con ese documento')
                }  
                
            } catch (error) {
                showErrorToast(`Error en buscar asistente por documento`);
            }
        }

        const keyboardActions = (event) => {
            if (event.key === 'Backspace') {
                if (busqueda.value.length == 0) {
                    fetchAttendees();
                    
                }else{
                    searchAttendee();
                }
            }else{
                searchAttendee();
            }
        }


        //Todo lo del páginador
        const nextPage = () => {
            if (currentPage.value < totalPages.value) {
                currentPage.value++; 
                fetchAttendees(); 
            }
        };

        const prevPage = () => {
            if (currentPage.value > 1) {
                currentPage.value--;
                fetchAttendees(); 
            }
        };

        const selectedPage = (pagina) => {
            currentPage.value = pagina;
            fetchAttendees();
        }

        // Todo lo de los Modales

        const showAddModal = () => {
            isAddModalOpen.value = true;
        };

        const closeAddModal = () => {
            isAddModalOpen.value = false;
            fetchAttendees();
        };

        const showEditModal = (infoAsistente) => {
            EditModalInfo.id_usuario = infoAsistente.id_usuario;
            EditModalInfo.documento = infoAsistente.documento;
            EditModalInfo.nombres = infoAsistente.nombres;
            EditModalInfo.apellidos = infoAsistente.apellidos;
            EditModalInfo.celular = infoAsistente.celular;
            EditModalInfo.correo = infoAsistente.correo;
            EditModalInfo.url_comprobante_pago = infoAsistente.url_comprobante_pago;
            isEditModalOpen.value = true;
        };

        const closeEditModal = () => {
            isEditModalOpen.value = false;
            fetchAttendees();
        };

        onMounted(() => {
            fetchAttendees();
        });

        return {
            currentPage,
            totalPages,
            nextPage,
            prevPage,
            selectedPage,
            busqueda,
            attendees,
            isAddModalOpen,
            isEditModalOpen,
            AttendeesArray,
            EditModalInfo,
            fetchAttendees,
            searchAttendee,
            keyboardActions,
            showAddModal,
            closeAddModal,
            showEditModal,
            closeEditModal

        }
    },
}

</script>

<style scoped>
p a
{
	display: inline;
	position: relative;
	color: #ffb606;
	border-bottom: solid 1px #ffb606;
	-webkit-transition: all 200ms ease;
	-moz-transition: all 200ms ease;
	-ms-transition: all 200ms ease;
	-o-transition: all 200ms ease;
	transition: all 200ms ease;
}
p a:active
{
	position: relative;
	color: #ffb606;
}
p a:hover
{
	color: #FFFFFF;
	background: #ffb606;
}

label{
	font-size: 20px;
	font-weight: bold;
	color: black;
}

.custom-file-upload {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    max-width: 250px;
    padding: 10px;
    margin-top: 10px; /* Para separar la caja de carga del label */
    border: 2px dashed #ccc;
    border-radius: 10px;
    background-color: #f8f9fa;
    text-align: center;
    cursor: pointer;
    transition: border-color 0.3s ease, background-color 0.3s ease;
}

.custom-file-upload:hover {
    border-color: #ffb606;
    background-color: #e9ecef;
}

.custom-file-upload input[type="file"] {
    display: none;
}

.upload-label {
    font-size: 0.9rem;
    color: #333;
    cursor: pointer;
    display: flex;
    align-items: center;
}

.upload-label i {
    font-size: 2rem;
    color: #ffb606;
    margin-right: 10px;
}

</style>