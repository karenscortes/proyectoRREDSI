<template>
    <div class="row mt-5 justify-content-center">
        <div class="col-9 text-center">
            <form>
                <label for="comprobante_pago" class="form-label d-flex justify-content-center">
                    Lista de Asistentes: 
                </label>
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
</template>

<!-- <script>
import { ref } from "vue";
import { uploadFileData } from "@/services/asistenciaService";
export default {
    setup() {
        const file = ref(null);

        const onFileChange = (event) => {
            file = event.target.files[0];
        };

        const bulkUpload = async () => {
            try {
                if (file) {
                    await uploadFileData(file); // Llama al servicio para subir los datos del excel
                    alert('Archivo subido exitosamente');
                }
            } catch (error) {
                console.error('Error al subir el archivo:', error);
            }
        };


        return {
            onFileChange,
            bulkUpload,
        }
    },
}

</script> -->