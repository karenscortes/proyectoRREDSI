<template>
    <div class="container mt-5 pt-5">
      <h2 class="text-center text-teal text-black mt-5">Formulario de Registro</h2>
      <form @submit.prevent="handleSubmit">
        <!-- Filas del formulario -->
        <div class="form-row mt-5">
          <!-- Tipo de Documento -->
          <div class="form-group col-md-6">
            <label for="tipoDocumento" class="text-black">Tipo de Documento:</label>
            <TipoDocumentoSelect v-model="form.tipoDocumento" />
          </div>
  
          <!-- Número de Documento -->
          <div class="form-group col-md-6">
            <label for="numeroDocumento" class="text-black">N° de documento:</label>
            <input type="text" v-model="form.numeroDocumento" class="form-control" id="numeroDocumento" required />
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
            <label for="telefono" class="text-black">Teléfono:</label>
            <input type="text" v-model="form.telefono" class="form-control" id="telefono" required />
          </div>
        </div>
  
        <div class="form-row">
          <!-- Contraseña -->
          <div class="form-group col-md-6">
            <label for="contrasena" class="text-black">Contraseña:</label>
            <input type="password" v-model="form.contrasena" class="form-control" id="contrasena" required />
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
            <div v-if="form.contrasena && form.confirmarContrasena && form.contrasena !== form.confirmarContrasena" class="text-danger">
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
  import TipoDocumentoSelect from './TipoDocumentoSelect.vue';
  import { registerUser } from '@/services/UsuarioService'; // Asegúrate de que el path es correcto
  
  export default {
    components: {
      TipoDocumentoSelect,
    },
    data() {
      return {
        form: {
          tipoDocumento: '', // Almacena el ID del tipo de documento
          numeroDocumento: '',
          nombres: '',
          apellidos: '',
          correo: '',
          telefono: '',
          contrasena: '',
          confirmarContrasena: '',
        },
      };
    },
    methods: {
      async handleSubmit() {
        // Validar si las contraseñas coinciden
        if (this.form.contrasena !== this.form.confirmarContrasena) {
          alert('Las contraseñas no coinciden.');
          return;
        }
  
        try {
          // Llamar al servicio para registrar el usuario
          const response = await registerUser(
            this.form.tipoDocumento,   // ID del tipo de documento
            this.form.numeroDocumento,
            this.form.nombres,
            this.form.apellidos,
            this.form.telefono,
            this.form.correo,
            this.form.contrasena
          );
  
          alert('Usuario registrado exitosamente');
  
          // Restablecer los campos del formulario después del registro exitoso
          this.form = {
            tipoDocumento: '', // Restablecer a los valores iniciales
            numeroDocumento: '',
            nombres: '',
            apellidos: '',
            correo: '',
            telefono: '',
            contrasena: '',
            confirmarContrasena: '',
          };
        } catch (error) {
          if (error.response) {
            console.error('Error al registrar el usuario:', error.response.data);
            alert(`Error al registrar el usuario: ${error.response.data}`);
          } else {
            console.error('Error de red o de servidor:', error);
            alert('Hubo un error de red o de servidor.');
          }
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
  