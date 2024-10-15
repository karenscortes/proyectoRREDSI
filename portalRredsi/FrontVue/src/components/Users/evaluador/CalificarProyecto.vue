<template>
  <form action="#" class="row justify-content-center">
    <div class="col-lg-12 col-md-12 col-sm-12 mb-3 table-responsive">
      <table class="table display text-dark border border-dark">
        <thead class="text-center">
          <tr class="titulo_rubrica">
            <td class="col-4" style="border-top: 1px solid #000;">Titulo:</td>
            <td colspan="4" style="border-top: 1px solid #000;">
              <input type="text" class="form-control text-dark fs-6 form-control-sm rounded-5" readonly v-bind:value="tituloProyecto" />
            </td>
          </tr>
          <tr class="titulo_rubrica">
            <td class="col-4">Ponente(s):</td>
            <td colspan="4">
              <input type="text" class="form-control text-dark fs-6 form-control-sm rounded-5" readonly v-bind:value="ponentesProyecto" />
            </td>
          </tr>
          <tr class="titulo_rubrica">
            <td class="col-4">Universidad:</td>
            <td colspan="4">
              <input type="text" class="form-control text-dark fs-6 form-control-sm rounded-5" readonly v-bind:value="universidadProyecto" />
            </td>
          </tr>
          <tr class="titulo_rubrica">
            <td scope="col-4">Componentes</td>
            <td scope="col-2">Max Valor</td>
            <td scope="col-2">Calificación</td>
            <td scope="col-4">Observaciones</td>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(componente, index) in componentes" :key="index">
            <td class="border border-dark componente texto">
              <span class="text-dark font-weight-bold">{{ componente.titulo }}:</span> {{ componente.descripcion }}
            </td>
            <td class="text-center-vertical border border-dark">{{ componente.valor_maximo }}</td>
            <td class="border border-dark text-center">
              <input 
                type="number" 
                v-model.number="componente.calificacion" 
                class="w-100 text-center" 
                step="0.1" 
                min="0" 
                :max="componente.valor_maximo" 
                @input="validarCalificacion(componente, index)" 
                :disabled="disabledCalificacionObservacion"
                required
              />
            </td>
            <td class="border border-dark">
              <textarea 
                v-model="componente.observaciones" 
                class="text-area-full-width" 
                rows="1" 
                @input="actualizarCaracteres"
                :disabled="disabledCalificacionObservacion"
                required
              ></textarea>
            </td>
          </tr>
        </tbody>
        <tfoot>
          <tr class="titulo_rubrica text-center">
            <th class="border border-dark" scope="row">Puntaje total:</th>
            <td class="border border-dark">
              <input type="number" class="form-control text-dark fs-6 form-control-sm rounded-5 w-100" :value="formateadoPuntajeTotal" readonly />
            </td>
          </tr>
          <tr class="titulo_rubrica text-center">
            <th class="border border-dark" scope="row">Nombre del Evaluador:</th>
            <td class="border border-dark">
              <input type="text" class="form-control text-dark fs-6 form-control-sm rounded-5 w-100" readonly v-bind:value="nombreEvaluador" />
            </td>
            <th class="border border-dark" scope="row">Cédula:</th>
            <td class="border border-dark">
              <input type="text" class="form-control text-dark fs-6 form-control-sm rounded-5" readonly v-bind:value="cedulaEvaluador" />
            </td>
          </tr>
          <tr class="titulo_rubrica text-center">
            <th scope="row" class="border border-dark">Universidad:</th>
            <td class="border border-dark">
              <input type="text" class="form-control text-dark fs-6 form-control-sm rounded-5" readonly v-bind:value="universidadEvaluador" />
            </td>
          </tr>
          <tr class="titulo_rubrica text-center">
            <th scope="row" class="border border-dark">Email:</th>
            <td class="border border-dark">
              <input type="text" class="form-control text-dark fs-6 form-control-sm rounded-5" readonly v-bind:value="emailEvaluador" />
            </td>
            <th scope="row" class="border border-dark">Celular:</th>
            <td class="border border-dark">
              <input type="text" class="form-control text-dark fs-6 form-control-sm rounded-5" readonly v-bind:value="celularEvaluador" />
            </td>
          </tr>
        </tfoot>
      </table>
    </div>
    <div class="col-8 text-center py-5" v-if="botonCalificar == 'Activo'">
      <button @click.prevent="enviarCalificaciones" class="btn btn-warning font-weight-bold text-dark">
        Calificar
      </button>
    </div>
  </form>
</template>
  
<script>
  import { ref, computed, watch, onMounted } from 'vue';
  import { obtenerDatosParaCalificarProyecto, insertarRespuestaRubrica, obtenerEtapaActual, obtenerRubricasCalificadas, obtenerProgramacionFases } from '../../../services/evaluadorService';
  import { useAuthStore } from '@/store';
  import { useToastUtils } from '@/utils/toast'; // Importar aquí directamente

  export default {
    props: {
      proyecto: {
        type: Object,
        required: true
      }
    },
    setup(props,  { emit }) {
      const tituloProyecto = ref('');
      const universidadProyecto = ref('');
      const nombreEvaluador = ref('');
      const cedulaEvaluador = ref('');
      const universidadEvaluador = ref('');
      const emailEvaluador = ref('');
      const celularEvaluador = ref('');
      const ponentesProyecto = ref('');
      const componentes = ref([]);
      const puntajeTotal = ref(0);
      const currentEtapa = ref('');
      const botonCalificar = ref('Activo'); // Nueva variable para habilitar o no el botón de calificar


      const { showSuccessToast, showErrorToast, showWarningToast, showInfoToast} = useToastUtils();

      const verificarPeriodoCalificacion = async () => {
        try {
          // Obtener la programación de fases según la etapa actual
          const programacionFases = await obtenerProgramacionFases(currentEtapa.value);

          // Obtener la fecha actual
          const fechaActual = new Date();
          // Reseteamos horas, minutos, segundos y milisegundos de la fecha actual
          fechaActual.setHours(0, 0, 0, 0);

          // Filtrar la fase que corresponde a evaluaciones (según la etapa)
          let faseEvaluacion;
          if (currentEtapa.value === 'Virtual') {
            // Fase de evaluación para la etapa virtual es "Evaluaciones"
            faseEvaluacion = programacionFases.data.find(fase => fase.nombre_fase === 'Evaluaciones');
          } else if (currentEtapa.value === 'Presencial') {
            // Fase de evaluación para la etapa presencial es "Evento"
            faseEvaluacion = programacionFases.data.find(fase => fase.nombre_fase === 'Evento');
          }

          // Si no encontramos la fase, devolvemos false
          if (!faseEvaluacion) {
            return false;
          }

          // Convertir las fechas de inicio y fin de la fase a objetos Date
          const fechaInicioFase = new Date(faseEvaluacion.fecha_inicio);
          const fechaFinFase = new Date(faseEvaluacion.fecha_fin);

          // Reseteamos horas, minutos, segundos y milisegundos de las fechas de inicio y fin
          fechaInicioFase.setHours(0, 0, 0, 0);
          fechaFinFase.setHours(0, 0, 0, 0);

          // Verificar si la fecha actual está dentro del rango
          if (fechaActual >= fechaInicioFase && fechaActual <= fechaFinFase) {
            return true; // Está dentro del periodo de calificación
          } else {
            return false; // Fuera del periodo de calificación
          }
        } catch (error) {
          console.error('Error al verificar el periodo de calificación:', error);
          return false; // En caso de error, no permitir calificar
        }
      };

      const puedeCalificar = computed(() => {
        // Verificar si el estado es pendiente en alguna de las fases (P_virtual o P_presencial)
        return props.proyecto.estado_evaluacion === 'P_virtual' || props.proyecto.estado_evaluacion === 'P_presencial';
      });

      const disabledCalificacionObservacion = computed(() => {
        return props.proyecto.estado_evaluacion === 'C_presencial' || props.proyecto.estado_evaluacion === 'C_virtual' || botonCalificar.value==="Inactivo";
      });

      const obtenerDatos = async () => {
        const authStore = useAuthStore();
        const user = authStore.user;

        // Obtener etapa actual
        try {
          const response = await obtenerEtapaActual();
          currentEtapa.value = response.nombre_etapa;
        } catch (etapaError) {
          showErrorToast('Error al obtener la etapa actual.');
        }
        
        try {
          // Intentamos obtener los datos de las rúbricas calificadas.
          const data = await obtenerRubricasCalificadas(props.proyecto.id_proyecto, user.id_usuario, currentEtapa.value);
          
          // Si se obtienen correctamente, significa que ya hay calificaciones registradas.
          tituloProyecto.value = data.titulo_proyecto;
          universidadProyecto.value = data.universidad_proyecto;
          nombreEvaluador.value = data.nombre_evaluador;
          cedulaEvaluador.value = data.cedula_evaluador;
          universidadEvaluador.value = data.universidad_evaluador;
          emailEvaluador.value = data.email_evaluador;
          celularEvaluador.value = data.celular_evaluador;
          ponentesProyecto.value = data.nombres_ponentes;
          componentes.value = data.componentes;

          if(props.proyecto.estado_evaluacion === 'P_presencial'){
            showInfoToast("El estado del proyecto cambiará a calificado en el momento que se ingrese la respuesta del otro evaluador.");
          }

          botonCalificar.value = "Inactivo";

        } catch (error) {
          // Si hay un error, significa que no hay calificaciones registradas aún, por lo tanto, obtenemos los datos para calificar.
          try {
            const data = await obtenerDatosParaCalificarProyecto(props.proyecto.id_proyecto, user.id_usuario, currentEtapa.value);
            
            tituloProyecto.value = data.titulo_proyecto;
            universidadProyecto.value = data.universidad_proyecto;
            nombreEvaluador.value = data.nombre_evaluador;
            cedulaEvaluador.value = data.cedula_evaluador;
            universidadEvaluador.value = data.universidad_evaluador;
            emailEvaluador.value = data.email_evaluador;
            celularEvaluador.value = data.celular_evaluador;
            ponentesProyecto.value = data.nombres_ponentes;
            componentes.value = data.componentes;

          
          } catch (innerError) {
            showErrorToast('Error al obtener los datos para calificar el proyecto.');
          }
        }
      };

      const actualizarPuntajeTotal = () => {
        puntajeTotal.value = componentes.value.reduce((total, componente) => {
          return total + (componente.calificacion || 0);
        }, 0);
      };

      const validarCalificacion = (componente, index) => {
        //Si la calificacion que va a insertar es mayor al valor maximo, se pondrá el valor maximo y manda una alerta
        if (componente.calificacion > componente.valor_maximo) {
          showWarningToast(`La calificación para "${componente.titulo}" no puede exceder el valor de ${componente.valor_maximo}.`);
          componente.calificacion = componente.valor_maximo;
        }

        if (componente.calificacion < 0) {
          showWarningToast(`La calificación para "${componente.titulo}" no puede ser menor de 0.`);
          componente.calificacion = 0;
        }
        actualizarPuntajeTotal();
      };

      const actualizarCaracteres = (event) => {
        const textarea = event.target;
        textarea.style.height = 'auto';
        textarea.style.height = textarea.scrollHeight + 'px';
      };

      const formateadoPuntajeTotal = computed(() => {
        return puntajeTotal.value.toFixed(1);
      });

      const validarCalificacionesYObservaciones = () => {
        //Verificamos si hay algún campo vacío
        for (let componente of componentes.value) {
          const calificacionValida = componente.calificacion !== null && componente.calificacion !== undefined && componente.calificacion !== '';
          const observacionValida = componente.observaciones !== null && componente.observaciones !== undefined && componente.observaciones.trim() !== '';

          if (!calificacionValida || !observacionValida) {
            showWarningToast('Hay campos vacíos en las calificaciones o observaciones.');
            return false; // Si algún campo está vacío, retornamos false para indicar que la validación ha fallado
          }
        }
        return true; // Si todos los campos están completos, retornamos true
      };


      const enviarCalificaciones = async () => {

        // Validar antes campos de enviar la calificacion
        if (!validarCalificacionesYObservaciones()) {
          return;  // Si la validación falla, no se envían las calificaciones
        }

        // let verificarperiodo = await verificarPeriodoCalificacion();
        
        // if (verificarperiodo == false){
        //   showErrorToast("No puedes calificar el proyecto. Visita el apartado de 'Convocatoria' para más información y saber cuando puedes calificar los proyectos.");
        //   return;  // Si la validación falla, no se envían las calificaciones   
        // }

        try {
          const authStore = useAuthStore();
          const user = authStore.user;

          // Iterar sobre los componentes y enviar la calificación de cada uno
          for (let componente of componentes.value) {
            const respuestaData = {
              id_item_rubrica: componente.id_item_rubrica,
              id_usuario: user.id_usuario,
              id_proyecto: props.proyecto.id_proyecto,
              observacion: componente.observaciones,
              calificacion: componente.calificacion,
              calificacion_final: puntajeTotal.value,
              etapa_actual: currentEtapa.value,  // Etapa actual
            };

            await insertarRespuestaRubrica(respuestaData);
          }

          showSuccessToast('Calificación enviada exitosamente'); 
          emit('volver'); // Emite el evento también en caso de error
        
        } catch (error) {
          showErrorToast('Ocurrió un error al enviar las calificaciones');
        }
      };

      watch(() => componentes.value, actualizarPuntajeTotal, { deep: true });

      onMounted(() => {
        obtenerDatos();
      });
      

      return {
        tituloProyecto,
        universidadProyecto,
        nombreEvaluador,
        cedulaEvaluador,
        universidadEvaluador,
        emailEvaluador,
        celularEvaluador,
        ponentesProyecto,
        componentes,
        puntajeTotal,
        formateadoPuntajeTotal,
        actualizarPuntajeTotal,
        actualizarCaracteres,
        enviarCalificaciones,
        puedeCalificar,
        disabledCalificacionObservacion,
        validarCalificacion,
        botonCalificar,
      };
    },
    emits: ['volver'], 
  };
</script>

<style scoped>

  .tr_rubrica{
    border-bottom: 1px solid black;
  }

  .td_rubrica{
    border-right: 1px solid black;
  }

  .titulo_rubrica{
    font-size: 18px; font-weight: bold;
  }

  .form-control{
    height: 35px;
    border: 1px solid black;
  }

  .text-area-full-width {
    width: 100%;
    box-sizing: border-box;
    overflow-y: auto;
    resize: none;
    max-height: 70px;   
  }

  .text-center-vertical {
    text-align: center;
    vertical-align: middle; 
    height: 100%; 
  }

  .texto{

    font-size: 14px;
  }

  .btn-warning {
    width: 300px;
  }

</style>