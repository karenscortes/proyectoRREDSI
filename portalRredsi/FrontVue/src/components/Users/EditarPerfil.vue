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
                <button type="button" class="btn btn-warning font-weight-bold text-white" @click="showChangePasswordModal">Cambiar Contraseña</button>
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
                  <br>
                  <div class="d-inline-flex">
                    <input v-if="formData.academico.pregrado == ''" type="text" class="form-control" id="inputMasterDegree" />
                    <a v-else :href="formData.academico.pregrado.url_titulo" target="_blank"> Ver titulo</a>
                    <label class="items-center p-1 text-black">
                      <i class="fas fa-plus-circle h4"></i>
                      <input  type="file" class="d-none d-print-block" />
                    </label>
                  </div>
                </div>
                <div class="form-group col-md-4">
                  <label for="inputPostgraduateDiploma">Título de Especialización:</label>
                  <div class="d-inline-flex">
                    <input v-if="formData.academico.especializacion == ''" type="text" class="form-control" id="inputMasterDegree" />
                    <a v-else :href="formData.academico.especializacion.url_titulo" target="_blank"> Ver titulo</a>
                    <label class="items-center p-1 text-black">
                      <i class="fas fa-plus-circle h4"></i>
                      <input  type="file" class="d-none d-print-block" />
                    </label>
                  </div>
                </div>
                <div class="form-group col-md-4">
                  <label for="inputMasterDegree">Título de Maestría:</label>
                  <div class="d-inline-flex">
                    <input v-if="formData.academico.maestria == ''" type="text" class="form-control" id="inputMasterDegree" />
                    <a v-else :href="formData.academico.maestria.url_titulo" target="_blank"> Ver titulo</a>
                    <label class="items-center p-1 text-black">
                      <i class="fas fa-plus-circle h4"></i>
                      <input  type="file" class="d-none d-print-block" />
                    </label>
                  </div>
                </div>
                <div class="form-group col-md-4">
                  <label for="inputMasterDegree">Título de doctorado:</label>
                  <div class="d-inline-flex">
                    <input v-if="formData.academico.doctorado == ''" type="text" class="form-control" id="inputMasterDegree" />
                    <a v-else :href="formData.academico.doctorado.url_titulo" target="_blank"> Ver titulo</a>
                    <label class="items-center p-1 text-black">
                      <i class="fas fa-plus-circle h4"></i>
                      <input  type="file" class="d-none d-print-block" />
                    </label>
                  </div>
                </div>
                <div class="form-group col-md-4">
                  <label for="inputDocumentType">Área de conocimiento:</label>
                  <select v-model="formData.institucional.id_primer_area" id="inputDocumentType" class="form-control text-dark custom-select" required>
                    <option value="" disabled selected>Seleccione una opción</option>
                    <option :value="area.id_area_conocimiento" v-for="(area,index) in areasConocimiento" :key="index">{{ area.nombre  }}</option>
                  </select>
                </div>
                <div class="form-group col-md-4">
                  <label for="inputMasterDegree">Otra área:</label>
                  <select v-model="formData.institucional.id_segunda_area" id="inputDocumentType" class="form-control text-dark custom-select" required>
                    <option value="" disabled selected>Seleccione una opción</option>
                    <option :value="area.id_area_conocimiento" v-for="(area,index) in areasConocimiento" :key="index">{{ area.nombre  }}</option>
                  </select>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="text-center">
                <button type="button" class="btn btn-warning font-weight-bold text-white" @click="showChangePasswordModal">Guardar cambios</button>
  </div>
</template>

<script>
import { getCurrentUser,getInstitutionalDetails } from '../../services/UsuarioService';
import { useAuthStore } from '@/store';
import { getCertificatesById } from '@/services/postulacionService';
import { getAreasConocimiento } from '@/services/administradorService';

export default {
  data() {
    return {
      activeSection: 'datos_personales',
      formData: {
        personal: {
          nombres: this.user.nombres,
          apellidos: this.user.apellidos,
          tipoDocumento: '',
          numeroDocumento: this.user.documento,
          correo: this.user.correo,
        },
        institucional: {
          institucion: '',
          grupoInvestigacion: '',
          semillero: '',
          id_primer_area:'',
          id_segunda_area:'',
        },
        academico: {
          pregrado: '',
          especializacion: '',
          maestria: '',
          doctorado: '',
        },
      },
      areasConocimiento: [],
    };
  },
  setup() {
        const authStore = useAuthStore();

        const user = authStore.user;

        return {
            user,
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
  
      }
    },
    handleSubmit(section) {
      // Lógica para manejar el envío del formulario por sección (personal, institucional, académico)
      console.log(`Datos enviados de la sección: ${section}`, this.formData[section]);
    },
    async loadAcademicDegrees(){
      
      // OBTIENE LOS DATOS ACADEMICOS 
      try {
        const response_datos_academicos = await getInstitutionalDetails();

        this.formData.institucional.institucion = response_datos_academicos.data.id_institucion ;
        this.formData.institucional.grupoInvestigacion = response_datos_academicos.data.grupo_investigacion;
        this.formData.institucional.semillero = response_datos_academicos.data.semillero;
        this.formData.institucional.id_primer_area = response_datos_academicos.data.id_primera_area_conocimiento;
        this.formData.institucional.id_segunda_area = response_datos_academicos.data.id_segunda_area_conocimiento;
      } catch (error) {
        console.error(error);
      }

      // OBTIENE LOS TITULOS 
      try {
        const responseTitulos = await getCertificatesById(this.user.id_usuario);
        const titulos = responseTitulos.data;

        // Buscar los titulos disponibles y agregarlo al formData.academico.pregrado
        for (let i = 0; i < titulos.length; i++) {
          if (titulos[i].nivel == "pregrado") {
            this.formData.academico.pregrado = titulos[i];
          }else if (titulos[i].nivel == "especializacion") {
            this.formData.academico.especializacion = titulos[i];
          }else if (titulos[i].nivel == "doctorado") {
            this.formData.academico.doctorado = titulos[i];
          }else if (titulos[i].nivel == "maestria") {
            this.formData.academico.maestria = titulos[i];
          }
        }
      } catch (error) {
        console.error(error);
      }

      // OBTIENE LAS AREAS DE CONOCIMIENTO 
      try {
        const responseAreasConocimiento = await getAreasConocimiento();
        this.areasConocimiento = responseAreasConocimiento.data;
      } catch (error) {
        console.error(error);
      }
    },
  },
  mounted() {
    this.loadUserProfile();
    this.loadAcademicDegrees();
  },
};
</script>
