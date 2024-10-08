<template>
  <div class="container-fluid">
    <div class="container">
      <div class="row justify-content-center py-5">
        <div class="col-xl-10 col-lg-10 col-md-12">
          <div class="big-screen">
            <div class="row text-center">
              <div class="col-6 text-white">
                <a href="#convocatorias" class="btn btn-outline-dark w-100">
                  <i class="fa fa-window-maximize"></i>
                  <strong class="font-weight-bold text-white">
                    1. Convocatorias
                  </strong>
                </a>
              </div>
              <div class="col-6">
                <a href="#gestionar_fases" class="btn btn-outline-dark w-100">
                  <i class="fa fa-retweet" aria-hidden="true"></i>
                  <strong class="font-weight-bold text-white">
                    2. Fases y etapas
                  </strong>
                </a>
              </div>
            </div>

            <!-- Sección Convocatorias -->
            <div class="form-section mt-5 w-100" id="convocatorias">
              <div class="d-flex align-items-start justify-content-center mb-3">
                <i class="fa fa-window-maximize title-icon"></i>
                <h2>Convocatorias</h2>
              </div>
              <div class="title-line"></div>
              <div class="text-left mt-3">
                <button v-if="!convocatoriaActiva" type="button" class="btn btn-warning fw-bold text-white w-25" @click="showCreateConvocatoriaModal">
                  Crear convocatoria
                </button>
              </div>
              <div class="row mt-5">
                <div class="col-12">
                  <table class="table table-striped">
                    <thead>
                      <tr>
                        <th>Nombre</th>
                        <th>Fecha de inicio</th>
                        <th>Fecha de fin</th>
                        <th>Estado</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="convocatoria in convocatorias" :key="convocatoria.id">
                        <td>{{ convocatoria.nombre }}</td>
                        <td>{{ convocatoria.fecha_inicio }}</td>
                        <td>{{ convocatoria.fecha_fin }}</td>
                        <td>{{ convocatoria.estado }}</td>
                      </tr>
                    </tbody>
                  </table>
                  <!-- Paginador -->
                  <PaginatorBody :totalPages="totalPaginasConvocatoria" @page-changed="cambiarPaginaConvocatoria" v-if="totalPaginasConvocatoria > 1" />
                </div>
              </div>
            </div>

            <!-- Sección Gestionar Fases -->
            <div class="form-section mt-5" id="gestionar_fases">
              <div class="d-flex align-items-center justify-content-center mb-3">
                <i class="fa fa-retweet title-icon"></i>
                <h2>Gestionar fases y etapas</h2>
              </div>
              <div class="title-line mb-4"></div>
              <div class="container">
                <div class="row mb-4">
                  <!-- Tabla para agregar fases -->
                  <div class="col-sm-12">
                    <table class="table table-striped">
                      <thead class="thead-warning">
                        <tr>
                          <th scope="col">Fase</th>
                          <th scope="col">Fecha Inicio</th>
                          <th scope="col">Fecha Fin</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="fase in programacionFases" :key="fase.idFase">
                          <td>{{ fase.nombre }} {{ fase.etapaNombre }}</td>
                          <td>
                            <input type="date" class="form-control text-dark" v-model="fase.fechaInicio" />
                          </td>
                          <td>
                            <input type="date" class="form-control text-dark" v-model="fase.fechaFin" />
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>

                  <!-- Botón para crear la programación de fases -->
                  <div class="col-sm-12 mt-4">
                    <button class="btn btn-outline-warning w-100 text-white" @click="crearProgramacionFases">
                      <i class="fas fa-plus"></i> Crear programación de fases
                    </button>
                  </div>
                </div>

                <!-- Tabla para mostrar las fases existentes -->
                <div class="table-responsive mt-4">
                  <div v-if="convocatoriaActiva">
                    <h2>Convocatoria Activa: {{ convocatoriaActiva.nombre }}</h2>
                  </div>
                  <table class="table table-striped">
                    <thead class="thead-warning">
                      <tr>
                        <th scope="col">Nombre</th>
                        <th scope="col">Modalidad</th>
                        <th scope="col">Fecha Inicio</th>
                        <th scope="col">Fecha Fin</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="fase in fases" :key="fase.id_programacion_fase">
                        <td>{{ fase.fase_nombre }}</td>
                        <td>{{ fase.etapa_nombre }}</td>
                        <td>{{ fase.fecha_inicio }}</td>
                        <td>{{ fase.fecha_fin }}</td>
                      </tr>
                    </tbody>
                  </table>
                  <PaginatorBody :totalPages="totalPaginasFases" @page-changed="cambiarPaginaFases" v-if="totalPaginasFases > 1" />
                </div>
              </div>
            </div>

            <!-- Modal de Crear Convocatoria -->
            <div v-if="showModal" class="modal fade show d-block" tabindex="-1" role="dialog">
              <div class="modal-dialog" role="document">
                <div class="modal-content">
                  <div class="modal-header">
                    <h2 class="modal-title">Crear Convocatoria</h2>
                    <button type="button" class="close" @click="hideModal" aria-label="Close">
                      <span aria-hidden="true">&times;</span>
                    </button>
                  </div>
                  <div class="modal-body">
                    <div class="form-group">
                      <label>Nombre:</label>
                      <input type="text" class="form-control" v-model="newConvocatoria.nombre" />
                    </div>
                    <div class="form-group">
                      <label>Fecha Inicio:</label>
                      <input type="date" class="form-control" v-model="newConvocatoria.fechaInicio" />
                    </div>
                    <div class="form-group">
                      <label>Fecha Fin:</label>
                      <input type="date" class="form-control" v-model="newConvocatoria.fechaFin" />
                    </div>
                    <div class="form-group">
                      <label>Estado:</label>
                      <select class="form-select" aria-label="Default select example" v-model="newConvocatoria.estado">
                        <option selected disabled="disabled">Selecciona un estado</option>
                        <option value="en curso">En curso</option>
                        <option value="concluida">Concluida</option>
                        <option value="por publicar">Por publicar</option>
                      </select>
                    </div>
                    <!-- Validaciones de fecha -->
                    <div v-if="errorMessage" class="alert alert-danger" role="alert">
                      {{ errorMessage }}
                    </div>
                  </div>
                  <div class="modal-footer d-flex justify-content-center">
                    <button type="button" class="btn btn-primary" @click="createConvocatoria">Crear</button>
                  </div>
                </div>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { createConvocatoria, getConvocatoriasByPage, getProgramacionFasesByPage, programarFases, getConvocatoriaEnCurso } from '../../../../services/administradorService';
import { useToastUtils } from '@/utils/toast';
import PaginatorBody from '../../../UI/PaginatorBody.vue';

const { showSuccessToast, showErrorToast, showWarningToast } = useToastUtils();

export default {
  data() {
    return {
      showModal: false,  // Control del estado del modal
      totalPaginasConvocatoria: 0,
      PaginarActualConvocatoria: 1,

      totalPaginasFases: 0,
      PaginarActualFases: 1,

      convocatorias: [],
      newConvocatoria: {
        nombre: '',
        fechaInicio: '',
        fechaFin: '',
        estado: '',
      },

      fases: [],
      convocatoriaActiva: null,  // Inicializa como null para verificar si hay una activa
      errorMessage: '',

      // Fases con ID y modalidad a programar
      programacionFases: [
        { idFase: 1, idEtapa: 2, nombre: 'Inscripciones abiertas (Virtual)', fechaInicio: '', fechaFin: '' },
        { idFase: 2, idEtapa: 2, nombre: 'Asignaciones (Virtual)', fechaInicio: '', fechaFin: '' },
        { idFase: 3, idEtapa: 2, nombre: 'Evaluaciones (Virtual)', fechaInicio: '', fechaFin: '' },
        { idFase: 4, idEtapa: 2, nombre: 'Publicación de Resultados (Virtual)', fechaInicio: '', fechaFin: '' },
        { idFase: 5, idEtapa: 1, nombre: 'Asignaciones (Presencial)', fechaInicio: '', fechaFin: '' },
        { idFase: 7, idEtapa: 1, nombre: 'Publicación de Resultados (Presencial)', fechaInicio: '', fechaFin: '' },
        { idFase: 8, idEtapa: 1, nombre: 'Evento (Presencial)', fechaInicio: '', fechaFin: '' },
      ],
    };
  },

  components: {
    PaginatorBody
  },

  methods: {
    // Mostrar modal para crear convocatoria
    showCreateConvocatoriaModal() {
      this.resetConvocatoria();
      this.showModal = true; // Mostrar modal
    },

    // Ocultar modal
    hideModal() {
      this.showModal = false; // Ocultar modal
    },

    // Resetear el formulario de convocatoria
    resetConvocatoria() {
      this.newConvocatoria = {
        nombre: '',
        fechaInicio: '',
        fechaFin: '',
        estado: ''
      };
    },

    // Validar campos de convocatoria
    validarCamposConvocatoria() {
      const { nombre, fechaInicio, fechaFin, estado } = this.newConvocatoria;

      // Verificar que todos los campos estén completos
      if (!nombre || !fechaInicio || !fechaFin || !estado) {
        showWarningToast('Todos los campos son obligatorios');
        return false;
      }

      // Validar que la fecha de inicio no sea mayor que la fecha de fin
      const fechaInicioObj = new Date(fechaInicio);
      const fechaFinObj = new Date(fechaFin);

      if (fechaInicioObj > fechaFinObj) {
        showWarningToast('La fecha de inicio no puede ser mayor que la fecha de fin');
        return false;
      }

      return true;
    },

    // Crear nueva convocatoria
    async createConvocatoria() {
      if (!this.validarCamposConvocatoria()) return; // Validar antes de crear

      try {
        await createConvocatoria(
          this.newConvocatoria.nombre,
          this.newConvocatoria.fechaInicio,
          this.newConvocatoria.fechaFin,
          this.newConvocatoria.estado
        );
        showSuccessToast('Convocatoria registrada exitosamente');
        this.fetchConvocatorias();
        this.hideModal(); // Ocultar modal al terminar
      } catch (error) {
        showErrorToast(error?.detail || 'Ocurrió un error al crear la convocatoria');
      }
    },

    // Obtener las convocatorias de la API
    async fetchConvocatorias(pagina_actual) {
      try {
        const respuesta = await getConvocatoriasByPage(pagina_actual);
        this.convocatorias = respuesta.convocatorias;  // Asignar las convocatorias
        this.totalPaginasConvocatoria = respuesta.total_pages;  // Total de páginas para la paginación
      } catch (error) {
        showWarningToast('Error al obtener convocatorias');
      }
    },

    async fetchFases(pagina_actual) {
      try {
        const respuesta = await getProgramacionFasesByPage(pagina_actual);
        this.fases = respuesta.programacion_fases;
        this.totalPaginasFases = respuesta.total_pages;
      } catch (error) {
        showWarningToast('Error al obtener fases');
      }
    },

    async obtenerConvocatoriaActiva() {
      try {
        const convocatoria = await getConvocatoriaEnCurso();
        this.convocatoriaActiva = convocatoria; // Almacena la convocatoria activa
      } catch (error) {
        showWarningToast('Error al obtener la convocatoria activa');
      }
    },

    async crearProgramacionFases() {
      await this.obtenerConvocatoriaActiva(); // Obtener convocatoria activa antes de programar

      // Verifica si la convocatoria activa existe
      if (!this.convocatoriaActiva || !this.convocatoriaActiva.id_convocatoria) {
        showWarningToast('No hay una convocatoria activa para programar fases.');
        return;
      }

      // Obtener las fases programadas desde el backend
      let fasesProgramadas = [];
      try {
        fasesProgramadas = await this.obtenerFasesProgramadas(); // Llama al servicio de fases programadas
      } catch (error) {
        showErrorToast('Error al obtener las fases programadas.');
        return; // Salir del método si ocurre un error
      }

      // Comprobar si alguna de las fases que se quiere programar ya está programada
      const faseYaProgramada = this.programacionFases.some(nuevaFase => 
        fasesProgramadas.some(faseProgramada => 
          faseProgramada.idFase === nuevaFase.idFase && 
          faseProgramada.fechaInicio === nuevaFase.fechaInicio && 
          faseProgramada.fechaFin === nuevaFase.fechaFin
        )
      );

      if (faseYaProgramada) {
        showWarningToast('Una o más fases ya están programadas. Por favor, revise las fechas.');
        return; // Salir del método si alguna fase ya está programada
      }

      const payload = this.programacionFases
        .filter(fase => fase.fechaInicio && fase.fechaFin) // Filtrar fases con fechas válidas
        .map(fase => ({
          id_fase: fase.idFase,  // Cambiar idFase a id_fase
          id_convocatoria: this.convocatoriaActiva.id_convocatoria,  // Incluir id_convocatoria dentro de cada objeto fase
          fecha_inicio: fase.fechaInicio,  // Cambiar fechaInicio a fecha_inicio
          fecha_fin: fase.fechaFin  // Cambiar fechaFin a fecha_fin
      }));


      console.log(JSON.stringify(payload, null, 2));  // Mostrar el payload en formato JSON


      console.log('Payload que se envía:', payload); // Agrega esto

      try {
        await programarFases(payload);
        showSuccessToast('Programación de fases creada exitosamente.');
        this.fetchFases(this.PaginarActualFases); // Refrescar lista de fases
      } catch (error) {
        showErrorToast('Error al programar las fases.');
      }
    },


    async obtenerFasesProgramadas(page = 1, pageSize = 100) {
      try {
        const response = await getProgramacionFasesByPage(page, pageSize);
        console.log('Respuesta completa del backend:', response); // Ver la estructura completa de la respuesta

        // Verificar si el array 'programacion_fases' está presente y es válido
        if (!response || !Array.isArray(response.programacion_fases)) {
          throw new Error('La respuesta no contiene un array válido de programaciones de fases.');
        }
        
        return response.programacion_fases;  // Devolver el array de fases programadas
      } catch (error) {
        console.error('Error al obtener fases programadas:', error);
        throw error; // Propagar el error para que sea manejado arriba
      }
    },





    cambiarPaginaConvocatoria(pageNumber) {
      this.PaginarActualConvocatoria = pageNumber;
      this.fetchConvocatorias(pageNumber);
    },

    cambiarPaginaFases(pageNumber) {
      this.PaginarActualFases = pageNumber;
      this.fetchFases(pageNumber);
    },
  },

  mounted() {
    this.fetchConvocatorias(this.PaginarActualConvocatoria);
    this.obtenerConvocatoriaActiva(); // Obtiene la convocatoria activa al montar el componente
    this.fetchFases(this.PaginarActualFases);
  }
};
</script>


