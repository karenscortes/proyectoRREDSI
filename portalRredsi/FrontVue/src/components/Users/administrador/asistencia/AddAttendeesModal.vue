<template>
    <div class="modal fade show" id="addAttendees" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div
        class="modal-content border border-dark border-5 rounded-5 text-dark"
      >
        <div class="text-center">
          <button type="button" class="close mr-3 mt-1 fs-2" @click="closeModal()">
            <span aria-hidden="true">&times;</span>
          </button>
          <h3 class="modal-title mt-5" id="modalLabel">
            Agregar Lista de Asistentes
          </h3>
        </div>
        <div class="modal-body mt-3 text-center">
            <form @submit.prevent="bulkUpload()">
                <div class="custom-file-upload mx-auto">
                    <label for="comprobante_pago" class="upload-label">
                        <input type="file" id="comprobante_pago" name="comprobante_pago" class="d-none d-print-block" @change="onFileChange"/>
                        <i class="fas fa-cloud-upload-alt"></i>
                        Selecciona un archivo
                    </label>
                </div> 
                <p>Archivo Excel con los campos requeridos. <a href="#">Descargar Formato</a></p>
                <div class="d-flex justify-content-center ">
                    <button class="btn boton pl-5 pr-5 mx-auto" type="submit">Agregar</button>
                </div>
            </form>    
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { ref } from "vue";
import { uploadFileData } from "@/services/asistenciaService";
export default {
    emits: ["close"],
    setup(props, { emit }) {
        const file = ref(null);

        const onFileChange = (event) => {
            file.value = event.target.files[0];
        };

        const bulkUpload = async () => {
            try {
                if (file.value) {
                    await uploadFileData(file.value); // Llama al servicio para subir los datos del excel
                    alert('Archivo subido exitosamente');
                }
            } catch (error) {
                console.error('Error al subir el archivo:', error);
            }
        };

        
        const closeModal = () => {
            emit("close");
        };


        return {
            onFileChange,
            bulkUpload,
            closeModal
        }
    },
}

</script>

<style scoped>
#addAttendees {
  display: block;
}

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
	font-size: 15px;
	font-weight: bold;
	color: black;
}

.custom-file-upload {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    max-width: 400px;
    padding: 20px;
    margin-top: 10px; 
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
