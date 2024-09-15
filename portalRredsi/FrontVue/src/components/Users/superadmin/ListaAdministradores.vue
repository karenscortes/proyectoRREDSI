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
              <th class="bg-warning">Historial</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(administrador, index) in administradores" :key="index">
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
                  >
                  <label class="form-check-label" :for="'estado' + index"></label>
                </div>
              </td>
              <td>
                <a @click="obtenerAdministradorActual(administrador)" data-bs-toggle="modal" data-bs-target="#detalleModal">
                  <i class="far fa-eye" style="font-size: 25px;"></i>
                </a>
              </td>
              <td>
                <a @click="obtenerAdministradorActual(administrador)" data-bs-toggle="modal" data-bs-target="#historialModal">
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


    </div>
  </div>
</template>

<script>
import { getAdminsByPage } from '../../../services/superadminService';

export default {
  data() {
    return {
      administradores: [],  // Lista de administradores
      administradorActual: {},   // Administrador actual para detalles o historial
      paginaActual: 1,      // Página actual para la paginación
      totalPaginas: 0,      // Total de páginas para la paginación
    };
  },
  methods: {
    // Obtener los administradores de la página actual
    async fetchUsers() {
      try {
        // Llamada a la API para obtener los administradores
        const response = await getAdminsByPage(this.paginaActual);
        
        // Mostrar la respuesta de la API en la consola
        console.log("Respuesta completa de la API:", response);

        // Verificar si la respuesta contiene administradores
        if (response && response.admins) {
          this.administradores = response.admins;  // Asignar los administradores
          this.totalPaginas = response.total_pages; // Asignar el total de páginas
          console.log("Administradores cargados correctamente:", this.administradores);
        } else {
          alert("No se encontraron administradores.");
        }
      } catch (error) {
        alert("Error al obtener la lista de administradores");
        console.error("Error en la solicitud:", error);
      }
    },

    // Cambiar a la página anterior
    paginaAnterior() {
      if (this.paginaActual > 1) {
        this.paginaActual--;
        this.fetchUsers();
      }
    },

    // Cambiar a la página siguiente
    paginaSiguiente() {
      if (this.paginaActual < this.totalPaginas) {
        this.paginaActual++;
        this.fetchUsers();
      }
    },

    // Ir a una página específica
    irAPagina(pagina) {
      this.paginaActual = pagina;
      this.fetchUsers();
    },

    // Obtener los detalles de un administrador
    obtenerAdministradorActual(administrador) {
      this.administradorActual = administrador;
    },
  },
  mounted() {
    this.fetchUsers(); // Cargar los administradores al montar el componente
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
    color: white;
  }

  .modal-content {
    background-color: white;
  }
</style>
