<template>
  <div class="container p-4 mt-5 shadow-sm rounded bg-light">
    <h2 class="text-center text-warning font-weight-bold">Formulario de Registro</h2>
    <form @submit.prevent="handleSubmit">
      <!-- Filas del formulario -->
      <div class="form-row mt-5">
        <!-- Tipo de Documento -->
        <div class="form-group col-md-6">
          <label for="tipoDocumento" class="font-weight-bold">Tipo de Documento:</label>
          <TipoDocumentoSelect 
            v-model="form.id_tipo_documento" 
            @tipo-documento-selected="setTipoDocumento"
          />
        </div>

        <!-- Número de documento -->
        <div class="form-group col-md-6">
          <label for="documento" class="font-weight-bold">N° de documento:</label>
          <input type="text" v-model="form.documento" class="form-control" id="documento" required />
        </div>
      </div>

      <div class="form-row">
        <!-- Nombres -->
        <div class="form-group col-md-6">
          <label for="nombres" class="font-weight-bold">Nombres:</label>
          <input type="text" v-model="form.nombres" class="form-control" id="nombres" required />
        </div>

        <!-- Apellidos -->
        <div class="form-group col-md-6">
          <label for="apellidos" class="font-weight-bold">Apellidos:</label>
          <input type="text" v-model="form.apellidos" class="form-control" id="apellidos" required />
        </div>
      </div>

      <div class="form-row">
        <!-- Correo -->
        <div class="form-group col-md-6">
          <label for="correo" class="font-weight-bold">Correo:</label>
          <input type="email" v-model="form.correo" class="form-control" id="correo" required />
        </div>

        <!-- Teléfono -->
        <div class="form-group col-md-6">
          <label for="celular" class="font-weight-bold">Teléfono:</label>
          <input type="text" v-model="form.celular" class="form-control" id="celular" required />
        </div>
      </div>

      <div class="form-row">
        <!-- Contraseña -->
        <div class="form-group col-md-6">
          <label for="clave" class="font-weight-bold">Contraseña:</label>
          <input type="password" v-model="form.clave" class="form-control" id="clave" required />
        </div>

        <!-- Confirmar Contraseña -->
        <div class="form-group col-md-6">
          <label for="confirmarContrasena" class="font-weight-bold">Confirmar Contraseña:</label>
          <input
            type="password"
            v-model="form.confirmarContrasena"
            class="form-control"
            id="confirmarContrasena"
            required
          />
          <div v-if="form.clave && form.confirmarContrasena && form.clave !== form.confirmarContrasena" class="text-danger">
            Las contraseñas no coinciden.
          </div>
        </div>
      </div>

      <!-- Botón de Envío -->
      <div class="text-center my-3 mb-5">
        <button type="submit" class="btn btn-warning text-dark font-weight-bold px-4">Registrar</button>
      </div>
    </form>
  </div>
</template>

<script>
import TipoDocumentoSelect from './TipoDocumentoSelect.vue'; // Importa el componente de selección
import { createUser } from '@/services/UsuarioService'; // Importa el servicio de creación de usuario
import { useToastUtils } from '@/utils/toast'; // Importa las alertas

export default {
  components: {
    TipoDocumentoSelect,
  },
  data() {
    return {
      form: this.getInitialForm(),
    };
  },
  methods: {
    getInitialForm() {
      return {
        id_tipo_documento: null, // Aquí almacenamos el ID del tipo de documento
        documento: '',           // Número de documento
        nombres: '',
        apellidos: '',
        celular: '',
        correo: '',
        clave: '',
        confirmarContrasena: '',
      };
    },
    // Método para capturar el ID del tipo de documento
    setTipoDocumento(id_tipo_documento) {
      this.form.id_tipo_documento = id_tipo_documento;
    },
    async handleSubmit() {
      const { showSuccessToast, showErrorToast } = useToastUtils(); // Obtenemos los métodos de las alertas

      // Validar si las contraseñas coinciden
      if (this.form.clave !== this.form.confirmarContrasena) {
        showErrorToast('Las contraseñas no coinciden.'); // Mostramos alerta de error
        return;
      }

      try {
        // Verifica los datos antes de enviarlos
        console.log('Datos enviados:', this.form);

        // Llamada al servicio de crear usuario
        const response = await createUser(
          this.form.id_tipo_documento, // Asegúrate de enviar el ID del tipo de documento
          this.form.documento,         // Número de documento
          this.form.nombres,           // Nombres del usuario
          this.form.apellidos,         // Apellidos del usuario
          this.form.celular,           // Celular
          this.form.correo,            // Correo
          this.form.clave              // Contraseña
        );

        showSuccessToast('Usuario creado exitosamente'); // Mostramos alerta de éxito
        console.log('Respuesta de la API:', response);

        // Limpia el formulario después de un envío exitoso
        this.form = this.getInitialForm();

      } catch (error) {
        console.error('Error al crear el usuario:', error.response ? error.response.data : error.message);
        showErrorToast('Error al crear el usuario'); // Mostramos alerta de error
      }
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 600px;
  background-color: #f8f9fa; /* Fondo claro */
  border: 1px solid #ddd; /* Borde del contenedor */
  border-radius: 10px;
}

h2 {
  color: #ffb606; /* Color amarillo del título */
}

label {
  font-weight: bold; /* Letra en negrilla */
  color: #000; /* Color negro para las etiquetas */
}

.btn-warning {
  background-color: #ffb606; /* Color del botón */
  border-color: #ffb606;
}

.btn-warning:hover {
  background-color: #e0a800; /* Hover del botón */
}

.shadow-sm {
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); /* Sombra suave */
}
</style>
