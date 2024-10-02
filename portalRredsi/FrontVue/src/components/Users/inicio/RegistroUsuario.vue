<template>
  <div class="container mt-5 pt-5">
    <h2 class="text-center text-teal text-black mt-5">Formulario de Registro</h2>
    <form @submit.prevent="handleSubmit">
      <!-- Filas del formulario -->
      <div class="form-row mt-5">
        <!-- Tipo de Documento -->
        <div class="form-group col-md-6">
          <label for="tipoDocumento" class="text-black">Tipo de Documento:</label>
          <!-- Usamos el componente TipoDocumentoSelect -->
          <TipoDocumentoSelect 
            v-model="form.id_tipo_documento" 
            @tipo-documento-selected="setTipoDocumento"
          />
        </div>

        <!-- Número de documento -->
        <div class="form-group col-md-6">
          <label for="documento" class="text-black">N° de documento:</label>
          <input type="text" v-model="form.documento" class="form-control" id="documento" required />
        </div>
      </div>

      <div class="form-row">
        <!-- Nombres -->
        <div class="form-group col-md-6">
          <label for="nombres" class="text-black">Nombres:</label>
          <input type="text" v-model="form.nombres" class="form-control" id="nombres" required />
        </div>

        <!-- Apellidos -->
        <div class="form-group col-md-6">
          <label for="apellidos" class="text-black">Apellidos:</label>
          <input type="text" v-model="form.apellidos" class="form-control" id="apellidos" required />
        </div>
      </div>

      <div class="form-row">
        <!-- Correo -->
        <div class="form-group col-md-6">
          <label for="correo" class="text-black">Correo:</label>
          <input type="email" v-model="form.correo" class="form-control" id="correo" required />
        </div>

        <!-- Teléfono -->
        <div class="form-group col-md-6">
          <label for="celular" class="text-black">Teléfono:</label>
          <input type="text" v-model="form.celular" class="form-control" id="celular" required />
        </div>
      </div>

      <div class="form-row">
        <!-- Contraseña -->
        <div class="form-group col-md-6">
          <label for="clave" class="text-black">Contraseña:</label>
          <input type="password" v-model="form.clave" class="form-control" id="clave" required />
        </div>

        <!-- Confirmar Contraseña -->
        <div class="form-group col-md-6">
          <label for="confirmarContrasena" class="text-black">Confirmar Contraseña:</label>
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
        <button type="submit" class="btn" style="background: rgb(255, 182, 6)">Registrar</button>
      </div>
    </form>
  </div>
</template>

<script>
import TipoDocumentoSelect from './TipoDocumentoSelect.vue'; // Importa el componente de selección
import { createUser } from '@/services/UsuarioService'; // Importa el servicio de creación de usuario

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
      // Validar si las contraseñas coinciden
      if (this.form.clave !== this.form.confirmarContrasena) {
        alert('Las contraseñas no coinciden.');
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

        alert('Usuario creado exitosamente');
        console.log('Respuesta de la API:', response);

        // Limpia el formulario después de un envío exitoso
        this.form = this.getInitialForm();

      } catch (error) {
        console.error('Error al crear el usuario:', error.response ? error.response.data : error.message);
        alert('Error al crear el usuario');
      }
    },
  },
};
</script>

<style scoped>
.container {
  max-width: 600px;
}
</style>
