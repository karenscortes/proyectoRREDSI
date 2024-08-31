<template>
    <div class="contenedor_principal">
        <div class="container pt-5">
            <div class="col-12">
                <div class="row justify-content-around">
                    <div class="col-5 col-sm-2 m-2">
                        <button id="btn_datos_institucionales" class="btn btn-outline-dark"
                            @click="scrollToSection('datos_institucionales')">
                            <strong class="font-weight-bold">
                                <i class="fas fa-university title-icon"></i>
                            </strong>Datos Institucionales
                        </button>
                    </div>
                    <div class="col-5 col-sm-2 m-2">
                        <button id="btn_datos_tutor" class="btn btn-outline-dark"
                            @click="scrollToSection('datos_tutor')">
                            <strong class="font-weight-bold">
                                <i class="fas fa-regular fa-user"></i>
                            </strong>Datos tutor
                        </button>
                    </div>
                    <div class="col-5 col-sm-2 m-2">
                        <button id="btn_datos_ponentes" class="btn btn-outline-dark"
                            @click="scrollToSection('datos_ponentes')">
                            <strong class="font-weight-bold">
                                <i class="fas fa-solid fa-users"></i>
                            </strong>Datos ponentes
                        </button>
                    </div>
                    <div class="col-5 col-sm-2 m-2">
                        <button id="btn_datos_proyecto" class="btn btn-outline-dark"
                            @click="scrollToSection('datos_proyecto')">
                            <strong class="font-weight-bold">
                                <i class="fas fa-solid fa-file"></i>
                            </strong>Datos proyecto
                        </button>
                    </div>
                </div>
            </div>

            <!-- Datos Institucionales -->
            <div class="container mt-5" id="datos_institucionales">
                <div class="form-section">
                    <div class="d-flex align-items-center justify-content-center mb-3">
                        <i class="fas fa-university title-icon"></i>
                        <h2 class="text-center">Datos Institucionales</h2>
                    </div>
                    <div class="title-line"></div>
                    <!-- Formulario de Datos Institucionales -->
                    <form class="mt-4">
                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="institucion_educativa" class="form-label text-black">Institución
                                    Educativa:</label>
                                <input type="text" class="form-control" id="campo_institucion_educativa" placeholder>
                            </div>
                            <div class="col-md-6">
                                <label for="programa_academico" class="form-label text-black">Programa
                                    Académico:</label>
                                <input type="text" class="form-control" id="campo_programa_academico" placeholder>
                            </div>
                        </div>
                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="grupo_investigacion" class="form-label text-black">Grupo de
                                    Investigación:</label>
                                <input type="text" class="form-control" id="campo_grupo_investigacion" placeholder>
                            </div>
                            <div class="col-md-6">
                                <label for="linea_investigacion" class="form-label text-black">Línea de
                                    Investigación:</label>
                                <input type="text" class="form-control" id="linea_investigacion" placeholder>
                            </div>
                        </div>
                        <div class="row mb-3">
                            <div class="col-md-12">
                                <label for="semillero" class="form-label text-black">Nombre de
                                    Semillero:</label>
                                <input type="text" class="form-control" id="nombre_semillero" placeholder>
                            </div>
                        </div>
                    </form>
                </div>
            </div>

            <!-- Datos Tutor -->
            <div class="container mt-5" id="datos_tutor">
                <div class="form-section">
                    <div class="d-flex align-items-center justify-content-center mb-3">
                        <i class="fas fa-regular fa-user title-icon"></i>
                        <h2 class="text-center">Datos Tutor</h2>
                    </div>
                    <div class="title-line"></div>
                    <!-- Formulario de Datos Tutor -->
                    <form class="mt-4">
                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="tipo_documento" class="font-weight-bold text-dark">Tipo de documento</label>
                                <select v-model="form.tipoDocumento" class="form-control text-dark custom-select"
                                    required>
                                    <option value="" disabled selected>Seleccione una opción</option>
                                    <option value="cedula">Cédula</option>
                                    <option value="pasaporte">Pasaporte</option>
                                    <option value="cedula_extranjeria">Cédula de extranjeria</option>
                                </select>
                            </div>
                            <div class="col-md-6">
                                <label for="numero_documento" class="form-label text-black">Numero de documento:</label>
                                <input type="text" class="form-control" v-model="form.numeroDocumentoTutor" />
                            </div>
                        </div>
                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="nombres" class="form-label text-black">Nombres:</label>
                                <input type="text" class="form-control" v-model="form.nombresTutor" />
                            </div>
                            <div class="col-md-6">
                                <label for="apellidos" class="form-label text-black">Apellidos:</label>
                                <input type="text" class="form-control" v-model="form.apellidosTutor" />
                            </div>
                        </div>
                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="celular" class="form-label text-black">Celular:</label>
                                <input type="text" class="form-control" v-model="form.celularTutor" />
                            </div>
                            <div class="col-md-6">
                                <label for="email" class="form-label text-black">Email:</label>
                                <input type="email" class="form-control" v-model="form.emailTutor" required />
                            </div>
                        </div>
                        <div class="row align-items-end">
                            <div class="col-11 mb-2">
                                <label for="aval" class="text-dark">Aval:</label>
                            </div>
                            <div class="row mb-3 mx-1 text-center">
                                <div class="custom-file-upload" @click="triggerFileUpload">
                                    <i class="fas fa-image"></i>
                                    <span>Sube una imagen</span>
                                    <a href="#">Seleccionala</a> o arrástrala
                                </div>
                                <input type="file" id="file-upload" ref="fileUpload" style="display: none" />
                            </div>
                        </div>
                    </form>
                </div>
            </div>

            <!-- Datos Ponentes -->
            <div class="container mt-5" id="datos_ponentes">
                <div class="form-section">
                    <div class="d-flex align-items-center justify-content-center mb-3">
                        <i class="fas fa-solid fa-users litle title-icon"></i>
                        <h2 class="text-center">Datos Ponentes</h2>
                    </div>
                    <div class="title-line"></div>
                    <!-- Formulario de Datos Ponente 1 -->
                    <form>
                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="tipoDocumento1" class="form-label text-dark">Tipo de Documento:</label>
                                <select class="form-select" v-model="form.tipoDocumentoPonente1">
                                    <option value="" disabled selected>Seleccione una opción</option>
                                    <option value="CC">Cédula de Ciudadanía</option>
                                    <option value="TI">Tarjeta de Identidad</option>
                                    <option value="CE">Cédula de Extranjería</option>
                                </select>
                            </div>
                            <div class="col-md-6">
                                <label for="documento1" class="form-label text-dark">Número de Documento:</label>
                                <input type="text" class="form-control" v-model="form.numeroDocumentoPonente1" />
                            </div>
                        </div>
                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="nombres1" class="form-label text-dark">Nombres:</label>
                                <input type="text" class="form-control" v-model="form.nombresPonente1" />
                            </div>
                            <div class="col-md-6">
                                <label for="apellidos1" class="form-label text-dark">Apellidos:</label>
                                <input type="text" class="form-control" v-model="form.apellidosPonente1" />
                            </div>
                        </div>
                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="celular1" class="form-label text-dark">Celular:</label>
                                <input type="text" class="form-control" v-model="form.celularPonente1" />
                            </div>
                            <div class="col-md-6">
                                <label for="email1" class="form-label text-dark">Email:</label>
                                <input type="email" class="form-control" v-model="form.emailPonente1" />
                            </div>
                        </div>
                    </form>

                    <!-- Botón para agregar otro ponente -->
                    <div class="row align-items-end">
                        <div class="col-12">
                            <button class="btn btn-outline-dark" @click="toggleOtroPonente">
                                <i class="fas fa-plus"></i> Agregar Segundo Ponente
                            </button>
                        </div>
                    </div>

                    <!-- Formulario de Otro Ponente (Visible/Oculto) -->
                    <form v-if="otroPonenteVisible">
                        <div class="d-flex align-items-center justify-content-center mb-3 mt-5">
                            <i class="fas fa-solid fa-users litle title-icon"></i>
                            <h2 class="text-center">Otro Ponente</h2>
                        </div>
                        <div class="title-line"></div>
                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="tipoDocumento2" class="form-label text-dark">Tipo de Documento:</label>
                                <select class="form-select" v-model="form.tipoDocumentoPonente2">
                                    <option value="" disabled selected>Seleccione una opción</option>
                                    <option value="CC">Cédula de Ciudadanía</option>
                                    <option value="TI">Tarjeta de Identidad</option>
                                    <option value="CE">Cédula de Extranjería</option>
                                </select>
                            </div>
                            <div class="col-md-6">
                                <label for="documento2" class="form-label text-dark">Número de Documento:</label>
                                <input type="text" class="form-control" v-model="form.numeroDocumentoPonente2" />
                            </div>
                        </div>
                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="nombres2" class="form-label text-dark">Nombres:</label>
                                <input type="text" class="form-control" v-model="form.nombresPonente2" />
                            </div>
                            <div class="col-md-6">
                                <label for="apellidos2" class="form-label text-dark">Apellidos:</label>
                                <input type="text" class="form-control" v-model="form.apellidosPonente2" />
                            </div>
                        </div>
                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label for="celular2" class="form-label text-dark">Celular:</label>
                                <input type="text" class="form-control" v-model="form.celularPonente2" />
                            </div>
                            <div class="col-md-6">
                                <label for="email2" class="form-label text-dark">Email:</label>
                                <input type="email" class="form-control" v-model="form.emailPonente2" />
                            </div>
                        </div>
                    </form>

                </div>
            </div>

            <!-- Datos Proyecto -->
            <div class="container mt-5" id="datos_proyecto">
                <div class="form-section">
                    <div class="d-flex align-items-center justify-content-center mb-3">
                        <i class="fas fa-solid fa-file title-icon"></i>
                        <h2 class="text-center">Datos Proyecto</h2>
                    </div>
                    <div class="title-line"></div>
                    <!-- Formulario de Datos Proyecto -->
                    <form>
                        <!-- Fila 1: Autores y Modalidad -->
                        <div class="form-row">
                            <div>
                                <label for="autores" class="text-dark">Autores:</label>
                                <div>
                                    <input type="text" id="autores_proyecto" v-model="autores"
                                        placeholder="Nombre del autor" class="col-10" readonly />
                                    <button type="button" class="add-author-btn col-1 text-dark"
                                        @click="openModal">+</button>
                                </div>
                            </div>
                            <div class="mr-2 col-6">
                                <label for="modalidad" class="text-dark">Modalidad:</label>
                                <select id="modalidad_proyecto" v-model="modalidad">
                                    <option value="">Seleccione una opción</option>
                                    <option value="Poster">Poster</option>
                                    <option value="En curso">En curso</option>
                                    <option value="Concluido">Concluido</option>
                                </select>
                            </div>
                        </div>

                        <!-- Fila 2: Título y Propuesta Escrita -->
                        <div class="form-row">
                            <div>
                                <label for="titulo" class="text-dark">Título:</label>
                                <input type="text" id="titulo_proyecto" v-model="titulo"
                                    placeholder="Título del proyecto" />
                            </div>
                            <div class="ml-2">
                                <label for="propuesta_escrita" class="form-label text-black">Propuesta Escrita:</label>
                                <input type="file" class="form-control" @change="handleFileUpload('propuesta')" />
                            </div>
                        </div>

                        <!-- Fila 3: Área de Conocimiento y Poster -->
                        <div class="form-row">
                            <div>
                                <label for="area-conocimiento" class="text-dark">Área de conocimiento:</label>
                                <select id="area-conocimiento_proyecto" v-model="areaConocimiento">
                                    <option value="">Seleccione una opción</option>
                                    <option value="Desarrollo de Software">Desarrollo de Software</option>
                                    <option value="Ciencia de Datos">Ciencia de Datos</option>
                                    <option value="Seguridad Informática">Seguridad Informática</option>
                                </select>
                            </div>
                            <div>
                                <label for="poster" class="form-label text-black">Poster:</label>
                                <input type="file" class="form-control" @change="handleFileUpload('poster')" />
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- Modal para agregar autores -->
    <div id="authorModal" v-if="modalVisible" class="modal">
        <div class="modal-content">
            <div class="modal-header font-weight-bold text-dark">
                <h2>Agregar Autor</h2>
            </div>
            <div class="modal-body">
                <label for="nombreAutor" class="text-dark">Nombre</label>
                <input type="text" id="nombreAutor" v-model="nombreAutor" placeholder="Escribe el nombre" />
            </div>
            <div id="listaAutores">
                <div v-for="(autor, index) in listaAutores" :key="index">{{ autor }}</div>
            </div>
            <div class="modal-footer">
                <button class="add-btn btn btn-outline-dark" @click="addAuthor"
                    style="background: rgb(255, 182, 6)">Agregar</button>
                <button class="close-btn" @click="closeModal">Cerrar</button>
            </div>
        </div>
    </div>
    <div class="row align-items-end">
        <div class="col-12 m-3">
            <button class="btn btn-outline-dark" @click="EnviarFormulario" style="background: rgb(255, 182, 6)">
                Enviar
            </button>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            form: {
                institucionEducativa: '',
                programaAcademico: '',
                grupoInvestigacion: '',
                lineaInvestigacion: '',
                nombreSemillero: '',
                tipoDocumento: '',
                numeroDocumentoTutor: '',
                nombresTutor: '',
                apellidosTutor: '',
                celularTutor: '',
                emailTutor: '',
                tipoDocumentoPonente1: '',
                numeroDocumentoPonente1: '',
                nombresPonente1: '',
                apellidosPonente1: '',
                celularPonente1: '',
                emailPonente1: '',
                tipoDocumentoPonente2: '',
                numeroDocumentoPonente2: '',
                nombresPonente2: '',
                apellidosPonente2: '',
                celularPonente2: '',
                emailPonente2: '',
                nombreProyecto: '',
                areaConocimiento: '',
                resumenProyecto: '',
                objetivoProyecto: '',
                justificacionProyecto: '',
                autores: '',
                modalidad: '',
                titulo: '',
                propuestaEscrita: '',
                poster: '',
                nombreAutor: '',
                listaAutores: [],
                modalVisible: false
            },
            autores: [],
            otroPonenteVisible: false,
        };
    },
    methods: {
        openModal() {
            this.modalVisible = true;
        },
        closeModal() {
            this.modalVisible = false;
        },

        handleFileUpload(event) {
            const file = event.target.files[0];
            console.log('Archivo seleccionado:', file);
        },
        scrollToSection(sectionId) {
            const section = document.getElementById(sectionId);
            if (section) {
                section.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        },
        toggleOtroPonente() {
            this.otroPonenteVisible = !this.otroPonenteVisible;
        },
        triggerFileUpload() {
            this.$refs.fileUpload.click();
        },
        addAuthor() {
            if (this.nombreAutor.trim() !== '') {
                this.listaAutores.push(this.nombreAutor);
                if (this.autores.trim() === '') {
                    this.autores = this.nombreAutor;
                } else {
                    this.autores += ', ' + this.nombreAutor;
                }
                this.nombreAutor = '';
                this.closeModal(); // Cerrar el modal después de agregar el autor
            }
        },
    }
}
   
</script>

<style scoped>
.scroll-div {
    width: 1000px;
    height: 400px;
    overflow-y: auto;
    overflow-x: hidden;
}

body {
    font-family: Arial, sans-serif;
    margin: 20px;
    background-color: #f7f7f7;
}

.form-section {
    background-color: #f8f9fa;
    border: 1px solid #ced4da;
    padding: 20px;
    border-radius: 5px;
    max-width: 800px;
    margin: auto;
}

.form-section h2 {
    color: rgb(255, 182, 6);
    text-align: center;
}

.form-section .title-icon {
    color: rgb(255, 182, 6);
    margin-right: 10px;
    font-size: 1.5rem;
    margin-bottom: 10px;
}

.title-line {
    border-top: 2px solid rgb(255, 182, 6);
    margin-top: -10px;
}

.btn:hover {
    box-shadow: none;
    color: #494949;
    background-color: rgb(255, 182, 6);
}

.accordion-button:focus {
    box-shadow: none;
    background-color: rgb(255, 182, 6);
    outline: none;
}

.span_acor {
    font-size: 18px
}

.modal-header .icon {
    color: rgb(255, 182, 6);
    font-size: 2rem;
    margin-right: 10px;
}

.modal-header {
    color: #000000;
    font-size: 2rem;
    margin-right: 10px;
}

.enlace {
    padding: 0.6rem;
    text-decoration: none;
    text-align: center;
    color: black;
    transition: all 0.4s ease-in-out;
}

.enlace:focus {
    background-color: rgb(255, 182, 6);
    color: black;
}

#cont_consultarProyecto {
    scroll-margin-top: 104px;
}

.botonAbrir {
    width: 30%;
    font-size: 18px;
}

.w-30 {
    width: 30% !important;
}

.btn-custom {
    display: inline-flex;
    align-items: center;
    padding: 0.5rem 1rem;
    border: 1px solid transparent;
    border-radius: 0.375rem;
    font-size: 1rem;
    text-align: center;
    text-decoration: none;
    background-color: rgb(255, 182, 6);
    color: black;
}

.btn-custom:hover {
    background-color: #e0a800;
    color: black;
}

.btn-custom i {
    margin-right: 0.5rem;
}

.scroll-div {
    width: 1000px;
    height: 400px;
    overflow-y: auto;
    overflow-x: hidden;
    width: 1000px;
    height: 400px;
    overflow-y: auto;
    overflow-x: hidden;
}

body {
    font-family: Arial, sans-serif;
    margin: 20px;
    background-color: #f7f7f7;
}

.form-section {
    background-color: #f8f9fa;
    /* Color más oscuro que el blanco */
    border: 1px solid #ced4da;
    /* Borde del div */
    background-color: #f8f9fa;
    border: 1px solid #ced4da;
    padding: 20px;
    border-radius: 5px;
    max-width: 800px;
    margin: auto;
}

.form-section h2 {
    color: rgb(255, 182, 6);
    /* Color del encabezado */
    color: rgb(255, 182, 6);
    text-align: center;
}

.form-section .title-icon {
    color: rgb(255, 182, 6);
    /* Color del ícono */
    color: rgb(255, 182, 6);
    margin-right: 10px;
    font-size: 1.5rem;
    /* Tamaño del ícono más grande */
    font-size: 1.5rem;
    margin-bottom: 10px;
}

.title-line {
    border-top: 2px solid rgb(255, 182, 6);
    /* Color de la línea */
    border-top: 2px solid rgb(255, 182, 6);
    margin-top: -10px;
    margin-bottom: 20px;
}

.form-row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
}

.form-row>div {
    flex: 1;
    margin-right: 20px;
}

.form-row>div:last-child {
    margin-right: 0;
}



input[type="text"],
select {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
}

.custom-file-upload {
    border: 2px dashed #ced4da;
    border-radius: 10px;
    text-align: center;
    padding: 20px;
    cursor: pointer;
}

.custom-file-upload:hover {
    border-color: rgb(255, 182, 6);
}

.custom-file-upload i {
    font-size: 2rem;
    color: rgb(0, 123, 255);
}

.custom-file-upload span {
    display: block;
    margin-top: 10px;
    font-weight: bold;
}

.custom-file-upload a {
    color: rgb(0, 0, 0);
    text-decoration: none;
}

.add-author-btn {
    background-color: rgb(255, 182, 6);
    color: black;
    border: none;
    padding: 5px;
    border-radius: 3px;
    font-size: 18px;
    text-align: center;
    cursor: pointer;
}

.modal-content {
    background-color: #fefefe;
    margin: 15% auto;
    padding: 10px;
    border: 1px solid #888;
    width: 400px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

.modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: bold;
    margin-bottom: 15px;
}

.modal-header span {
    cursor: pointer;
    font-size: 1.5rem;
}

.modal-body {
    margin-bottom: 15px;
}

.modal-footer {
    text-align: center;
}

.modal-footer button {
    margin: 0 10px;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 14px;
}

.add-btn {
    color: rgb(0, 0, 0);
}

.close-btn {
    background-color: #b7b7b7;
    color: rgb(0, 0, 0);
}

#listaAutores div {
    margin-top: 5px;
    padding: 5px;
    background-color: #f1f1f1;
    border-radius: 5px;
}

.accordion {
    display: none;
}

@media only screen and (max-width:767px) {
    .contenedor_principal {
        display: none;
    }

    .accordion {
        display: block;
    }

    .card {
        width: 100%;
        text-align: left;
        text-decoration: none;
        background-color: #f7f7f7;
        border: 1px solid black;
        margin-bottom: 2rem;
    }

    .card button {
        font-weight: 700;
        text-align: center;
    }

    .toggle-button:not(.collapsed) {
        color: rgb(255, 182, 6);
    }

}
</style>