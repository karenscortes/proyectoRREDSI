<template>
    <div class="container mt-5 pt-5">
        <!-- Sección Datos del Proyecto -->
        <div v-if="showSection === 'datosProyecto'" class="form-section mt-5">
            <h2 class="text-center section-title">Datos del Proyecto</h2>
            <form class="mt-4" @submit.prevent="guardarDatosProyecto">
                <div class="row mb-3">
                    <div class="col-md-6">
                        <label for="institucion_educativa" class="form-label text-black">Institución Educativa:</label>
                        <input v-model="datosProyecto.institucion_educativa" type="text" class="form-control"
                            id="institucion_educativa" placeholder="Nombre de la institución" />
                    </div>
                    <div class="col-md-6">
                        <label for="programa_academico" class="form-label text-black">Programa Académico:</label>
                        <input v-model="datosProyecto.programa_academico" type="text" class="form-control"
                            id="programa_academico" placeholder="Nombre del programa" />
                    </div>
                </div>

                <div class="row mb-3">
                    <div class="col-md-6">
                        <label for="grupo_investigacion" class="form-label text-black">Grupo de Investigación:</label>
                        <input v-model="datosProyecto.grupo_investigacion" type="text" class="form-control"
                            id="grupo_investigacion" placeholder="Nombre del grupo de investigación" />
                    </div>
                    <div class="col-md-6">
                        <label for="linea_investigacion" class="form-label text-black">Línea de Investigación:</label>
                        <input v-model="datosProyecto.linea_investigacion" type="text" class="form-control"
                            id="linea_investigacion" placeholder="Nombre de la línea de investigación" />
                    </div>
                </div>

                <!-- Selector de Modalidad -->
                <div class="row mb-3">
                    <div class="col-md-6">
                        <label for="modalidad" class="form-label text-black">Modalidad:</label>
                        <ModalidadesSelect v-model="datosProyecto.modalidad" />
                    </div>
                </div>

                <!-- Título del Proyecto -->
                <div class="row mb-3">
                    <div class="col-md-12">
                        <label for="titulo_proyecto" class="form-label text-black">Título del Proyecto:</label>
                        <input v-model="datosProyecto.titulo" type="text" class="form-control" id="titulo_proyecto"
                            placeholder="Título del proyecto" />
                    </div>
                </div>

                <!-- Propuesta Escrita -->
                <div class="row mb-3">
                    <div class="col-md-12">
                        <label for="propuesta_escrita" class="form-label text-black">Propuesta Escrita:</label>
                        <input type="file" @change="handleFileUpload($event, 'propuesta_escrita')" class="form-control"
                            id="propuesta_escrita" />
                    </div>
                </div>

                <!-- Selector de Área de Conocimiento -->
                <div class="row mb-3">
                    <div class="col-md-6">
                        <label for="area_conocimiento" class="form-label text-black">Área de Conocimiento:</label>
                        <AreasConocimientoSelect v-model="datosProyecto.area_conocimiento" />
                    </div>
                </div>

                <!-- Poster -->
                <div class="row mb-3">
                    <div class="col-md-12">
                        <label for="poster" class="form-label text-black">Poster:</label>
                        <input type="file" @change="handleFileUpload($event, 'poster')" class="form-control"
                            id="poster" />
                    </div>
                </div>

                <!-- Aval -->
                <div class="row mb-3">
                    <div class="col-md-12">
                        <label for="aval" class="form-label text-black">Aval:</label>
                        <input type="file" @change="handleFileUpload($event, 'aval')" class="form-control" id="aval" />
                    </div>
                </div>

                <div class="text-center">
                    <button type="submit" class="btn btn-outline-dark btn-sm">Guardar Datos del Proyecto</button>
                </div>
            </form>
        </div>

        <!-- Sección Datos del Tutor -->
        <div v-if="showSection === 'datosTutor'" class="form-section mt-5">
            <h2 class="text-center section-title">Datos del Tutor</h2>
            <form class="mt-4" @submit.prevent="guardarDatosTutor">
                <div class="row mb-3">
                    <div class="col-md-6">
                        <label for="tipo_documento_tutor" class="form-label text-black">Tipo de Documento:</label>
                        <TipoDocumentoSelect v-model="datosTutor.tipo_documento" />
                    </div>
                    <div class="col-md-6">
                        <label for="numero_documento_tutor" class="form-label text-black">Número de Documento:</label>
                        <input v-model="datosTutor.numero_documento" type="text" class="form-control"
                            id="numero_documento_tutor" />
                    </div>
                </div>
                <div class="row mb-3">
                    <div class="col-md-6">
                        <label for="nombres_tutor" class="form-label text-black">Nombres:</label>
                        <input v-model="datosTutor.nombres" type="text" class="form-control" id="nombres_tutor" />
                    </div>
                    <div class="col-md-6">
                        <label for="apellidos_tutor" class="form-label text-black">Apellidos:</label>
                        <input v-model="datosTutor.apellidos" type="text" class="form-control" id="apellidos_tutor" />
                    </div>
                </div>

                <div class="text-center">
                    <button type="submit" class="btn btn-outline-dark btn-sm">Guardar Datos del Tutor</button>
                </div>
            </form>
        </div>

        <!-- Sección Datos de los Ponentes -->
        <div v-if="showSection === 'datosPonentes'" class="form-section mt-5">
            <h2 class="text-center section-title">Datos de los Ponentes</h2>
            <form class="mt-4" @submit.prevent="guardarDatosPonente">
                <div class="row mb-3">
                    <div class="col-md-6">
                        <label for="tipo_documento_ponente" class="form-label text-black">Tipo de Documento:</label>
                        <TipoDocumentoSelect v-model="datosPonente.tipo_documento" />
                    </div>
                    <div class="col-md-6">
                        <label for="numero_documento_ponente" class="form-label text-black">Número de Documento:</label>
                        <input v-model="datosPonente.numero_documento" type="text" class="form-control"
                            id="numero_documento_ponente" />
                    </div>
                </div>
                <div class="row mb-3">
                    <div class="col-md-6">
                        <label for="nombres_ponente" class="form-label text-black">Nombres:</label>
                        <input v-model="datosPonente.nombres" type="text" class="form-control" id="nombres_ponente" />
                    </div>
                    <div class="col-md-6">
                        <label for="apellidos_ponente" class="form-label text-black">Apellidos:</label>
                        <input v-model="datosPonente.apellidos" type="text" class="form-control"
                            id="apellidos_ponente" />
                    </div>
                </div>

                <div class="text-center">
                    <button type="submit" class="btn btn-outline-dark btn-sm">Guardar Datos del Ponente</button>
                </div>

                <!-- Botón para agregar ponente opcional -->
                <div v-if="!mostrarPonenteOpcional" class="text-center mt-3">
                    <button type="button" @click="agregarPonenteOpcional" class="btn btn-outline-dark btn-sm">Agregar
                        Ponente Opcional</button>
                </div>

                <!-- Ponente Opcional -->
                <div v-if="mostrarPonenteOpcional" class="mt-4 optional-ponente">
                    <h4 class="text-center section-subtitle">Ponente Opcional</h4>
                    <div class="row mb-3">
                        <div class="col-md-6">
                            <label for="tipo_documento_opcional" class="form-label text-black">Tipo de
                                Documento:</label>
                            <TipoDocumentoSelect v-model="ponenteOpcional.tipo_documento"/>
                        </div>
                        <div class="col-md-6">
                            <label for="numero_documento_opcional" class="form-label text-black">Número de
                                Documento:</label>
                            <input v-model="ponenteOpcional.numero_documento" type="text" class="form-control"
                                id="numero_documento_opcional" />
                        </div>
                    </div>
                    <div class="row mb-3">
                        <div class="col-md-6">
                            <label for="nombres_opcional" class="form-label text-black">Nombres:</label>
                            <input v-model="ponenteOpcional.nombres" type="text" class="form-control"
                                id="nombres_opcional" />
                        </div>
                        <div class="col-md-6">
                            <label for="apellidos_opcional" class="form-label text-black">Apellidos:</label>
                            <input v-model="ponenteOpcional.apellidos" type="text" class="form-control"
                                id="apellidos_opcional" />
                        </div>
                    </div>
                </div>
            </form>
        </div>

        <!-- Sección Datos de los Autores -->
        <div v-if="showSection === 'datosAutores'" class="form-section mt-5">
            <h2 class="text-center section-title">Datos de los Autores</h2>
            <form class="mt-4">
                <div class="row mb-3">
                    <div class="col-md-10">
                        <input v-model="nuevoAutor.nombre" type="text" class="form-control"
                            placeholder="Nombre del Autor" />
                    </div>
                    <div class="col-md-2 text-center">
                        <button type="button" class="btn btn-outline-dark btn-sm" @click="agregarAutor">Agregar</button>
                    </div>
                </div>

                <ul class="list-group mb-3">
                    <li v-for="(autor, index) in autores" :key="index"
                        class="list-group-item d-flex justify-content-between align-items-center">
                        {{ autor.nombre }}
                        <button type="button" class="btn btn-outline-dark btn-sm"
                            @click="eliminarAutor(index)">Eliminar</button>
                    </li>
                </ul>

                <!-- Botón para registrar el proyecto -->
                <div class="text-center">
                    <button type="button" @click="registrarProyecto" class="btn btn-outline-dark btn-sm">Registrar
                        Proyecto</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import TipoDocumentoSelect from './TipoDocumentoSelect.vue';
import { ref } from 'vue';

export default {
    components: {
        TipoDocumentoSelect,
    },
    setup() {
        const showSection = ref('datosProyecto');

        const datosProyecto = ref({
            institucion_educativa: '',
            programa_academico: '',
            grupo_investigacion: '',
            linea_investigacion: '',
            modalidad: null,
            titulo: '',
            propuesta_escrita: null,
            area_conocimiento: null,
            poster: null,
            aval: null,
        });

        const datosTutor = ref({
            tipo_documento: null,
            numero_documento: '',
            nombres: '',
            apellidos: '',
        });

        const datosPonente = ref({
            tipo_documento: null,
            numero_documento: '',
            nombres: '',
            apellidos: '',
        });

        const ponenteOpcional = ref({
            tipo_documento: null,
            numero_documento: '',
            nombres: '',
            apellidos: '',
        });

        const mostrarPonenteOpcional = ref(false);

        const nuevoAutor = ref({
            nombre: '',
        });

        const autores = ref([]);

        const handleFileUpload = (event, key) => {
            const file = event.target.files[0];
            datosProyecto.value[key] = file;
        };

        const agregarPonenteOpcional = () => {
            mostrarPonenteOpcional.value = true;
        };

        const agregarAutor = () => {
            autores.value.push({ ...nuevoAutor.value });
            nuevoAutor.value.nombre = '';
        };

        const eliminarAutor = (index) => {
            autores.value.splice(index, 1);
        };

        const guardarDatosProyecto = () => {
            console.log('Datos del Proyecto:', datosProyecto.value);
            showSection.value = 'datosTutor';
        };

        const guardarDatosTutor = () => {
            console.log('Datos del Tutor:', datosTutor.value);
            showSection.value = 'datosPonentes';
        };

        const guardarDatosPonente = () => {
            console.log('Datos del Ponente:', datosPonente.value);
            showSection.value = 'datosAutores';
        };

        const registrarProyecto = () => {
            console.log('Datos del Proyecto a registrar:', {
                datosProyecto: datosProyecto.value,
                datosTutor: datosTutor.value,
                datosPonente: datosPonente.value,
                ponenteOpcional: ponenteOpcional.value,
                autores: autores.value,
            });
            alert('Proyecto registrado con éxito');
        };

        return {
            showSection,
            datosProyecto,
            datosTutor,
            datosPonente,
            ponenteOpcional,
            mostrarPonenteOpcional,
            nuevoAutor,
            autores,
            handleFileUpload,
            agregarPonenteOpcional,
            agregarAutor,
            eliminarAutor,
            guardarDatosProyecto,
            guardarDatosTutor,
            guardarDatosPonente,
            registrarProyecto,
        };
    },
};
</script>

<style scoped>
.form-section {
    background-color: #f9f9f9;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 50px;
    margin-top: 80px;
}

.section-title {
    color: rgb(255, 182, 6);
    font-weight: bold;
    padding: 10px;
}

.section-subtitle {
    color: rgb(255, 182, 6);
    font-weight: bold;
}

.btn-outline-dark {
    border: 2px solid black;
    color: black;
    padding: 5px 15px;
    transition: all 0.3s;
}

.btn-outline-dark:hover {
    background-color: black;
    color: white;
}

.list-group-item {
    background-color: #fff;
    border: 1px solid black;
}

.optional-ponente {
    background-color: #e9ecef;
    padding: 20px;
    border-radius: 5px;
}
</style>