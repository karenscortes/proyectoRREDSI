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
              <input type="number" v-model.number="componente.calificacion" class="w-100 text-center" step="0.1" min="0" :max="componente.valor_maximo" @input="actualizarPuntajeTotal" />
            </td>
            <td class="border border-dark">
              <textarea v-model="componente.observaciones" class="text-area-full-width" rows="1" @input="actualizarCaracteres"></textarea>
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
              <input type="text" class="form-control  text-dark fs-6 form-control-sm rounded-5" readonly v-bind:value="cedulaEvaluador" />
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
    <div class="col-8 text-center py-5">
      <button @click.prevent="enviarCalificaciones" class="btn btn-warning font-weight-bold text-dark" >Calificar</button>
    </div>
  </form>
</template>
  
<script>
import { ref, computed, watch, onMounted } from 'vue';
import { obtenerDatosParaCalificarProyecto, insertarRespuestaRubrica, obtenerEtapaActual } from '../../../services/evaluadorService';
import { useAuthStore } from '@/store';

export default {
  props: {
    proyecto: {
      type: Object,
      required: true
    }
  },
  setup(props) {
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

    const obtenerDatos = async () => {
      const authStore = useAuthStore();
      const user = authStore.user;

      try {
        // Obtener datos del proyecto
        const data = await obtenerDatosParaCalificarProyecto(props.proyecto.id_proyecto, user.id_usuario);
        tituloProyecto.value = data.titulo_proyecto;
        universidadProyecto.value = data.universidad_proyecto;
        nombreEvaluador.value = data.nombre_evaluador;
        cedulaEvaluador.value = data.cedula_evaluador;
        universidadEvaluador.value = data.universidad_evaluador;
        emailEvaluador.value = data.email_evaluador;
        celularEvaluador.value = data.celular_evaluador;
        ponentesProyecto.value = data.nombres_ponentes;
        componentes.value = data.componentes;

        console.log(componentes);

        // Obtener etapa actual
        const response = await obtenerEtapaActual();
        currentEtapa.value = response.nombre_etapa;

      } catch (error) {
        console.error('Error al obtener los datos del proyecto o la etapa:', error);
      }
    };

    const actualizarPuntajeTotal = () => {
      puntajeTotal.value = componentes.value.reduce((total, componente) => {
        return total + (componente.calificacion || 0);
      }, 0);
    };

    const actualizarCaracteres = (event) => {
      const textarea = event.target;
      textarea.style.height = 'auto';
      textarea.style.height = textarea.scrollHeight + 'px';
    };

    const formateadoPuntajeTotal = computed(() => {
      return puntajeTotal.value.toFixed(1);
    });

    const enviarCalificaciones = async () => {
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

        alert('Calificaciones enviadas exitosamente');
      } catch (error) {
        console.error('Error al enviar las calificaciones:', error);
        alert('Ocurrió un error al enviar las calificaciones');
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
    };
  }
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