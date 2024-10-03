<template>
  <div>
    <div class="container pt-5">
      <!-- Título -->
      <div class="row mb-5 mt-2">
        <div class="col">
          <div class="section_title text-center">
            <h1>Gestión de administradores y delegados</h1>
          </div>
        </div>
      </div>

      <!-- Tabla de admins -->
      <div class="table-responsive">
        <table id="basic-datatables" class="display table table-striped table-hover text-dark">
          <thead>
            <tr>
              <th class="bg-warning">Identificación</th>
              <th class="bg-warning">Administrador/Delegado</th>
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
                    :checked="administrador.estado === 'activo'"
                    @change="cambiarEstadoUsuario(administrador)"

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

      <PaginatorBody :totalPages="totalPaginas" @page-changed="cambiarPagina" v-if="totalPaginas > 1" />

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
                    <option value="3">Administrador</option>
                    <option value="2">Delegado</option>
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
              <!-- Tabla para mostrar el historial de actividades del administrador -->
              <table class="table table-bordered table-striped" v-if="historialAdmin.length">
                <thead>
                  <tr>
                    <th>Módulo</th>
                    <th>Acción</th>
                    <th>Fecha</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(actividad, index) in historialAdmin" :key="index">
                    <td>{{ actividad.modulo_nombre }}</td>
                    <td>{{ actividad.accion }}</td>
                    <td>{{ new Date(actividad.fecha).toLocaleString() }}</td>
                  </tr>
                </tbody>
              </table>
              <div v-else>
                <p>No se encontraron actividades.</p>
              </div>
            </div>
            <div class="modal-footer d-flex justify-content-between">
              <!-- Controles de paginación centrados -->
              <div class="mx-auto">
                <PaginatorBody 
                  :totalPages="totalPaginasHistorial" 
                  @page-changed="cambiarPaginaHistorial" 
                  v-if="totalPaginasHistorial > 1" 
                />
              </div>
              <!-- Botón de cerrar a la derecha -->
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
            </div>
          </div>
        </div>
      </div>



    </div>
  </div>
</template>


<script>
import { getAdminsByPage, updateUserRole, getActivityHistoryByAdmin, toggleUserStatus } from '../../../services/superadminService';
import { useToastUtils } from '@/utils/toast';
const { showSuccessToast, showErrorToast, showWarningToast} = useToastUtils();
import PaginatorBody from '../../UI/PaginatorBody.vue';

export default {
  data() {
    return {
      administradores: [],  // Lista de administradores obtenida de la API
      adminSeleccionado: {},  // Detalles del administrador seleccionado
      nuevoRolSeleccionado: null, // Rol seleccionado para actualizar
      paginaActual: 1,  // Página actual de la paginación
      totalPaginas: 0,  // Total de páginas disponibles
      historialAdmin: [],  // Historial de actividades del admin seleccionado
      paginaHistorialActual: 1,  // Página actual del historial
      totalPaginasHistorial: 0,  // Total de páginas del historial

    };
  },
  computed: {
    administradoresFiltrados() {
      return this.administradores;
       
    },
  },

  components: {
    PaginatorBody
  },
  methods: {
    // Obtener los administradores de la API
    async fetchAdmins() {
      try {
        const response = await getAdminsByPage(this.paginaActual);
        this.administradores = response.admins;  // Asignar los administradores
        this.totalPaginas = response.total_pages;  // Total de páginas para la paginación
      } catch (error) {
        showWarningToast('Error al obtener administradores');
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
          showSuccessToast('Rol actualizado exitosamente');
        }
      } catch (error) {
        showErrorToast(error.detail || 'Error al actualizar el rol');
      }
    },

    // Cambiar el estado del usuario
    async cambiarEstadoUsuario(admin) {
      try {
        // Guardar el estado actual del usuario
        const estadoActual = admin.estado;  // true si está activo, false si está inactivo

        // Cambiar el estado en el backend
        const actualizado = await toggleUserStatus(admin.id_usuario);  // Usar el servicio toggleUserStatus

        if (actualizado) {
          // Invertir el estado local en el objeto admin
          admin.estado = !estadoActual;  // Esto actualiza el estado después de que ha cambiado en el backend

          // Mostrar el mensaje basado en el nuevo estado
          if (admin.estado) {
            // Ahora está activo
            showSuccessToast('El estado del usuario ha sido cambiado.');
          } else {
            // Ahora está inactivo
            showSuccessToast('El estado del usuario ha sido cambiado.');
          }

          await this.fetchAdmins();  // Refrescar la lista de administradores
        }
      } catch (error) {
        showWarningToast(error.detail || 'Error al cambiar el estado del usuario');
      }
    },

    // Mostrar las acciones del administrador en el modal con paginación
    async mostrarAcciones(admin) {
      this.adminSeleccionado = admin;
      this.paginaHistorialActual = 1;  // Reiniciar la paginación al abrir el modal
      await this.fetchHistorialAdmin();
    },

    // Obtener el historial de actividades paginado
    async fetchHistorialAdmin() {
      try {
        // Llama al servicio para obtener el historial paginado
        const response = await getActivityHistoryByAdmin(this.adminSeleccionado.id_usuario, this.paginaHistorialActual);
        this.historialAdmin = response.activities;  // Asignar el historial de actividades
        this.totalPaginasHistorial = response.total_pages;  // Total de páginas del historial
      } catch (error) {
        showWarningToast(error.detail || 'Error al obtener el historial de actividades');
        this.historialAdmin = [];  // Limpiar el historial si ocurre un error
      }
    },

    // Paginación del historial de actividades
    async cambiarPaginaHistorial(pagina) {
      this.paginaHistorialActual = pagina;
      await this.fetchHistorialAdmin();
    },

    // Paginación
    cambiarPagina(pagina){
        this.paginaActual = pagina;
        this.fetchAdmins(pagina);
    },
  },
  mounted() {
    this.fetchAdmins();  // Obtener los administradores cuando se monte el componente
    this.fetchHistorialAdmin();
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
