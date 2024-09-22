<template>
  <div class="container">
    <div class="row justify-content-center py-5">
      <div class="col-xl-10 col-lg-10 col-md-12">
        <div class="big-screen">
          <div class="row text-center">
            <div class="col-4">
              <button @click="setActiveSection('datos_personales')" class="btn btn-outline-dark w-100">
                <strong class="font-weight-bold">
                  <i class="fas fa-user-secret"></i>
                </strong>
                Datos Personales
              </button>
            </div>
            <div class="col-4">
              <button @click="setActiveSection('datos_institucionales')" class="btn btn-outline-dark w-100">
                <strong class="font-weight-bold">
                  <i class="fas fa-university"></i>
                </strong>
                Datos Institucionales
              </button>
            </div>
            <div class="col-4">
              <button @click="setActiveSection('datos_academicos')" class="btn btn-outline-dark w-100">
                <strong class="font-weight-bold">
                  <i class="fas fa-graduation-cap"></i>
                </strong>
                Datos Académicos
              </button>
            </div>
          </div>

          <!-- Sección de datos personales -->
          <div v-if="activeSection === 'datos_personales'" class="form-section mt-5" id="datos_personales">
            <div class="d-flex align-items-center justify-content-center mb-3">
              <i class="fas fa-user-secret title-icon"></i>
              <h2>Datos Personales</h2>
            </div>
            <div class="title-line"></div>
            <form @submit.prevent="handleSubmit('personal')" class="mt-4 font-weight-bold text-dark">
              <div class="form-row">
                <div class="form-group col-md-6">
                  <label for="inputName">Nombres:</label>
                  <input type="text" v-model="formData.personal.nombres" class="form-control" id="inputName" />
                </div>
                <div class="form-group col-md-6">
                  <label for="inputLastname">Apellidos:</label>
                  <input type="text" v-model="formData.personal.apellidos" class="form-control" id="inputLastname" />
                </div>
              </div>
              <div class="form-row">
                <div class="form-group col-md-6">
                  <label for="inputDocumentType">Tipo de documento:</label>
                  <select v-model="formData.personal.tipoDocumento" id="inputDocumentType" class="form-control text-dark custom-select" required>
                    <option value="" disabled selected>Seleccione una opción</option>
                    <option value="cedula">Cédula</option>
                    <option value="pasaporte">Pasaporte</option>
                    <option value="cedula_extranjeria">Cédula de extranjería</option>
                  </select>
                </div>
                <div class="form-group col-md-6">
                  <label for="inputDocumentNumber">N° de Documento:</label>
                  <input type="text" v-model="formData.personal.numeroDocumento" class="form-control" id="inputDocumentNumber" />
                </div>
              </div>
              <div class="form-group mb-5">
                <label for="inputEmail">Correo:</label>
                <input type="email" v-model="formData.personal.correo" class="form-control" id="inputEmail" placeholder="usuario@gmail.com" />
              </div>
              <div class="text-center">
                <button type="button" class="btn btn-warning font-weight-bold text-dark" @click="showChangePasswordModal">Cambiar Contraseña</button>
              </div>
            </form>
          </div>

          <!-- Sección de datos institucionales -->
          <div v-if="activeSection === 'datos_institucionales'" class="form-section mt-5" id="datos_institucionales">
            <div class="d-flex align-items-center justify-content-center mb-3">
              <i class="fas fa-university title-icon"></i>
              <h2>Datos Institucionales</h2>
            </div>
            <div class="title-line"></div>
            <form @submit.prevent="handleSubmit('institucional')" class="mt-4 font-weight-bold text-dark">
              <div class="form-row">
                <div class="form-group col-md-6">
                  <label for="inputPlaceName">Institución educativa:</label>
                  <input type="text" v-model="formData.institucional.institucion" class="form-control" id="inputPlaceName" />
                </div>
                <div class="form-group col-md-6">
                  <label for="inputResearchGroup">Grupo de Investigación:</label>
                  <input type="text" v-model="formData.institucional.grupoInvestigacion" class="form-control" id="inputResearchGroup" />
                </div>
              </div>
              <div class="form-group mb-5">
                <label for="inputResearchLab">Nombre del Semillero:</label>
                <input type="text" v-model="formData.institucional.semillero" class="form-control" id="inputResearchLab" />
              </div>
            </form>
          </div>

          <!-- Sección de datos académicos -->
          <div v-if="activeSection === 'datos_academicos'" class="form-section mt-5" id="datos_academicos">
            <div class="d-flex align-items-center justify-content-center mb-3">
              <i class="fas fa-graduation-cap title-icon"></i>
              <h2>Datos Académicos</h2>
            </div>
            <div class="title-line"></div>
            <form @submit.prevent="handleSubmit('academico')" class="mt-4 font-weight-bold text-dark">
              <div class="form-row">
                <div class="form-group col-md-4">
                  <label for="inputUndergraduateDegree">Título Pregrado:</label>
                  <div class="d-inline-flex">
                    <input type="text" v-model="formData.academico.pregrado" class="form-control" id="inputUndergraduateDegree" />
                    <label class="items-center p-1 text-black">
                      <i class="fas fa-plus-circle h4"></i>
                      <input type="file" class="d-none d-print-block" />
                    </label>
                  </div>
                </div>
                <div class="form-group col-md-4">
                  <label for="inputPostgraduateDiploma">Título de Especialización:</label>
                  <div class="d-inline-flex">
                    <input type="text" v-model="formData.academico.especializacion" class="form-control" id="inputPostgraduateDiploma" />
                    <label class="items-center p-1 text-black">
                      <i class="fas fa-plus-circle h4"></i>
                      <input type="file" class="d-none d-print-block" />
                    </label>
                  </div>
                </div>
                <div class="form-group col-md-4">
                  <label for="inputMasterDegree">Título de Maestría:</label>
                  <div class="d-inline-flex">
                    <input type="text" v-model="formData.academico.maestria" class="form-control" id="inputMasterDegree" />
                    <label class="items-center p-1 text-black">
                      <i class="fas fa-plus-circle h4"></i>
                      <input type="file" class="d-none d-print-block" />
                    </label>
                  </div>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { getCurrentUser } from '../../services/UsuarioService';

export default {
  data() {
    return {
      activeSection: 'datos_personales',
      formData: {
        personal: {
          nombres: '',
          apellidos: '',
          tipoDocumento: '',
          numeroDocumento: '',
          correo: '',
        },
        institucional: {
          institucion: '',
          grupoInvestigacion: '',
          semillero: '',
        },
        academico: {
          pregrado: '',
          especializacion: '',
          maestria: '',
        },
      },
    };
  },
  methods: {
    setActiveSection(section) {
      this.activeSection = section;
    },
    async loadUserProfile() {
      try {
        const userData = await getCurrentUser();
        // Asignar los datos recibidos al formData
        this.formData.personal.nombres = userData.nombres || '';
        this.formData.personal.apellidos = userData.apellidos || '';
        this.formData.personal.tipoDocumento = userData.tipoDocumento || '';
        this.formData.personal.numeroDocumento = userData.numeroDocumento || '';
        this.formData.personal.correo = userData.correo || '';

        this.formData.institucional.institucion = userData.institucion || '';
        this.formData.institucional.grupoInvestigacion = userData.grupoInvestigacion || '';
        this.formData.institucional.semillero = userData.semillero || '';

        this.formData.academico.pregrado = userData.pregrado || '';
        this.formData.academico.especializacion = userData.especializacion || '';
        this.formData.academico.maestria = userData.maestria || '';
      } catch (error) {
        console.error('Error al cargar el perfil del usuario:', error);
        alert('Hubo un problema al cargar los datos del usuario. Por favor, intenta nuevamente.');
      }
    },
    handleSubmit(section) {
      // Lógica para manejar el envío del formulario por sección (personal, institucional, académico)
      console.log(`Datos enviados de la sección: ${section}`, this.formData[section]);
    },
    
  },
  mounted() {
    this.loadUserProfile();
  },
};
</script>
