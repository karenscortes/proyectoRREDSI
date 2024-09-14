<template>
    <div>
      <div class="container pt-5">
        <!-- Título -->
        <div class="row mb-5 mt-2">
          <div class="col">
            <div class="section_title text-center">
              <h1>Información delegados</h1>
            </div>
          </div>
        </div>
  
        <!-- Buscador -->
        <div class="row mb-4 justify-content-end">
          <div class="col-8 col-sm-6">
            <div class="row justify-content-end">
              <div class="col-8">
                <input type="text" v-model="busqueda" class="form-control" placeholder="Buscar...">
              </div>
              <div class="col-4">
                <button class="btn w-100 font-weight-bold" style="background: rgb(255, 182, 6);" @click="buscarDelegado">
                  Buscar
                </button>
              </div>
            </div>
          </div>
        </div>
  
        <!-- Tabla de delegados -->
        <div class="table-responsive">
          <table id="basic-datatables" class="display table table-striped table-hover text-dark">
            <thead>
              <tr>
                <th class="bg-warning">Identificación</th>
                <th class="bg-warning">Delegado</th>
                <th class="bg-warning">Área de conocimiento</th>
                <th class="bg-warning">Institución</th>
                <th class="bg-warning">Estado</th>
                <th class="bg-warning">Detalle</th>
                <th class="bg-warning">Historial</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(delegado, index) in delegadosFiltrados" :key="index">
                <td style="font-size: 16px;">{{ delegado.identificacion }}</td>
                <td style="font-size: 16px;">{{ delegado.delegado }}</td>
                <td style="font-size: 16px;">{{ delegado.areaConocimiento }}</td>
                <td style="font-size: 16px;">{{ delegado.institucion }}</td>
                <td>
                  <div class="form-check form-switch">
                    <input
                      class="form-check-input bg-warning border-warning"
                      type="checkbox"
                      role="switch"
                      :id="'estado' + index"
                      v-model="delegado.estado"
                    >
                    <label class="form-check-label" :for="'estado' + index"></label>
                  </div>
                </td>
                <td>
                  <a @click="obtenerDelegadoActual(delegado)" data-bs-toggle="modal" data-bs-target="#detalleModal">
                    <i class="far fa-eye" style="font-size: 25px;"></i>
                  </a>
                </td>
                <td>
                  <a @click="obtenerDelegadoActual(delegado)" data-bs-toggle="modal" data-bs-target="#historialModal">
                    <i class="far fa-list-alt" style="font-size: 25px;"></i>
                  </a>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
  
        <!-- Paginación -->
        <div class="mt-2 text-dark">
          <nav aria-label="Page navigation example mb-5">
            <ul class="pagination justify-content-center">
              <li class="page-item m-1" :class="{ disabled: paginaActual === 1 }">
                <a class="page-link text-dark" href="#" @click.prevent="paginaAnterior" style="border-radius: 20px;">
                  Anterior
                </a>
              </li>
              <li
                class="page-item m-1"
                v-for="pagina in totalPaginas"
                :key="pagina"
                :class="{ active: pagina === paginaActual }"
              >
                <a class="page-link rounded-circle text-dark" href="#" @click.prevent="irAPagina(pagina)">
                  {{ pagina }}
                </a>
              </li>
              <li class="page-item m-1" :class="{ disabled: paginaActual === totalPaginas }">
                <a class="page-link text-dark" href="#" @click.prevent="paginaSiguiente" style="border-radius: 20px;">
                  Siguiente
                </a>
              </li>
            </ul>
          </nav>
        </div>
  
        <!-- Modal datos delegados -->
        <div class="modal fade" id="detalleModal" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content border border-dark border-5 rounded-5 text-dark">
              <div class="modal-header">
                <h3 class="modal-title" id="modalLabel">{{ delegadoActual.delegado }}</h3>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <div class="row mx-auto justify-content-center">
                  <div class="col-4 text-dark fw-bold">Rol:</div>
                  <div class="col-6 mb-3">
                    <select class="form-select" v-model="delegadoActual.rol">
                      <option value="" disabled>Selecciona un rol</option>
                      <option value="administrador">Administrador</option>
                      <option value="delegado">Delegado</option>
                    </select>
                  </div>
                  <div class="col-5 text-dark fw-bold">Tipo de Documento:</div>
                  <div class="col-5 border mb-3">
                    <span class="text-dark">Cédula</span>
                  </div>
                  <div class="col-5 text-dark fw-bold">Documento:</div>
                  <div class="col-5 border mb-3">
                    <span class="text-dark">{{ delegadoActual.identificacion }}</span>
                  </div>
                  <div class="col-5 text-dark fw-bold">Nombre Completo:</div>
                  <div class="col-5 border mb-3">
                    <span class="text-dark">{{ delegadoActual.delegado }}</span>
                  </div>
                  <div class="col-5 text-dark fw-bold">Área de conocimiento:</div>
                  <div class="col-5 border mb-3">
                    <span class="text-dark">{{ delegadoActual.areaConocimiento }}</span>
                  </div>
                  <div class="col-5 text-dark fw-bold">Institución:</div>
                  <div class="col-5 border mb-3">
                    <span class="text-dark">{{ delegadoActual.institucion }}</span>
                  </div>
                  <div class="col-5 text-dark fw-bold">Teléfono:</div>
                  <div class="col-5 border mb-3">
                    <span class="text-dark">{{ delegadoActual.telefono }}</span>
                  </div>
                  <div class="col-5 text-dark fw-bold">Correo:</div>
                  <div class="col-5 border mb-3">
                    <span class="text-dark">{{ delegadoActual.correo }}</span>
                  </div>
                </div>
  
                <div class="text-center mt-3">
                  <a :href="delegadoActual.urlArchivo" class="btn btn-outline-primary" target="_blank">
                    Ver Títulos
                  </a>
                </div>
  
                <div class="row text-center mt-3">
                  <div class="col-6 mb-2">
                    <button type="button" class="btn btn-secondary w-100" data-bs-dismiss="modal">
                      Cerrar
                    </button>
                  </div>
                  <div class="col-6">
                    <button type="button" class="btn btn-warning w-100" @click="guardarCambios">
                      Guardar cambios
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
  
        <!-- Modal historial de acciones -->
        <div class="modal fade" id="historialModal" tabindex="-1" aria-labelledby="historialLabel" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered modal-lg">
            <div class="modal-content border border-dark border-5 rounded-4 text-dark">
              <div class="modal-header bg-warning">
                <h3 class="modal-title mx-auto" id="historialLabel">Historial acciones {{ delegadoActual.delegado }}</h3>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body p-4">
                <div class="table-responsive">
                  <table class="table table-bordered">
                    <thead class="bg-warning">
                      <tr>
                        <th>Tipo de Acción</th>
                        <th>Módulo</th>
                        <th>Descripción</th>
                        <th>Fecha</th>
                        <th>Hora</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(actividad, index) in historialActual.actividades" :key="index">
                        <td>{{ actividad.tipoAccion }}</td>
                        <td>{{ actividad.modulo }}</td>
                        <td>{{ actividad.detalle }}</td>
                        <td>{{ actividad.fecha }}</td>
                        <td>{{ actividad.hora }}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
  
      </div>
    </div>
  </template>
  
  <script>
  import { reactive, ref, computed } from 'vue';
  
  export default {
    setup() {
      const busqueda = ref('');
      const paginaActual = ref(1);
      const elementosPorPagina = 5;
  
      const delegados = reactive([
        // ... (tu lista de delegados)
      ]);
  
      const historialActividades = reactive([
        // ... (tu lista de actividades)
      ]);
  
      const delegadoActual = reactive({
        identificacion: '',
        delegado: '',
        areaConocimiento: '',
        institucion: '',
        estado: false,
        telefono: '',
        correo: '',
        urlArchivo: '',
        rol: ''
      });
  
      const historialActual = reactive({
        actividades: []
      });
  
      const delegadosFiltrados = computed(() => {
        let filtrados = delegados.filter(delegado =>
          delegado.delegado.toLowerCase().includes(busqueda.value.toLowerCase())
        );
        const inicio = (paginaActual.value - 1) * elementosPorPagina;
        return filtrados.slice(inicio, inicio + elementosPorPagina);
      });
  
      const totalPaginas = computed(() => {
        return Math.ceil(
          delegados.filter(delegado =>
            delegado.delegado.toLowerCase().includes(busqueda.value.toLowerCase())
          ).length / elementosPorPagina
        );
      });
  
      const buscarDelegado = () => {
        paginaActual.value = 1;
      };
  
      const obtenerDelegadoActual = delegado => {
        Object.assign(delegadoActual, delegado);
  
        // Filtrar historial para el delegado seleccionado
        historialActual.actividades = historialActividades.filter(actividad =>
          actividad.modulo.includes(delegado.areaConocimiento)
        );
      };
  
      const guardarCambios = () => {
        // Lógica para guardar los cambios del delegadoActual
        console.log('Cambios guardados:', delegadoActual);
      };
  
      const paginaAnterior = () => {
        if (paginaActual.value > 1) {
          paginaActual.value--;
        }
      };
  
      const paginaSiguiente = () => {
        if (paginaActual.value < totalPaginas.value) {
          paginaActual.value++;
        }
      };
  
      const irAPagina = pagina => {
        paginaActual.value = pagina;
      };
  
      return {
        busqueda,
        delegadosFiltrados,
        delegadoActual,
        historialActual,
        buscarDelegado,
        obtenerDelegadoActual,
        guardarCambios,
        paginaActual,
        totalPaginas,
        paginaAnterior,
        paginaSiguiente,
        irAPagina
      };
    }
  };
  </script>
  
  <style scoped>
  .section_title h1 {
    display: block;
    color: #1a1a1a;
    font-weight: 500;
    padding-top: 24px;
  }
  
  .section_title h1::before {
    display: block;
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 55px;
    height: 4px;
    content: '';
    background: #ffb606;
  }
  
  .page-link {
    color: black;
  }
  
  .page-item.active .page-link {
    background-color: #ffb606;
    border-color: #ffb606;
    color: #fff;
  }

  .bg-warning {
    background-color: #ffb606;
  }
  </style>
  