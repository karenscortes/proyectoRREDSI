<template>
    <div class="container mt-5 pt-5">
      <!-- Sección Datos del Proyecto -->
      <div v-if="showSection === 'datosProyecto'" class="form-section mt-5">
        <h2 class="text-center section-title">Datos del Proyecto</h2>
        <form class="mt-4" @submit.prevent="guardarDatosProyecto">
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="institucion_educativa" class="form-label text-black">Institución Educativa:</label>
              <input v-model="datosProyecto.institucion_educativa" type="text" class="form-control" id="institucion_educativa" placeholder="Nombre de la institución" />
            </div>
            <div class="col-md-6">
              <label for="programa_academico" class="form-label text-black">Programa Académico:</label>
              <input v-model="datosProyecto.programa_academico" type="text" class="form-control" id="programa_academico" placeholder="Nombre del programa" />
            </div>
          </div>
  
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="grupo_investigacion" class="form-label text-black">Grupo de Investigación:</label>
              <input v-model="datosProyecto.grupo_investigacion" type="text" class="form-control" id="grupo_investigacion" placeholder="Nombre del grupo de investigación" />
            </div>
            <div class="col-md-6">
              <label for="linea_investigacion" class="form-label text-black">Línea de Investigación:</label>
              <input v-model="datosProyecto.linea_investigacion" type="text" class="form-control" id="linea_investigacion" placeholder="Nombre de la línea de investigación" />
            </div>
          </div>
  
          <!-- Modalidad y Área de Conocimiento en una línea -->
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="modalidad" class="form-label text-black">Modalidad:</label>
              <ModalidadesSelect v-model="datosProyecto.modalidad" />
            </div>
            <div class="col-md-6">
              <label for="area_conocimiento" class="form-label text-black">Área de Conocimiento:</label>
              <AreasConocimientoSelect v-model="datosProyecto.area_conocimiento" />
            </div>
          </div>
  
          <!-- Título del Proyecto -->
          <div class="row mb-3">
            <div class="col-md-12">
              <label for="titulo_proyecto" class="form-label text-black">Título del Proyecto:</label>
              <input v-model="datosProyecto.titulo" type="text" class="form-control" id="titulo_proyecto" placeholder="Título del proyecto" />
            </div>
          </div>
  
          <!-- Propuesta Escrita y Poster en una línea -->
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="propuesta_escrita" class="form-label text-black">Propuesta Escrita:</label>
              <input type="file" @change="handleFileUpload($event, 'propuesta_escrita')" class="form-control" id="propuesta_escrita" />
            </div>
            <div class="col-md-6">
              <label for="poster" class="form-label text-black">Poster:</label>
              <input type="file" @change="handleFileUpload($event, 'poster')" class="form-control" id="poster" />
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
              <input v-model="datosTutor.numero_documento" type="text" class="form-control" id="numero_documento_tutor" />
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
  
          <!-- Campos adicionales: Celular y Correo -->
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="celular_tutor" class="form-label text-black">Celular:</label>
              <input v-model="datosTutor.celular" type="text" class="form-control" id="celular_tutor" />
            </div>
            <div class="col-md-6">
              <label for="correo_tutor" class="form-label text-black">Correo Electrónico:</label>
              <input v-model="datosTutor.correo" type="email" class="form-control" id="correo_tutor" />
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
              <input v-model="datosPonente.numero_documento" type="text" class="form-control" id="numero_documento_ponente" />
            </div>
          </div>
          <div class="col-md-6">
            <label for="nombres_ponente" class="form-label text-black">Nombres:</label>
            <input v-model="datosPonente.nombres" type="text" class="form-control" id="nombres_ponente" />
          </div>
          <div class="col-md-6">
            <label for="apellidos_ponente" class="form-label text-black">Apellidos:</label>
            <input v-model="datosPonente.apellidos" type="text" class="form-control" id="apellidos_ponente" />
          </div>
          <div class="text-center">
            <button type="submit" class="btn btn-outline-dark btn-sm">Guardar Datos del Ponente</button>
          </div>
  
          <!-- Botón para agregar ponente opcional -->
          <div v-if="!mostrarPonenteOpcional" class="text-center mt-3">
            <button type="button" @click="agregarPonenteOpcional" class="btn btn-outline-dark btn-sm">Agregar Ponente Opcional</button>
          </div>
  
          <!-- Ponente Opcional -->
          <div v-if="mostrarPonenteOpcional" class="mt-4 optional-ponente">
            <h4 class="text-center section-subtitle">Ponente Opcional</h4>
            <div class="row mb-3">
              <div class="col-md-6">
                <label for="tipo_documento_opcional" class="form-label text-black">Tipo de Documento:</label>
                <TipoDocumentoSelect v-model="ponenteOpcional.tipo_documento" />
              </div>
              <div class="col-md-6">
                <label for="numero_documento_opcional" class="form-label text-black">Número de Documento:</label>
                <input v-model="ponenteOpcional.numero_documento" type="text" class="form-control" id="numero_documento_opcional" />
              </div>
            </div>
            <div class="row mb-3">
              <div class="col-md-6">
                <label for="nombres_opcional" class="form-label text-black">Nombres:</label>
                <input v-model="ponenteOpcional.nombres" type="text" class="form-control" id="nombres_opcional" />
              </div>
              <div class="col-md-6">
                <label for="apellidos_opcional" class="form-label text-black">Apellidos:</label>
                <input v-model="ponenteOpcional.apellidos" type="text" class="form-control" id="apellidos_opcional" />
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
              <input v-model="nuevoAutor.nombre" type="text" class="form-control" placeholder="Nombre del Autor" />
            </div>
            <div class="col-md-2 text-center">
              <button type="button" class="btn btn-outline-dark btn-sm" @click="agregarAutor">Agregar</button>
            </div>
          </div>
  
          <ul class="list-group mb-3">
            <li v-for="(autor, index) in autores" :key="index" class="list-group-item d-flex justify-content-between align-items-center">
              {{ autor.nombre }}
              <button type="button" class="btn btn-outline-dark btn-sm" @click="eliminarAutor(index)">Eliminar</button>
            </li>
          </ul>
  
          <!-- Botón para registrar el proyecto -->
          <div class="text-center">
            <button type="button" @click="registrarProyecto" class="btn btn-outline-dark btn-sm">Registrar Proyecto</button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import TipoDocumentoSelect from './TipoDocumentoSelect.vue';
  import ModalidadesSelect from './ModalidadesSelect.vue';
  import AreasConocimientoSelect from './AreasConocimientoSelect.vue';
  import { ref } from 'vue';
  import { insertarProyecto, insertarParticipanteProyecto, agregarProyectoConvocatoria } from '@/services/proyectoService.js';
  
  export default {
    components: {
      ModalidadesSelect,
      AreasConocimientoSelect,
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
        celular: '',
        correo: '',
      });
  
      const datosPonente = ref({
        tipo_documento: null,
        numero_documento: '',
        nombres: '',
        apellidos: '',
        celular: '',
        correo: '',
      });
  
      const ponenteOpcional = ref({
        tipo_documento: null,
        numero_documento: '',
        nombres: '',
        apellidos: '',
        celular: '',
        correo: '',
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
  
      const guardarDatosProyecto = async () => {
        try {
          const response = await insertarProyecto(
            datosProyecto.value.institucion_educativa,
            datosProyecto.value.modalidad,
            datosProyecto.value.area_conocimiento,
            datosProyecto.value.titulo,
            datosProyecto.value.programa_academico,
            datosProyecto.value.grupo_investigacion,
            datosProyecto.value.linea_investigacion,
            datosProyecto.value.propuesta_escrita,
            datosProyecto.value.aval
          );
          console.log('Proyecto guardado con éxito:', response.data);
          showSection.value = 'datosTutor';  // Avanza a la siguiente sección
        } catch (error) {
          console.error('Error al guardar datos del proyecto:', error);
        }
      };
  
      const guardarDatosTutor = async () => {
        showSection.value = 'datosPonentes';
      };
  
      const guardarDatosPonente = async () => {
        showSection.value = 'datosAutores';
      };
  
      const registrarProyecto = async () => {
        try {
          // Lógica para registrar el proyecto en la base de datos
          await guardarDatosProyecto();
          // Lógica para registrar participantes en el proyecto
          await insertarParticipanteProyecto(datosTutor.value);
          // Lógica para agregar proyecto a la convocatoria
          await agregarProyectoConvocatoria(datosProyecto.value);
  
          alert('Proyecto registrado con éxito');
        } catch (error) {
          console.error('Error al registrar proyecto:', error);
          alert('Hubo un error al registrar el proyecto');
        }
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
    font-size: 1.2em;
  }
  
  .btn-outline-dark{
  
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
  