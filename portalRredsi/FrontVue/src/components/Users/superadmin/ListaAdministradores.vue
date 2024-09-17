<template>
  <div>
    <div class="container pt-5">
      <!-- Título -->
      <div class="row mb-5 mt-2">
        <div class="col">
          <div class="section_title text-center">
            <h1>Información administradores</h1>
          </div>
        </div>
      </div>

      <!-- Tabla de admins -->
      <div class="table-responsive">
        <table id="basic-datatables" class="display table table-striped table-hover text-dark">
          <thead>
            <tr>
              <th class="bg-warning">Identificación</th>
              <th class="bg-warning">Administrador</th>
              <th class="bg-warning">Correo</th>
              <th class="bg-warning">Teléfono</th>
              <th class="bg-warning">Estado</th>
              <th class="bg-warning">Detalle</th> 
              <th class="bg-warning">Acciones</th> 
            </tr>
          </thead>
          <tbody>
            <tr v-for="(administrador, index) in administradoresFiltrados" :key="index">
              <td style="font-size: 16px;">{{ administrador.documento }}</td>
              <td style="font-size: 16px;">{{ administrador.nombres }} {{ administrador.apellidos }}</td>
              <td style="font-size: 16px;">{{ administrador.correo }}</td>
              <td style="font-size: 16px;">{{ administrador.telefono }}</td>
              <td>
                <div class="form-check form-switch">
                  <input
                    class="form-check-input bg-warning border-warning"
                    type="checkbox"
                    role="switch"
                    :id="'estado' + index"
                    v-model="administrador.estado"
                    disabled
                  >
                  <label class="form-check-label" :for="'estado' + index"></label>
                </div>
              </td>

              <!-- Columna de acciones existente -->
              <td>
                <a @click="mostrarDetalle(administrador)" data-bs-toggle="modal" data-bs-target="#detalleAdminModal">
                  <button class="far fa-eye border border-0" style="font-size: 25px;"></button>
                </a>
              </td>

              <!-- Columna para ver acciones en el modal -->
              <td>
                <a @click="mostrarAcciones(administrador)" data-bs-toggle="modal" data-bs-target="#accionesAdminModal">
                  <button class="far fa-list-alt border border-0" style="font-size: 25px;"></button>
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

      <!-- Modal detalle administrador -->
      <div class="modal fade" id="detalleAdminModal" tabindex="-1" aria-labelledby="detalleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-lg">
          <div class="modal-content">
            <div class="modal-header bg-warning">
              <h3 class="modal-title" id="detalleModalLabel">Detalles del Administrador: {{ adminSeleccionado.nombres }} {{ adminSeleccionado.apellidos }}</h3>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body text-dark">
              <!-- Información detallada del administrador -->
              <div class="row text-dark">
                <div class="col-6">
                  <strong>Identificación:</strong>
                  <p class="text-dark">{{ adminSeleccionado.documento }}</p>
                </div>
                <div class="col-6">
                  <strong>Nombre Completo:</strong>
                  <p class="text-dark">{{ adminSeleccionado.nombres }} {{ adminSeleccionado.apellidos }}</p>
                </div>
                <div class="col-6">
                  <strong>Correo:</strong>
                  <p class="text-dark">{{ adminSeleccionado.correo }}</p>
                </div>
                <div class="col-6">
                  <strong>Teléfono:</strong>
                  <p class="text-dark">{{ adminSeleccionado.telefono }}</p>
                </div>
                <div class="col-6">
                  <strong>Estado:</strong>
                  <p class="text-dark">{{ adminSeleccionado.estado }}</p>
                </div>

                <!-- Cambiar a un select para editar el rol -->
                <div class="col-6">
                  <strong>Rol:</strong>
                  <select class="form-select" v-model="nuevoRolSeleccionado">
                    <option value="2">Administrador</option>
                    <option value="3">Delegado</option>
                  </select>
                </div>
              </div>
            </div>
            <div class="modal-footer">
              <!-- Botón para guardar cambios -->
              <button type="button" class="btn btn-primary" @click="guardarRol">Guardar</button>
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
            </div>
          </div>
        </div>
      </div>

      <!-- Modal historial administrador -->
      <div class="modal fade" id="accionesAdminModal" tabindex="-1" aria-labelledby="detalleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-lg">
          <div class="modal-content">
            <div class="modal-header bg-warning">
              <h3 class="modal-title" id="detalleModalLabel">
                Historial del Administrador: {{ adminSeleccionado.nombres }} {{ adminSeleccionado.apellidos }}
              </h3>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body text-dark">
              <!-- Historial detallado del administrador/delegado -->
              <div class="row text-dark" v-if="historialAdmin.length">
                <div class="col-12" v-for="(actividad, index) in historialAdmin" :key="index">
                  <div class="row mb-3">
                    <div class="col-4">
                      <strong>Módulo:</strong>
                      <p class="text-dark">{{ actividad.modulo_nombre }}</p>
                    </div>
                    <div class="col-4">
                      <strong>Acción:</strong>
                      <p class="text-dark">{{ actividad.accion }}</p>
                    </div>
                    <div class="col-4">
                      <strong>Fecha:</strong>
                      <p class="text-dark">{{ actividad.fecha }}</p>
                    </div>
                  </div>
                </div>
              </div>
              <div v-else>
                <p>No se encontraron actividades.</p>
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
            </div>
          </div>
        </div>
      </div>


    </div>
  </div>
</template>


<script>
import { getAdminsByPage, updateUserRole, getActivityHistoryByAdmin } from '../../../services/superadminService';

export default {
  data() {
    return {
      administradores: [],  // Lista de administradores obtenida de la API
      adminSeleccionado: {},  // Detalles del administrador seleccionado
      nuevoRolSeleccionado: null, // Rol seleccionado para actualizar
      paginaActual: 1,  // Página actual de la paginación
      totalPaginas: 0,  // Total de páginas disponibles
      historialAdmin: [],
    };
  },
  computed: {
    administradoresFiltrados() {
      return this.administradores;
       
    },
  },
  methods: {
    // Obtener los administradores de la API
    async fetchAdmins() {
      try {
        const response = await getAdminsByPage(this.paginaActual);
        this.administradores = response.admins;  // Asignar los administradores
        this.totalPaginas = response.total_pages;  // Total de páginas para la paginación
      } catch (error) {
        alert(error.detail || 'Error al obtener administradores');
      }
    },
    // Mostrar el detalle del administrador en el modal
    mostrarDetalle(admin) {
      this.adminSeleccionado = admin;
      this.nuevoRolSeleccionado = admin.id_rol;  // Asignar el rol actual al select
    },
    // Guardar el nuevo rol del administrador
    async guardarRol() {
      try {
        // Llamar al servicio para actualizar el rol
        const actualizado = await updateUserRole(this.adminSeleccionado.id_usuario, this.nuevoRolSeleccionado);

        if (actualizado) {
          // Actualizar la lista de administradores después de guardar el nuevo rol
          await this.fetchAdmins();
          alert('Rol actualizado exitosamente');
        }
      } catch (error) {
        alert(error.detail || 'Error al actualizar el rol');
      }
    },

    // Mostrar las acciones del administrador en el modal
    async mostrarAcciones(admin) {
        this.adminSeleccionado = admin;
      try {
        // Llama al servicio para obtener el historial de actividades
        const historial = await getActivityHistoryByAdmin(admin.id_usuario);
        this.historialAdmin = historial;  // Asigna el historial de actividades
     } catch (error) {
        this.historialAdmin = [];  // En caso de error, deja vacío el historial
      }
    },
    // Paginación
    paginaAnterior() {
      if (this.paginaActual > 1) {
        this.paginaActual--;
        this.fetchAdmins();
      }
    },
    paginaSiguiente() {
      if (this.paginaActual < this.totalPaginas) {
        this.paginaActual++;
        this.fetchAdmins();
      }
    },
    irAPagina(pagina) {
      this.paginaActual = pagina;
      this.fetchAdmins();
    },
  },
  mounted() {
    this.fetchAdmins();  // Obtener los administradores cuando se monte el componente
  },
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
