<template>
    <!-- Título de la sección -->
    <div class="row mb-3 mt-2">
        <div class="col">
            <div class="section_title text-center">
                <h1>Gestionar Asistentes</h1>
            </div>
        </div>
    </div>

    <div class="row mt-5 justify-content-center">
        <div class="col-6 text-center">
            <form @submit.prevent="bulkUpload()">
                <label for="comprobante_pago" class="form-label d-flex justify-content-center">
                    Lista de Asistentes: 
                </label>
                <p>Archivo Excel con los campos requeridos. <a href="#">Descargar Formato</a></p>
                <div class="custom-file-upload mx-auto">
                    <label for="comprobante_pago" class="upload-label">
                        <input type="file" id="comprobante_pago" name="comprobante_pago" class="d-none d-print-block" @change="onFileChange"/>
                        <i class="fas fa-cloud-upload-alt"></i>
                        Selecciona un archivo
                    </label>
                </div> 
            </form> 
        </div>         
    </div>

</template>
<script>
import { ref } from "vue";
import { uploadFileData } from "@/services/asistenciaService";
export default {
    // setup() {
    //     const file = ref(null);

    //     const onFileChange = (event) => {
    //         file = event.target.files[0];
    //     };

    //     const bulkUpload = async () => {
    //         try {
    //             if (file) {
    //                 await uploadFileData(file); // Llama al servicio para subir los datos del excel
    //                 alert('Archivo subido exitosamente');
    //             }
    //         } catch (error) {
    //             console.error('Error al subir el archivo:', error);
    //         }
    //     };


    //     return {
    //         onFileChange,
    //         bulkUpload,
    //     }
    // },
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
    max-width: 300px;
    padding: 20px;
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
    font-size: 1.1rem;
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