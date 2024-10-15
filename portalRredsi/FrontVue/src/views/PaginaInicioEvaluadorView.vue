<template>
    <div class="row justify-content-center">
        <div class="col-lg-8 col-10 mb-3" v-if="convocatoriaEnCurso">
            <div class="row justify-content-between align-items-center question text-center">
                <div class="col-md-8 col-sm-6 col-xs-10">
                    <h4 class=" text-dark">¿Te gustaría ser evaluador en la convocatoria actual?</h4>
                </div>
                <div class="col-md-4 col-sm-6 col-xs-10">
                    <a href="#" type="button" data-bs-toggle="modal"
                    data-bs-target="#postulacionEvaluador" class="btn w-md-100 w-xs-25 px-lg-5 py-3">Postularme</a>
                </div> 
            </div>
        </div>
        <div class="col-lg-6 col-8 text-center">
            <h4 class=" mb-5 fs-3 border-2 d-inline-block p-2 title-border-radius">Bienvenid@ al Portal RREDSI</h4>
        </div>
    </div>
    <div class="row g-5 align-items-center">
        <div class="col-lg-5 wow1 fadeIn" data-wow-delay="0.1s">
            <div class="video border">
                <button type="button" class="btn btn-play">
                  <a href="https://www.youtube.com/embed/DWRcNpR6Kdc" target="_blank"><span></span></a>
                </button>
            </div>
        </div>
        <div class="col-lg-7 wow2 fadeIn" data-wow-delay="0.3s">
            <h1 class="text-dark mb-4 display-7">Aprende Sobre las Funcionalidades y Servicios Disponibles</h1>
            <p class="text-dark mb-4">En este video se presenta una guía completa sobre las distintas opciones disponibles en el portal RREDSI. Explorarás las tareas que puedes realizar y la ubicación de cada sección para facilitar tu experiencia de uso. Además, podrás obtener información detallada sobre...
            </p>
            <div class="row mb-4">
                <div class="col-lg-6">
                    <h6 class="mb-3 text-dark"><i class="fas fa-check-circle me-2 icon"></i>Características</h6>
                    <h6 class="mb-3 text-dark"><i class="fas fa-check-circle me-2 icon"></i>Herramientas</h6>
                    <h6 class="mb-3 text-dark"><i class="fas fa-check-circle me-2 icon"></i>Limitaciones</h6>
                </div>
                <div class="col-lg-6">
                    <h6 class="mb-3 text-dark"><i class="fas fa-check-circle me-2 icon"></i>Alcance</h6>
                    <h6 class="mb-3 text-dark"><i class="fas fa-check-circle me-2 icon"></i>Requisitos</h6>
                    <h6 class="text-dark"><i class="fas fa-check-circle me-2 icon"></i>Configuraciones Predeterminadas</h6>
                </div>
            </div>
            <a href="" class="btn px-5 py-3">Más información</a>
        </div>
      </div>
      
      <!-- accordion -->
      <div class="container mt-5">
        <div class="row text-center pt-5">
          <h1 class="display-7 text-dark">Preguntas Frecuentes</h1>
          <div class="heading-line"></div>
        </div>
        <!-- ACCORDION CONTENT  -->
        <div class="row mt-5">
          <div class="col-md-12">
            <div class="accordion" id="accordionExample">
              <!-- ACCORDION ITEM 1 -->
              <div class="accordion-item shadow mb-3">
                <h2 class="accordion-header" id="headingOne">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="false" aria-controls="collapseOne">
                    ¿Por qué debo terminar mi registro para enviar una postulación?
                  </button>
                </h2>
                <div id="collapseOne" class="accordion-collapse collapse" aria-labelledby="headingOne" data-bs-parent="#accordionExample" style="">
                  <div class="accordion-body">
                    En el proceso que hace <strong>RREDSI</strong> para seleccionar a los evaluadores más aptos para calificar, se tendrá en cuenta toda la información referente a la persona, por esto es necesario que se termine el registro con los datos académicos. <strong>RREDSI</strong> necesita toda esta información para así poder repartir los proyectos inscritos entre los diferentes evaluadores que hayan hecho una postulación.
                  </div>
                </div>
              </div>
                 <!-- ACCORDION ITEM 2 -->
              <div class="accordion-item shadow mb-3">
                <h2 class="accordion-header" id="headingTwo">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                    ¿Como puedo saber en que fechas puedo calificar un proyecto?
                  </button>
                </h2>
                <div id="collapseTwo" class="accordion-collapse collapse" aria-labelledby="headingTwo" data-bs-parent="#accordionExample" style="">
                  <div class="accordion-body">
                    Podrás saber sobre las fechas de evaluación en el apartado en el apartado de <strong>Convocatoria</strong>. Ten en cuenta que en la etapa virtual, las fechas para evaluar se encontrarán en "Evaluaciones". Para la etapa presencial, las fechas para evaluar estarán en "Evento".
                  </div>
                </div>
              </div>
                 <!-- ACCORDION ITEM 3 -->
              <div class="accordion-item shadow mb-3">
                <h2 class="accordion-header" id="headingThree">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
                  ¿Que sucede si no logro calificar un proyecto en el tiempo límite?
                  </button>
                </h2>
                <div id="collapseThree" class="accordion-collapse collapse" aria-labelledby="headingThree" data-bs-parent="#accordionExample" style="">
                  <div class="accordion-body">
                    Si no llegas a calificar un proyecto a tiempo, uno de nuestros delegados de <strong>RREDSI</strong> se encargará a partir de la fecha límite de calificación. Aunque esto no afecta en ningún momento a la calificación del proyecto, será tomado en cuenta para proximas convocatorias.
                  </div>
                </div>
              </div>
                 <!-- ACCORDION ITEM 4 -->
              <div class="accordion-item shadow mb-3">
                <h2 class="accordion-header" id="headingFour">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseFour" aria-expanded="false" aria-controls="collapseFour">
                    ¿A qué se refiere con primera y segunda etapa?
                  </button>
                </h2>
                <div id="collapseFour" class="accordion-collapse collapse" aria-labelledby="headingFour" data-bs-parent="#accordionExample">
                  <div class="accordion-body">
                   La primera etapa quiere decir <strong>Virtual</strong> y la segunda quiere decir <strong>Presencial</strong>. Es de esta manera en la que se divide todo el proceso de la inscripción y calificación de los proyectos dentro de <strong>RREDSI</strong>.
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

    <!-- Modal postulacion -->
    <div class="modal fade" id="postulacionEvaluador" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content border border-dark border-5 rounded-5 text-dark">
                <div class="modal-header text-center">
                    <h3 class="modal-title mt-3 w-100 fs-4  mr-1" id="modalLabel">Formulario de Postulación</h3>
                    <button type="button" class="btn-close mr-1 mt-3" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body mt-3">
                    <div class="row justify-content-center text-start">
                        <!-- Jornadas -->
                        <div class="col-5 text-dark font-weight-bold px-3 fs-6">Participación jornada virtual:</div>
                        <div class="col-5 mb-3 px-3">
                            <select v-model="etapa_virtual" class="form-select">
                                <option value="">Seleccionar</option>
                                <option value="1">Sí</option>
                                <option value="0">No</option>
                            </select>
                        </div>

                        <div class="col-5 text-dark font-weight-bold px-3 fs-6 mt-2">Participación jornada presencial:</div>
                        <div class="col-5 mb-3 px-3 mt-2">
                            <select v-model="etapa_presencial" class="form-select">
                                <option value="">Seleccionar</option>
                                <option value="1">Sí</option>
                                <option value="0">No</option>
                            </select>
                        </div>

                       
                        <div class="col-5 text-dark font-weight-bold px-3 fs-6 mt-2"  v-if="etapa_presencial === '1'">Disponibilidad en la mañana:</div>
                        <div class="col-5 mb-3 px-3 mt-2">
                            <select v-model="jornada_manana" class="form-select" v-if="etapa_presencial === '1'">
                                <option value="">Seleccionar</option>
                                <option value="1">Sí</option>
                                <option value="0">No</option>
                            </select>
                        </div>

                        <div class="col-5 text-dark font-weight-bold px-3 fs-6 mt-2"  v-if="etapa_presencial === '1'">Disponibilidad en la tarde:</div>
                        <div class="col-5 mb-3 px-3 mt-2" v-if="etapa_presencial === '1'">
                            <select v-model="jornada_tarde" class="form-select">
                                <option value="">Seleccionar</option>
                                <option value="1">Sí</option>
                                <option value="0">No</option>
                            </select>
                        </div>
                        

                        <!-- Botón para enviar -->
                        <div class="col-12 text-center mt-4 mb-2">
                            <button @click="enviarPostulacion"  class="btn btn-warning text-white">Enviar Postulación</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
  import { insertarPostulacionEvaluador, obtenerProgramacionFases, obtenerEstadoDatosInstitucionales, obtenerEstadoPostulacion} from '../services/evaluadorService'; 
  import { useAuthStore } from '@/store';
  import { useToastUtils } from '@/utils/toast'; 
  import {onMounted, ref} from 'vue';

  const { showSuccessToast, showErrorToast, showWarningToast, showInfoToast} = useToastUtils();
  const estadoDatosInstitucionales = ref(""); 
  export default {
    data() {
      return {
        id_evaluador: null,
        etapa_virtual: '',
        etapa_presencial: '',
        jornada_manana: '',
        jornada_tarde: '',
        postulacionExitosa: false 
      };
    },
    watch: {
      // Observamos cambios en etapa_presencial para actualizar los campos de jornada
      etapa_presencial(newVal) {
        if (newVal === '1') {
          // Si selecciona asistencia presencial, restablecemos los valores de jornada a vacíos
          this.jornada_manana = '';
          this.jornada_tarde = '';
        } else {
          // Si selecciona no presencial, asignamos 0 a los campos de jornada
          this.jornada_manana = '0';
          this.jornada_tarde = '0';
        }
      }
    },
    methods: {
      async enviarPostulacion() {
        // Verificamos que los campos obligatorios estén completos
        if (this.etapa_virtual === '' || this.etapa_presencial === '') {
            showWarningToast('Por favor, complete todos los campos antes de enviar.');
            return;
        }

        // Si se selecciona la etapa presencial, validamos que los campos de jornada estén completos
        if (this.etapa_presencial === '1' && (this.jornada_manana === '' || this.jornada_tarde === '')) {
            showWarningToast('Por favor, complete los campos de disponibilidad para la jornada presencial.');
            return;
        }
        
        try {
          const authStore = useAuthStore();
          const user = authStore.user;

          const postulacionData = {
              id_evaluador: user.id_usuario,  
              etapa_virtual: parseInt(this.etapa_virtual), 
              etapa_presencial: parseInt(this.etapa_presencial),
              jornada_manana: parseInt(this.jornada_manana),
              jornada_tarde: parseInt(this.jornada_tarde)
          };

          try {
            // Realiza la llamada a la API
            const response = await obtenerEstadoDatosInstitucionales(user.id_usuario);

            // Asigna el valor al estado reactivo
            estadoDatosInstitucionales.value = response.estado_institucional_academico;
            
          } catch (error) {
            console.error("Error obteniendo los datos institucionales:", error);
          }

          if (estadoDatosInstitucionales.value === 'sin datos institucionales') {
            showWarningToast('No se ha podido enviar la postulación debido a que no se ha terminado el registro en el apartado de "Perfíl".');
            $('#postulacionEvaluador').modal('hide'); // Cierra el modal
          }else{
            // Intentar enviar la postulación
            const response = await insertarPostulacionEvaluador(postulacionData);
            console.log('Postulación exitosa', response.data);
            this.postulacionExitosa = true;  
            showSuccessToast('Postulación enviada exitosamente. Espera una respuesta en los proximos días...');
            $('#postulacionEvaluador').modal('hide'); // Cierra el modal
          }
        } catch (error) {
          const authStore = useAuthStore();
          const user = authStore.user;
          // Si el error es "Ya existe una postulación para este evaluador y convocatoria"
          if (error.response && error.response.data && error.response.data.detail === "Ya existe una postulación para este evaluador y convocatoria") {
            try {
              // Realiza la llamada a la API
              const response = await obtenerEstadoPostulacion(user.id_usuario);

              // Accede a la propiedad estado_postulacion de la respuesta
              const estadoPostulacion = response.estado_postulacion;


              // Según el estado de la postulación, definimos si se habilitan o no los apartados
              switch (estadoPostulacion) {
                  case 'aceptada':
                    showInfoToast('Tu postulación ya ha sido aceptada. Disfruta del sistema');
                    $('#postulacionEvaluador').modal('hide'); // Cierra el modal
                    break;
                  case 'pendiente':
                    showErrorToast('Ya te postulaste para esta convocatoria, espera una respuesta en los próximos días...');
                    $('#postulacionEvaluador').modal('hide'); // Cierra el modal
                      break;
                  case 'rechazada':
                    showInfoToast('Tu postulación fue rechazada. Intenta nuevamente en una proxima convocatoria');
                    $('#postulacionEvaluador').modal('hide'); // Cierra el modal
                      break;
                  
              }
            } catch (error) {
              console.error('Error obteniendo estado de postulación:', error);
            }
        
          } else {
            // Manejo de otros errores
            console.error('Error al insertar postulación:', error.message);
            showErrorToast('Error al insertar postulación');
            $('#postulacionEvaluador').modal('hide'); // Cierra el modal
          }
        }
      },
    },
    setup(){
      const convocatoriaEnCurso = ref(true);//poner en false para hacer pruebas

      //obteniendo fecha actual
      const currentDate = ref(new Date().toISOString().split('T')[0]);

      const verificar_fase_actual = async() => {
        const response = await obtenerProgramacionFases('virtual');
        if(response.data && response.data.length > 0){
          if(currentDate >= response.data[0].fecha_inicio && currentDate <= response.data[0].fecha_fin){
            convocatoriaEnCurso.value = ref(true);
          }
        }
      };

      onMounted (() =>{
        verificar_fase_actual();
      });

      return{
        convocatoriaEnCurso,
        verificar_fase_actual
      }
    },
    mounted() {
      const authStore = useAuthStore();
      this.id_evaluador = authStore.user.id_usuario;  
    }
  };
</script>


<style scoped> 
  .btn-close{
    width: 8px;
    height: 8px;
  }


  .question{
    margin-bottom: 30px;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    padding: 15px;
    border-radius: 8px;
  }
    
  .title-border-radius {
    border-radius: 10% 30%;
    color: #ffb606;
    border-bottom: 2px solid #ffb606;
  }
  
  .icon{
    color: #343a40;
    font-size: 15px
  }
  
  .border {
    border: 1px solid #dee2e6 !important;
  }
  
  .btn {
    font-weight: 600;
    transition: .5s;
    background: #ffb606;
  }
  
  .video {
    position: relative;
    height: 100%;
    min-height: 400px;
    background: linear-gradient(rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.1)), url(../assets/img/learning.png);
    background-position: center center;
    background-repeat: no-repeat;
    background-size: cover;
    border-radius: 10px;
  }
  
  .video .btn-play {
    position: absolute;
    z-index: 3;
    top: 50%;
    left: 50%;
    transform: translateX(-50%) translateY(-50%);
    box-sizing: content-box;
    display: block;
    width: 32px;
    height: 44px;
    border-radius: 50%;
    border: none;
    outline: none;
    padding: 18px 20px 18px 28px;
  }
  
  .video .btn-play:before {
    content: "";
    position: absolute;
    z-index: 0;
    left: 50%;
    top: 50%;
    transform: translateX(-50%) translateY(-50%);
    display: block;
    width: 100px;
    height: 100px;
    background: #7083f9;
    border-radius: 50%;
    animation: pulse-border 1500ms ease-out infinite;
  }
  
  .video .btn-play:after {
    content: "";
    position: absolute;
    z-index: 1;
    left: 50%;
    top: 50%;
    transform: translateX(-50%) translateY(-50%);
    display: block;
    width: 100px;
    height: 100px;
    background: #ffb606;
    border-radius: 50%;
    transition: all 200ms;
  }
  
  .video .btn-play img {
    position: relative;
    z-index: 3;
    max-width: 100%;
    width: auto;
    height: auto;
  }
  
  .video .btn-play span {
    display: block;
    position: relative;
    z-index: 3;
    width: 0;
    height: 0;
    border-left: 32px solid white;
    border-top: 22px solid transparent;
    border-bottom: 22px solid transparent;
  }
  
  @keyframes pulse-border {
    0% {
        transform: translateX(-50%) translateY(-50%) translateZ(0) scale(1);
        opacity: 1;
    }
  
    100% {
        transform: translateX(-50%) translateY(-50%) translateZ(0) scale(1.5);
        opacity: 0;
    }
  }
  
  #videoModal {
    z-index: 99999;
  }
  
  #videoModal .modal-dialog {
    position: relative;
    max-width: 800px;
    margin: 60px auto 0 auto;
  }
  
  #videoModal .modal-body {
    position: relative;
    padding: 0px;
  }
  
  #videoModal .close {
    position: absolute;
    width: 30px;
    height: 30px;
    right: 0px;
    top: -30px;
    z-index: 999;
    font-size: 30px;
    font-weight: normal;
    color: #FFFFFF;
    background: #000000;
    opacity: 1;
  }
  
  .video.border {
    border-radius: 50% 20% / 10% 40%;
  }
  
  .about {
    background: linear-gradient(rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)), url(../img/background.jpg);
    background-position: center center;
    background-repeat: no-repeat;
    background-size: cover;
  }
  /*** About End ***/
    
</style>