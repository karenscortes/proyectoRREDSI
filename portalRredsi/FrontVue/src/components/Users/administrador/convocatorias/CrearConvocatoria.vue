<template>
    <div class="container-fluid">
      <div class="container">
        <div class="row justify-content-center py-5">
          <div class="col-xl-10 col-lg-10 col-md-12">
            <div class="big-screen">
              <div class="row text-center">
                <div class="col-4 text-white">
                  <a href="#convocatorias" class="btn btn-outline-dark w-100">
                    <strong class="font-weight-bold">
                      <i class="fa fa-window-maximize"></i>
                    </strong>
                    1. Convocatorias
                  </a>
                </div>
                <div class="col-4">
                  <a href="#etapas" class="btn btn-outline-dark w-100">
                    <strong class="font-weight-bold">
                      <i class="fa fa-window-restore" aria-hidden="true"></i>
                    </strong>
                    2. Etapas
                  </a>
                </div>
                <div class="col-4">
                  <a href="#gestionar_fases" class="btn btn-outline-dark w-100">
                    <strong class="font-weight-bold">
                      <i class="fa fa-retweet" aria-hidden="true"></i>
                    </strong>
                    3. Fases
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
                  <button type="button" class="btn btn-warning fw-bold text-dark w-25" @click="showCreateConvocatoriaModal">
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
                          <th>Acciones</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="convocatoria in convocatorias" :key="convocatoria.id">
                          <td>{{ convocatoria.nombre }}</td>
                          <td>{{ convocatoria.fechaInicio }}</td>
                          <td>{{ convocatoria.fechaFin }}</td>
                          <td>{{ convocatoria.estado }}</td>
                          <td>
                            <button type="button" class="btn btn-primary" @click="editConvocatoria(convocatoria)">
                              Editar
                            </button>
                            <button type="button" class="btn btn-danger" @click="deleteConvocatoria(convocatoria)">
                              Eliminar
                            </button>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
  
              <!-- Sección Etapas -->
              <div class="form-section mt-5" id="etapas">
                <div class="d-flex align-items-center justify-content-center mb-3">
                  <i class="fa fa-window-restore title-icon"></i>
                  <h2>Etapas</h2>
                </div>
                <div class="title-line mb-4"></div>
                <div class="text-center mb-4">
                  <button type="button" class="btn btn-warning" @click="showCreateEtapaModal">
                    Crear etapa
                  </button>
                </div>
  
                <!-- Contenido de Etapas -->
                <div class="container">
                  <div class="row">
                    <div class="col-md-6">
                      <div class="modal-content text-center">
                        <div class="modal-header justify-content-center">
                          <h2 class="modal-title text-dark">Etapa virtual</h2>
                        </div>
                        <div class="modal-body">
                          <div class="row justify-content-center">
                            <div class="col-sm-8 m-4">
                              <label class="text-dark"><strong>Fecha Inicio:</strong></label>
                              <input type="date" class="form-control text-dark" v-model="etapaVirtual.fechaInicio">
                            </div>
                            <div class="col-sm-8 m-4">
                              <label class="text-dark"><strong>Fecha Fin:</strong></label>
                              <input type="date" class="form-control text-dark" v-model="etapaVirtual.fechaFin">
                            </div>
                          </div>
                        </div>
                        <div class="modal-footer justify-content-center">
                          <button class="btn btn-warning" @click="createEtapa('virtual')">Guardar</button>
                        </div>
                      </div>
                    </div>
  
                    <div class="col-md-6">
                      <div class="modal-content text-center">
                        <div class="modal-header justify-content-center">
                          <h2 class="modal-title text-dark">Etapa presencial</h2>
                        </div>
                        <div class="modal-body">
                          <div class="row justify-content-center">
                            <div class="col-sm-8 m-4">
                              <label class="text-dark"><strong>Fecha Inicio:</strong></label>
                              <input type="date" class="form-control text-dark" v-model="etapaPresencial.fechaInicio">
                            </div>
                            <div class="col-sm-8 m-4">
                              <label class="text-dark"><strong>Fecha Fin:</strong></label>
                              <input type="date" class="form-control text-dark" v-model="etapaPresencial.fechaFin">
                            </div>
                          </div>
                        </div>
                        <div class="modal-footer justify-content-center">
                          <button class="btn btn-warning" @click="createEtapa('presencial')">Guardar</button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
  
              <!-- Sección Gestionar Fases -->
              <div class="form-section mt-5" id="gestionar_fases">
                <div class="d-flex align-items-center justify-content-center mb-3">
                  <i class="fa fa-retweet title-icon"></i>
                  <h2>Gestionar fases</h2>
                </div>
                <div class="title-line mb-4"></div>
                <div class="container">
                  <div class="row mb-4">
                    <div class="col-sm-4">
                      <label><strong>Nombre:</strong></label>
                      <select class="form-select border border-dark" v-model="selectedFase">
                        <option value="" disabled>Seleccionar</option>
                        <option v-for="fase in fases" :key="fase.nombre" :value="fase.nombre">{{ fase.nombre }}</option>
                      </select>
                    </div>
                    <div class="col-sm-4">
                      <label><strong>Fecha Inicio:</strong></label>
                      <input type="date" class="form-control text-dark" v-model="fechaInicioFase">
                    </div>
                    <div class="col-sm-4">
                      <label><strong>Fecha Fin:</strong></label>
                      <input type="date" class="form-control text-dark" v-model="fechaFinFase">
                    </div>
                  </div>
  
                  <!-- Tabla de Fases -->
                  <table class="table table-bordered border border-dark text-center">
                    <thead>
                      <tr>
                        <th class="bg-warning">Fases</th>
                        <th class="bg-warning">Fecha Inicio</th>
                        <th class="bg-warning">Fecha Fin</th>
                        <th class="bg-warning">Editar</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="fase in fases" :key="fase.nombre">
                        <td>{{ fase.nombre }}</td>
                        <td>{{ fase.fechaInicio }}</td>
                        <td>{{ fase.fechaFin }}</td>
                        <td class="text-center">
                          <button type="button" class="btn" @click="editFase(fase)">
                            <i class="fas fa-edit"></i>
                          </button>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
  
              <!-- Botón de Guardar -->
              <div class="text-center mt-4">
                <button type="button" class="btn btn-primary text-dark" @click="saveData">Guardar</button>
              </div>
  
              <!-- Modal de Crear Convocatoria -->
              <div class="modal fade" id="crearConvocatoria" tabindex="-1" role="dialog">
                <div class="modal-dialog" role="document">
                  <div class="modal-content">
                    <div class="modal-header">
                      <h5 class="modal-title">Crear Convocatoria</h5>
                      <button type="button" class="close" data-dismiss="modal" aria-label="Close">
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
  export default {
    data() {
      return {
        convocatorias: [], // Array para almacenar convocatorias
        newConvocatoria: {
          nombre: '',
          fechaInicio: '',
          fechaFin: ''
        },
        etapas: [], // Array para etapas
        etapaVirtual: {
          fechaInicio: '',
          fechaFin: ''
        },
        etapaPresencial: {
          fechaInicio: '',
          fechaFin: ''
        },
        fases: [], // Array para fases
        selectedFase: '',
        fechaInicioFase: '',
        fechaFinFase: ''
      };
    },
    methods: {
      // Mostrar modal para crear convocatoria
      showCreateConvocatoriaModal() {
        $('#crearConvocatoria').modal('show');
      },
  
      // Crear nueva convocatoria
      createConvocatoria() {
        this.convocatorias.push({ ...this.newConvocatoria });
        this.newConvocatoria = { nombre: '', fechaInicio: '', fechaFin: '' };
        $('#crearConvocatoria').modal('hide');
      },
  
      // Editar convocatoria
      editConvocatoria(convocatoria) {
        // Lógica para editar convocatoria
      },
  
      // Eliminar convocatoria
      deleteConvocatoria(convocatoria) {
        // Lógica para eliminar convocatoria
      },
  
      // Crear nueva etapa
      createEtapa(tipo) {
        const nuevaEtapa = tipo === 'virtual' ? { ...this.etapaVirtual } : { ...this.etapaPresencial };
        this.etapas.push(nuevaEtapa);
        if (tipo === 'virtual') {
          this.etapaVirtual = { fechaInicio: '', fechaFin: '' };
        } else {
          this.etapaPresencial = { fechaInicio: '', fechaFin: '' };
        }
      },
  
      // Editar fase
      editFase(fase) {
        // Lógica para editar fase
      },
  
      // Guardar datos
      saveData() {
        // Lógica para guardar todos los datos
      }
    }
  };
  </script>
  