<template>
  <div class="container">
    <!-- Sección Datos del Proyecto -->
    <div>

      <form class="mt-4" @submit.prevent="registrarProyecto">
        <div class="form-section mt-5">
          <h2 class="text-center section-title">Datos del Proyecto</h2>
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="institucion_educativa" class="form-label text-black">Institución Educativa:</label>
              <instituciones_Select v-model="datosProyecto.institucion_educativa"
                @institucion-selected="setInstitucionEducativa" required />
            </div>
            <div class="col-md-6">
              <label for="programa_academico" class="form-label text-black">Programa Académico:</label>
              <input v-model="datosProyecto.programa_academico" type="text" class="form-control" id="programa_academico"
                required />
            </div>
          </div>

          <div class="row mb-3">
            <div class="col-md-6">
              <label for="grupo_investigacion" class="form-label text-black">Grupo de Investigación:</label>
              <input v-model="datosProyecto.grupo_investigacion" type="text" class="form-control"
                id="grupo_investigacion" required />
            </div>
            <div class="col-md-6">
              <label for="linea_investigacion" class="form-label text-black">Línea de Investigación:</label>
              <input v-model="datosProyecto.linea_investigacion" type="text" class="form-control"
                id="linea_investigacion" required />
            </div>
          </div>

          <div class="row mb-3">
            <div class="col-md-6">
              <label for="nombre_semillero" class="form-label text-black">Nombre del Semillero:</label>
              <input v-model="datosProyecto.nombre_semillero" type="text" class="form-control" id="nombre_semillero"
                required />
            </div>
            <div class="col-md-6">
              <label for="modalidad" class="form-label text-black">Modalidad:</label>
              <ModalidadesSelect v-model="datosProyecto.modalidad" @modalidad-selected="setModalidad" required />
            </div>
          </div>

          <div class="row mb-3">
            <div class="col-md-6">
              <label for="titulo_proyecto" class="form-label text-black">Título del Proyecto:</label>
              <input v-model="datosProyecto.titulo" type="text" class="form-control" id="titulo_proyecto" required />
            </div>
            <div class="col-md-6">
              <label for="area_conocimiento" class="form-label text-black">Área de Conocimiento:</label>
              <areasConocimiento_Select v-model="datosProyecto.area_conocimiento"
                @area-conocimiento-selected="setAreaConocimiento" required />
            </div>
          </div>

          <div class="row mb-3">
            <div class="col-md-6">
              <label for="propuesta_escrita" class="form-label text-black">Propuesta Escrita:</label>
              <input type="file" @change="handleFileChange($event, 'propuesta_escrita')" class="form-control"
                id="propuesta_escrita" required />
            </div>
            <div class="col-md-6">
              <label for="aval" class="form-label text-black">Aval:</label>
              <input type="file" @change="handleFileChange($event, 'aval')" class="form-control" id="aval" required />
            </div>
          </div>
        </div>

        <!-- Datos del Tutor -->
        <div class="form-section mt-5">
          <h2 class="text-center section-title">Datos del Tutor</h2>
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="tipo_documento_tutor" class="form-label text-black">Tipo de Documento:</label>
              <TipoDocumentoSelect v-model="datosTutor.tipo_documento" @tipo-documento-selected="setTipoDocumentoTutor"
                :disabled="datosTutor.bloqueado" required />
            </div>
            <div class="col-md-6">
              <label for="numero_documento_tutor" class="form-label text-black">Número de Documento:</label>
              <input v-model="datosTutor.numero_documento" @blur="buscarTutorPorDocumento" type="text"
                class="form-control" id="numero_documento_tutor" :disabled="datosTutor.bloqueado" required />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="nombres_tutor" class="form-label text-black">Nombres:</label>
              <input v-model="datosTutor.nombres" type="text" class="form-control" id="nombres_tutor"
                :disabled="datosTutor.bloqueado" required />
            </div>
            <div class="col-md-6">
              <label for="apellidos_tutor" class="form-label text-black">Apellidos:</label>
              <input v-model="datosTutor.apellidos" type="text" class="form-control" id="apellidos_tutor"
                :disabled="datosTutor.bloqueado" required />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="celular_tutor" class="form-label text-black">Celular:</label>
              <input v-model="datosTutor.celular" type="text" class="form-control" id="celular_tutor"
                :disabled="datosTutor.bloqueado" required />
            </div>
            <div class="col-md-6">
              <label for="correo_tutor" class="form-label text-black">Correo Electrónico:</label>
              <input v-model="datosTutor.correo" type="email" class="form-control" id="correo_tutor"
                :disabled="datosTutor.bloqueado" required />
            </div>
          </div>
        </div>

        <!-- Datos del Ponente 1 -->
        <div class="form-section mt-5">
          <h2 class="text-center section-title">Primer ponente</h2>
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="tipo_documento_ponente1" class="form-label text-black">Tipo de Documento:</label>
              <TipoDocumentoSelect v-model="datosPonente.tipo_documento"
                @tipo-documento-selected="setTipoDocumentoPonente" :disabled="datosPonente.bloqueado" required />
            </div>
            <div class="col-md-6">
              <label for="numero_documento_ponente1" class="form-label text-black">Número de Documento:</label>
              <input v-model="datosPonente.numero_documento" @blur="buscarPonentePorDocumento" type="text"
                class="form-control" id="numero_documento_ponente1" :disabled="datosPonente.bloqueado" required />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="nombres_ponente1" class="form-label text-black">Nombres:</label>
              <input v-model="datosPonente.nombres" type="text" class="form-control" id="nombres_ponente1"
                :disabled="datosPonente.bloqueado" required />
            </div>
            <div class="col-md-6">
              <label for="apellidos_ponente1" class="form-label text-black">Apellidos:</label>
              <input v-model="datosPonente.apellidos" type="text" class="form-control" id="apellidos_ponente1"
                :disabled="datosPonente.bloqueado" required />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-md-6">
              <label for="celular_ponente1" class="form-label text-black">Celular:</label>
              <input v-model="datosPonente.celular" type="text" class="form-control" id="celular_ponente1"
                :disabled="datosPonente.bloqueado" required />
            </div>
            <div class="col-md-6">
              <label for="correo_ponente1" class="form-label text-black">Correo Electrónico:</label>
              <input v-model="datosPonente.correo" type="email" class="form-control" id="correo_ponente1"
                :disabled="datosPonente.bloqueado" required />
            </div>
          </div>
          <!-- Ponente Opcional -->
          <div v-if="mostrarPonenteOpcional" class="form-section mt-5">
            <h4 class="text-center section-title">Datos del Ponente Opcional</h4>
            <div class="row mb-3">
              <div class="col-md-6">
                <label for="tipo_documento_opcional" class="form-label text-black">Tipo de Documento:</label>
                <TipoDocumentoSelect v-model="datosPonente2.tipo_documento"
                  @tipo-documento-selected="setTipoDocumentoPonente2" />
              </div>
              <div class="col-md-6">
                <label for="numero_documento_opcional" class="form-label text-black">Número de Documento:</label>
                <input v-model="datosPonente2.numero_documento" @blur="buscarPonente2PorDocumento" type="text"
                  class="form-control" id="numero_documento_opcional" />
              </div>
            </div>
            <div class="row mb-3">
              <div class="col-md-6">
                <label for="nombres_opcional" class="form-label text-black">Nombres:</label>
                <input v-model="datosPonente2.nombres" type="text" class="form-control" id="nombres_opcional" />
              </div>
              <div class="col-md-6">
                <label for="apellidos_opcional" class="form-label text-black">Apellidos:</label>
                <input v-model="datosPonente2.apellidos" type="text" class="form-control" id="apellidos_opcional" />
              </div>
            </div>
            <div class="row mb-3">
              <div class="col-md-6">
                <label for="celular_opcional" class="form-label text-black">Celular:</label>
                <input v-model="datosPonente2.celular" type="text" class="form-control" id="celular_opcional" />
              </div>
              <div class="col-md-6">
                <label for="correo_opcional" class="form-label text-black">Correo Electrónico:</label>
                <input v-model="datosPonente2.correo" type="email" class="form-control" id="correo_opcional" />
              </div>
            </div>

            <!-- Botón para eliminar Ponente Opcional -->
            <div class="text-center mt-3">
              <button type="button" @click="eliminarPonenteOpcional" class="btn btn-outline-dark btn-sm">Eliminar
                Ponente Opcional</button>
            </div>
          </div>

          <!-- Botón para agregar Ponente Opcional -->
          <div v-if="!mostrarPonenteOpcional" class="text-center mt-3">
            <button type="button" @click="agregarPonenteOpcional" class="btn btn-sm">Agregar Ponente Opcional</button>
          </div>

        </div>



        <!-- Sección Datos de los Autores -->
        <div class="form-section mt-5">
          <h2 class="text-center section-title">Nombres de los Autores</h2>
          <div class="row mb-3">
            <div class="col-md-10">
              <input v-model="nuevoAutor.nombre" type="text" class="form-control text-black"
                placeholder="Nombre del Autor" />
            </div>
            <div class="col-md-2 text-center">
              <button type="button" class="btn  btn-sm" @click="agregarAutor">Agregar</button>
            </div>
          </div>

          <ul class="list-group mb-3">
            <li v-for="(autor, index) in autores" :key="index"
              class="list-group-item d-flex justify-content-between align-items-center">
              {{ autor.nombre }}
              <button type="button" class="btn btn-sm" @click="eliminarAutor(index)">Eliminar</button>
            </li>
          </ul>
        </div>

        <!-- Botón para registrar el proyecto -->
        <div class="text-center">
          <button type="submit" class="btn ">Guardar Proyecto</button>
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
import { ObtenerUsuarioDocumento } from '@/services/UsuarioService';
import { ref } from 'vue';
import { useToastUtils } from '@/utils/toast';

export default {
  components: {
    ModalidadesSelect,
    areasConocimiento_Select,
    TipoDocumentoSelect,
    instituciones_Select,
  },
  setup(_, { router }) {
    const { showSuccessToast, showErrorToast } = useToastUtils();

    const proyectoCodigo = ref(''); // Código del proyecto generado
    const selectKey = ref(0); // Usado para forzar actualización de selectores e inputs

    const datosProyecto = ref({
      institucion_educativa: null,
      programa_academico: '',
      grupo_investigacion: '',
      linea_investigacion: '',
      nombre_semillero: '',
      modalidad: null,
      titulo: '',
      propuesta_escrita: null,
      area_conocimiento: null,
      aval: null,
    });

    const datosTutor = ref({
      tipo_documento: null,
      numero_documento: '',
      nombres: '',
      apellidos: '',
      celular: '',
      correo: '',
      bloqueado: false, // Nuevo campo para controlar el bloqueo
    });

    const datosPonente = ref({
      tipo_documento: null,
      numero_documento: '',
      nombres: '',
      apellidos: '',
      celular: '',
      correo: '',
      bloqueado: false, // Nuevo campo para controlar el bloqueo
    });

    const datosPonente2 = ref({
      tipo_documento: null,
      numero_documento: '',
      nombres: '',
      apellidos: '',
      celular: '',
      correo: '',
      bloqueado: false, // Nuevo campo para controlar el bloqueo
    });

    const mostrarPonenteOpcional = ref(false);
    const nuevoAutor = ref({ nombre: '' });
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
      datosPonente2.value = {
        tipo_documento: null,
        numero_documento: '',
        nombres: '',
        apellidos: '',
        celular: '',
        correo: '',
        bloqueado: false,
      };
    };

    const agregarAutor = () => {
      if (nuevoAutor.value.nombre.trim()) {
        autores.value.push({ ...nuevoAutor.value });
        nuevoAutor.value.nombre = '';
      } else {
        showErrorToast('El nombre del autor no puede estar vacío');
      }
    };

    const eliminarAutor = (index) => {
      autores.value.splice(index, 1);
    };

    const registrarProyecto = async () => {
      try {
        const response = await createProject(
          datosProyecto.value,
          datosTutor.value,
          datosPonente.value,
          datosPonente2.value,
          autores.value
        );

        proyectoCodigo.value = response.data.id_proyecto;
        showSuccessToast(`Proyecto registrado exitosamente, el código de identificación es: ${proyectoCodigo.value} y fue enviado al correo electronico del tutor.`);

        limpiarFormulario();

        setTimeout(() => {
          window.location.reload();
        }, 10000); // 10 segundos para refrescar la página

      } catch (error) {
        if (error.message) {
          showErrorToast(error.message);
        } else {
          showErrorToast('Error inesperado al registrar el proyecto.');
        }
      }
    };

    const buscarTutorPorDocumento = async () => {
      try {
        const tutor = await ObtenerUsuarioDocumento(datosTutor.value.numero_documento);
        if (tutor) {
          datosTutor.value.nombres = tutor.nombres;
          datosTutor.value.apellidos = tutor.apellidos;
          datosTutor.value.celular = tutor.celular;
          datosTutor.value.correo = tutor.correo;
          datosTutor.value.bloqueado = true; // Bloquear los campos si ya existe
        }
      } catch (error) {
        datosTutor.value.bloqueado = false;
      }
    };

    const buscarPonentePorDocumento = async () => {
      try {
        const ponente = await ObtenerUsuarioDocumento(datosPonente.value.numero_documento);
        if (ponente) {
          datosPonente.value.nombres = ponente.nombres;
          datosPonente.value.apellidos = ponente.apellidos;
          datosPonente.value.celular = ponente.celular;
          datosPonente.value.correo = ponente.correo;
          datosPonente.value.bloqueado = true; // Bloquear los campos si ya existe
        }
      } catch (error) {
        datosPonente.value.bloqueado = false;
      }
    };

    const buscarPonente2PorDocumento = async () => {
      try {
        const ponente2 = await ObtenerUsuarioDocumento(datosPonente2.value.numero_documento);
        if (ponente2) {
          datosPonente2.value.nombres = ponente2.nombres;
          datosPonente2.value.apellidos = ponente2.apellidos;
          datosPonente2.value.celular = ponente2.celular;
          datosPonente2.value.correo = ponente2.correo;
          datosPonente2.value.bloqueado = true; // Bloquear los campos si ya existe
        }
      } catch (error) {
        datosPonente2.value.bloqueado = false;
      }
    };

    const limpiarFormulario = () => {
      datosProyecto.value = {
        institucion_educativa: null,
        programa_academico: '',
        grupo_investigacion: '',
        linea_investigacion: '',
        nombre_semillero: '',
        modalidad: null,
        titulo: '',
        propuesta_escrita: null, // Limpiar el archivo de propuesta
        area_conocimiento: null,
        aval: null, // Limpiar el archivo de aval
      };

      datosTutor.value = {
        tipo_documento: null,
        numero_documento: '',
        nombres: '',
        apellidos: '',
        celular: '',
        correo: '',
        bloqueado: false, // Resetear el bloqueo
      };

      datosPonente.value = {
        tipo_documento: null,
        numero_documento: '',
        nombres: '',
        apellidos: '',
        celular: '',
        correo: '',
        bloqueado: false, // Resetear el bloqueo
      };

      datosPonente2.value = {
        tipo_documento: null,
        numero_documento: '',
        nombres: '',
        apellidos: '',
        celular: '',
        correo: '',
        bloqueado: false, // Resetear el bloqueo
      };

      mostrarPonenteOpcional.value = false;
      nuevoAutor.value.nombre = '';
      autores.value = [];

      document.getElementById('propuesta_escrita').value = null;
      document.getElementById('aval').value = null;

      selectKey.value += 1;
    };

    const setInstitucionEducativa = (id) => datosProyecto.value.institucion_educativa = id;
    const setModalidad = (id) => datosProyecto.value.modalidad = id;
    const setAreaConocimiento = (id) => datosProyecto.value.area_conocimiento = id;
    const setTipoDocumentoTutor = (id) => datosTutor.value.tipo_documento = id;
    const setTipoDocumentoPonente = (id) => datosPonente.value.tipo_documento = id;
    const setTipoDocumentoPonente2 = (id) => datosPonente2.value.tipo_documento = id;

    return {
      datosProyecto,
      datosTutor,
      datosPonente,
      datosPonente2,
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
      limpiarFormulario,
      selectKey,
      setInstitucionEducativa,
      setModalidad,
      setAreaConocimiento,
      setTipoDocumentoTutor,
      setTipoDocumentoPonente,
      setTipoDocumentoPonente2,
      buscarTutorPorDocumento,
      buscarPonentePorDocumento,
      buscarPonente2PorDocumento,
    };
  },
};
</script>




<style scoped>
.form-section {
  padding: 20px;

  margin-bottom: 50px;
}

.section-title {
  color: rgb(255, 182, 6);
  font-weight: bold;
  padding: 10px;
}

.section-subtitle {
  color: rgb(0, 0, 0);
  font-weight: bold;
}

.btn {
  color: rgb(255, 182, 6);
  color: #000000;
  font-size: medium;
}

.btn:hover:hover {
  background-color: rgb(0, 0, 0);
  color: white;
}

.list-group-item {
  background-color: #fff;

}
</style>
