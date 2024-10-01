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
                  <button type="button" class="btn btn-warning fw-bold text-white w-25" @click="showCreateConvocatoriaModal" >
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
                    <PaginatorBody :totalPages="totalPaginasConvocatoria" @page-changed="cambiarPaginaConvocatorias" v-if="totalPaginasConvocatoria > 1" />
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
                    <div class="col-sm-6">
                      <label><strong class="text-dark">Modalidad:</strong></label>
                      <select class="form-select border border-dark">
                        <option class="text-dark" value="" disabled>Seleccionar modalidad</option>
                        <option value="Presencial">Presencial</option>
                        <option value="Virtual">Virtual</option>
                      </select>
                    </div>
                    <div class="col-sm-6">
                      <label><strong class="text-dark">Nombre:</strong></label>
                      <select class="form-select border border-dark" v-model="selectedFase">
                        <option class="text-dark" value="" disabled>Seleccionar</option>
                        <option value="Inscripciones abiertas">Inscripciones abiertas</option>
                        <option value="Asignaciones">Asignaciones</option>
                        <option value="Ponencias">Ponencias</option>
                        <option value="Evaluaciones">Evaluaciones</option>
                        <option value="Publicación de resultados">Publicación de resultados</option>
                      </select>
                    </div>
                    <div class="col-sm-4 mt-4">
                      <label><strong class="text-dark">Fecha Inicio:</strong></label>
                      <input type="date" class="form-control text-dark" v-model="fechaInicioFase">
                    </div>
                    <div class="col-sm-4 mt-4">
                      <label><strong class="text-dark">Fecha Fin:</strong></label>
                      <input type="date" class="form-control text-dark" v-model="fechaFinFase">
                    </div>
                    <div class="col-sm-4 mt-5">
                      <button class="btn btn-outline-warning w-100 text-white">
                        <i class="fas fa-plus"></i> 
                        Agregar
                      </button>
                    </div>
                  </div>
                  <!-- Tabla para mostrar fases -->
                  <div class="table-responsive mt-4">
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
                              <tr v-for="fase in fases" :key="fase.id">
                                  <td>{{ fase.fase_nombre }}</td> <!-- Asegúrate de que `fase.nombre` existe -->
                                  <td>{{ fase.etapa_nombre }}</td> <!-- Asegúrate de que `fase.modalidad` existe -->
                                  <td>{{ fase.fecha_inicio }}</td> <!-- Verifica que esto coincida con la propiedad correcta -->
                                  <td>{{ fase.fecha_fin }}</td> <!-- Verifica que esto coincida con la propiedad correcta -->
                              </tr>
                          </tbody>
                      </table>
                      <PaginatorBody :totalPages="totalPaginasFase" @page-changed="cambiarPaginaFases" v-if="totalPaginasFase > 1" />
                  </div>
                </div>
              </div>


              <!-- Modal de Crear Convocatoria -->
              <div class="modal fade" id="crearConvocatoria" tabindex="-1" role="dialog">
                <div class="modal-dialog" role="document">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h2 class="modal-title">Crear Convocatoria</h2>
                      <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                      </button>
                    </div>
                    <div class="modal-body">
                      <div class="form-group">
                        <label>Nombre:</label>
                        <input type="text" class="form-control" v-model="newConvocatoria.nombre"/>
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
                        <select class="form-select" aria-label="Default select example" v-model="newConvocatoria.estado" >
                          <option selected disabled="disabled">Selecciona un estado</option>
                          <option value="en curso">En curso</option>
                          <option value="concluida">Concluida</option>
                          <option value="por publicar">Por publicar</option>
                        </select>
                      </div>
                    </div>
                    <div class="modal-footer">
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
  import { createConvocatoria, getConvocatoriasByPage, getProgramacionFasesByPage } from '../../../../services/administradorService';
  import { useToastUtils } from '@/utils/toast';
  import PaginatorBody from '../../../UI/PaginatorBody.vue';

  const { showSuccessToast, showErrorToast, showWarningToast} = useToastUtils();
  export default {
    data() {
      return {
        paginaActualConvocatoria: 1,  // Página actual de la paginación
        totalPaginasConvocatoria: 0,  // Total de páginas disponibles

        paginaActualFase: 1,
        totalPaginasFase: 0,

        convocatorias: [],
        newConvocatoria: {
          nombre: '',
          modalidad: '',
          fechaFin: '',
          estado: '',
        },
        
        fases: [],
        nombre: '',
        selectedFase: '',
        fechaInicioFase: '',
        fechaFinFase: ''
      };
    },

    components: {
        PaginatorBody
    },
    methods: {
      // Mostrar modal para crear convocatoria
      showCreateConvocatoriaModal() {
        this.resetConvocatoria();
        $('#crearConvocatoria').modal('show');
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
          console.log(this.newConvocatoria); 
          await createConvocatoria(
            this.newConvocatoria.nombre,
            this.newConvocatoria.fechaInicio,
            this.newConvocatoria.fechaFin,
            this.newConvocatoria.estado
          );
          showSuccessToast('Convocatoria registrada exitosamente');
          this.fetchConvocatorias();
          $('#crearConvocatoria').modal('hide');
        } catch (error) {
          showErrorToast(error?.detail || 'Ocurrió un error al crear la convocatoria');
        }
      },

      // Obtener las convocatorias de la API
      async fetchConvocatorias(paginaActualConvocatoria) {
        try {
          const response = await getConvocatoriasByPage(paginaActualConvocatoria);
          this.convocatorias = response.convocatorias;  // Asignar los administradores
          this.totalPaginasConvocatoria = response.data.totalPaginasConvocatoria;  // Total de páginas para la paginación
        } catch (error) {
          showWarningToast('Error al obtener convocatorias');
        }
      },
      
      async fetchFases() {
        try {
            const response = await getProgramacionFasesByPage(this.paginaActualFase);
            this.fases = response.programacion_fases; // Verifica que esto sea correcto
            this.totalPaginasFase = response.data.totalPaginasFase; // Asegúrate de que esta propiedad exista en la respuesta
        } catch (error) {
            showWarningToast('Error al obtener fases');
        }
      },


      // Paginación convocatorias
      cambiarPaginaConvocatorias(paginaConvocatoria){
          this.paginaActualConvocatoria = paginaConvocatoria;
          this.fetchConvocatorias(paginaConvocatoria);
      },

      // Paginación fases
      cambiarPaginaFases(paginaFases){
          this.paginaActualFase = paginaFases;
          this.fetchFases(paginaFases);
      },

      // Guardar todos los datos
      saveData() {
        // Implementar la lógica para guardar toda la información
      },
    }, 
    mounted() {
      this.fetchConvocatorias();
      this.fetchFases();
    },
  };
</script>
  