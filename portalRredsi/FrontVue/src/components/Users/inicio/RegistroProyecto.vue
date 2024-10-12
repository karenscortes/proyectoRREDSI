<template>
  <div class="container">
    <!-- Sección Datos del Proyecto -->
    <div style="border: 1px">
      
      <form class="mt-4" @submit.prevent="registrarProyecto">
        <div class="form-section mt-5" style="border: 1px solid #ddd; padding: 20px; border-radius: 10px;">
          <h2 class="text-center section-title">Datos del Proyecto</h2>
          <div class="row mb-3">
            <!-- Selector de Institución Educativa -->
            <div class="col-md-6">
              <label for="institucion_educativa" class="form-label text-black">Institución Educativa:</label>
              <instituciones_Select 
                v-model="datosProyecto.institucion_educativa" 
                @institucion-selected="setInstitucionEducativa" 
                required />
            </div>
            <div class="col-md-6">
              <label for="programa_academico" class="form-label text-black">Programa Académico:</label>
              <input v-model="datosProyecto.programa_academico" type="text" class="form-control" id="programa_academico" required />
            </div>
          </div>
  
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="grupo_investigacion" class="form-label text-black">Grupo de Investigación:</label>
              <input v-model="datosProyecto.grupo_investigacion" type="text" class="form-control" id="grupo_investigacion" required />
            </div>
            <div class="col-md-6">
              <label for="linea_investigacion" class="form-label text-black">Línea de Investigación:</label>
              <input v-model="datosProyecto.linea_investigacion" type="text" class="form-control" id="linea_investigacion" required />
            </div>
          </div>
  
          <!-- Campo de Nombre del Semillero -->
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="nombre_semillero" class="form-label text-black">Nombre del Semillero:</label>
              <input v-model="datosProyecto.nombre_semillero" type="text" class="form-control" id="nombre_semillero" required />
            </div>
            <div class="col-md-6">
              <label for="modalidad" class="form-label text-black">Modalidad:</label>
              <ModalidadesSelect 
                v-model="datosProyecto.modalidad" 
                @modalidad-selected="setModalidad" 
                required />
            </div>
          </div>
  
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="titulo_proyecto" class="form-label text-black">Título del Proyecto:</label>
              <input v-model="datosProyecto.titulo" type="text" class="form-control" id="titulo_proyecto" required />
            </div>
            <div class="col-md-6">
              <label for="area_conocimiento" class="form-label text-black">Área de Conocimiento:</label>
              <areasConocimiento_Select 
                v-model="datosProyecto.area_conocimiento" 
                @area-conocimiento-selected="setAreaConocimiento" 
                required />
            </div>
          </div>
  
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="propuesta_escrita" class="form-label text-black">Propuesta Escrita:</label>
              <input type="file" @change="handleFileChange($event, 'propuesta_escrita')" class="form-control" id="propuesta_escrita" required />
            </div>
            <div class="col-md-6">
              <label for="aval" class="form-label text-black">Aval:</label>
              <input type="file" @change="handleFileChange($event, 'aval')" class="form-control" id="aval" required />
            </div>
          </div>
        </div>
        

        <!-- Datos del Tutor -->
        <div class="form-section mt-5" style="border: 1px solid #ddd; padding: 20px; border-radius: 10px;">
          <h2 class="text-center section-title">Datos del Tutor</h2>
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="tipo_documento_tutor" class="form-label text-black">Tipo de Documento:</label>
              <TipoDocumentoSelect 
                v-model="datosTutor.tipo_documento" 
                @tipo-documento-selected="setTipoDocumentoTutor" 
                required />
            </div>
            <div class="col-md-6">
              <label for="numero_documento_tutor" class="form-label text-black">Número de Documento:</label>
              <input v-model="datosTutor.numero_documento" type="text" class="form-control" id="numero_documento_tutor" required />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="nombres_tutor" class="form-label text-black">Nombres:</label>
              <input v-model="datosTutor.nombres" type="text" class="form-control" id="nombres_tutor" required />
            </div>
            <div class="col-md-6">
              <label for="apellidos_tutor" class="form-label text-black">Apellidos:</label>
              <input v-model="datosTutor.apellidos" type="text" class="form-control" id="apellidos_tutor" required />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="celular_tutor" class="form-label text-black">Celular:</label>
              <input v-model="datosTutor.celular" type="text" class="form-control" id="celular_tutor" required />
            </div>
            <div class="col-md-6">
              <label for="correo_tutor" class="form-label text-black">Correo Electrónico:</label>
              <input v-model="datosTutor.correo" type="email" class="form-control" id="correo_tutor" required />
            </div>
          </div>
        </div>

        <!-- Datos del Ponente 1 -->
        <div class="form-section mt-5" style="border: 1px solid #ddd; padding: 20px; border-radius: 10px;">
          <h2 class="text-center section-title">Datos del Ponente 1</h2>
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="tipo_documento_ponente1" class="form-label text-black">Tipo de Documento:</label>
              <TipoDocumentoSelect 
                v-model="datosPonente.tipo_documento" 
                @tipo-documento-selected="setTipoDocumentoPonente" 
                required />
            </div>
            <div class="col-md-6">
              <label for="numero_documento_ponente1" class="form-label text-black">Número de Documento:</label>
              <input v-model="datosPonente.numero_documento" type="text" class="form-control" id="numero_documento_ponente1" required />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="nombres_ponente1" class="form-label text-black">Nombres:</label>
              <input v-model="datosPonente.nombres" type="text" class="form-control" id="nombres_ponente1" required />
            </div>
            <div class="col-md-6">
              <label for="apellidos_ponente1" class="form-label text-black">Apellidos:</label>
              <input v-model="datosPonente.apellidos" type="text" class="form-control" id="apellidos_ponente1" required />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="celular_ponente1" class="form-label text-black">Celular:</label>
              <input v-model="datosPonente.celular" type="text" class="form-control" id="celular_ponente1" required />
            </div>
            <div class="col-md-6">
              <label for="correo_ponente1" class="form-label text-black">Correo Electrónico:</label>
              <input v-model="datosPonente.correo" type="email" class="form-control" id="correo_ponente1" required />
            </div>
          </div>
           <!-- Ponente Opcional -->
        <div v-if="mostrarPonenteOpcional" class="form-section mt-5" style="border: 1px solid #ddd; padding: 20px; border-radius: 10px;">
          <h4 class="text-center section-title">Datos del Ponente Opcional</h4>
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="tipo_documento_opcional" class="form-label text-black">Tipo de Documento:</label>
              <TipoDocumentoSelect 
                v-model="ponenteOpcional.tipo_documento" 
                @tipo-documento-selected="setTipoDocumentoPonenteOpcional" />
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
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="celular_opcional" class="form-label text-black">Celular:</label>
              <input v-model="ponenteOpcional.celular" type="text" class="form-control" id="celular_opcional" />
            </div>
            <div class="col-md-6">
              <label for="correo_opcional" class="form-label text-black">Correo Electrónico:</label>
              <input v-model="ponenteOpcional.correo" type="email" class="form-control" id="correo_opcional" />
            </div>
          </div>

          <!-- Botón para eliminar Ponente Opcional -->
          <div class="text-center mt-3">
            <button type="button" @click="eliminarPonenteOpcional" class="btn btn-outline-dark btn-sm">Eliminar Ponente Opcional</button>
          </div>
        </div>

        <!-- Botón para agregar o eliminar Ponente Opcional -->
        <div v-if="!mostrarPonenteOpcional" class="text-center mt-3">
          <button type="button" @click="agregarPonenteOpcional" class="btn btn-outline-dark btn-sm">Agregar Ponente Opcional</button>
        </div>
        </div>

       

        <!-- Sección Datos de los Autores -->
        <div class="form-section mt-5" style="border: 1px solid #ddd; padding: 20px; border-radius: 10px;">
          <h2 class="text-center section-title">Nombres de los Autores</h2>
          <div class="row mb-3">
            <div class="col-md-10">
              <input v-model="nuevoAutor.nombre" type="text" class="form-control text-black " placeholder="Nombre del Autor" />
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
        </div>

        <!-- Botón para registrar el proyecto -->
        <div class="text-center">
          <button type="submit" class="btn btn-outline-dark">Guardar Proyecto</button>
        </div>

      </form>
    </div>
  </div>
</template>

<script>
import ModalidadesSelect from './ModalidadesSelect.vue';
import TipoDocumentoSelect from './TipoDocumentoSelect.vue';
import areasConocimiento_Select from './areasConocimiento_Select.vue';
import instituciones_Select from './instituciones_Select.vue';
import { createProject } from '@/services/ProyectoService';
import { ref } from 'vue';
import { useToastUtils } from '@/utils/toast';

export default {
  components: {
    ModalidadesSelect,
    areasConocimiento_Select,
    TipoDocumentoSelect,
    instituciones_Select,
  },
  setup() {
    const { showSuccessToast, showErrorToast } = useToastUtils();

    const showModal = ref(false);
    const proyectoCodigo = ref('');

    const datosProyecto = ref({
      institucion_educativa: null,  // ID de Institución
      programa_academico: '',
      grupo_investigacion: '',
      linea_investigacion: '',
      nombre_semillero: '', // Campo añadido
      modalidad: null,  // ID de Modalidad
      titulo: '',
      propuesta_escrita: null,
      area_conocimiento: null,  // ID de Área de Conocimiento
      aval: null,
    });

    const datosTutor = ref({
      tipo_documento: null,  // ID de Tipo de Documento
      numero_documento: '',
      nombres: '',
      apellidos: '',
      celular: '',
      correo: '',
    });

    const datosPonente = ref({
      tipo_documento: null,  // ID de Tipo de Documento
      numero_documento: '',
      nombres: '',
      apellidos: '',
      celular: '',
      correo: '',
    });

    const ponenteOpcional = ref({
      tipo_documento: null,  // ID de Tipo de Documento
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

    const handleFileChange = (event, key) => {
      const file = event.target.files[0];
      datosProyecto.value[key] = file;
    };

    const agregarPonenteOpcional = () => {
      mostrarPonenteOpcional.value = true;
    };

    const eliminarPonenteOpcional = () => {
      mostrarPonenteOpcional.value = false;
      ponenteOpcional.value = {
        tipo_documento: null,
        numero_documento: '',
        nombres: '',
        apellidos: '',
        celular: '',
        correo: '',
      };
    };

    const agregarAutor = () => {
      if (nuevoAutor.value.nombre.trim()) {
        autores.value.push({ ...nuevoAutor.value });
        nuevoAutor.value.nombre = '';
        showSuccessToast('Autor agregado correctamente');
      } else {
        showErrorToast('El nombre del autor no puede estar vacío');
      }
    };

    const eliminarAutor = (index) => {
      autores.value.splice(index, 1);
      showSuccessToast('Autor eliminado correctamente');
    };

    const registrarProyecto = async () => {
      try {
        const response = await createProject(
          datosProyecto.value,
          datosTutor.value,
          datosPonente.value,
          ponenteOpcional.value,
          autores.value
        );

        proyectoCodigo.value = response.data.id_proyecto;
        showSuccessToast(`Proyecto registrado exitosamente, el Código de identificación es: ${proyectoCodigo.value}.`);
      } catch (error) {
        if (error.message) {
          showErrorToast(error.message);
        } else {
          showErrorToast('Error inesperado al registrar el proyecto.');
        }
      }
    };

    const setInstitucionEducativa = (id) => datosProyecto.value.institucion_educativa = id;
    const setModalidad = (id) => datosProyecto.value.modalidad = id;
    const setAreaConocimiento = (id) => datosProyecto.value.area_conocimiento = id;
    const setTipoDocumentoTutor = (id) => datosTutor.value.tipo_documento = id;
    const setTipoDocumentoPonente = (id) => datosPonente.value.tipo_documento = id;
    const setTipoDocumentoPonenteOpcional = (id) => ponenteOpcional.value.tipo_documento = id;

    return {
      datosProyecto,
      datosTutor,
      datosPonente,
      ponenteOpcional,
      mostrarPonenteOpcional,
      nuevoAutor,
      autores,
      handleFileChange,
      agregarPonenteOpcional,
      eliminarPonenteOpcional,
      agregarAutor,
      eliminarAutor,
      registrarProyecto,
      proyectoCodigo,
      setInstitucionEducativa,
      setModalidad,
      setAreaConocimiento,
      setTipoDocumentoTutor,
      setTipoDocumentoPonente,
      setTipoDocumentoPonenteOpcional,
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
    border: solid black;
    color: rgb(0, 0, 0);
    transition: all 0.3s;
  }

  .btn-outline-dark:hover {
    background-color: rgb(84, 84, 84);
    color: white;
  }

  .list-group-item {
    background-color: #fff;
    border: 1px solid black;
  }

</style>
