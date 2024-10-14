<template>
  <div>
    <!-- Botón para abrir el modal -->
    <b-button v-b-modal.resetPasswordModal variant="primary">
      Restaurar contraseña
    </b-button>

    <!-- Modal -->
    <b-modal id="resetPasswordModal" title="¿Recordar contraseña?" hide-footer>
      <div class="hero_slider_container">
        <div class="back_img">
          <div class="hero_slide_container d-flex justify-content-center align-items-center">
            <div class="hero_slide_content text-center">
              <h1 class="text-gray-900 mb-2">¿Recordar contraseña?</h1>
              <p class="mb-4 text-light">
                Simplemente ingrese su dirección de correo electrónico a continuación y le enviaremos un código para restablecer su contraseña.
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- Fase 1: Ingreso de email para enviar código de reseteo -->
      <div v-if="!showPasswordForm" class="p-4">
        <form @submit.prevent="sendResetCode" class="user">
          <div class="form-group">
            <input 
              type="email" 
              class="form-control form-control-user" 
              v-model="email" 
              placeholder="Ingrese su correo electrónico" 
              required 
            />
          </div>
          <b-button type="submit" variant="primary" block>
            Enviar código
          </b-button>
        </form>
      </div>

      <!-- Fase 2: Introducción de código, nueva contraseña y confirmación -->
      <div v-if="showPasswordForm" class="p-4">
        <form @submit.prevent="resetPassword" class="user">
          <div class="form-group">
            <input 
              type="password" 
              class="form-control form-control-user" 
              v-model="newPassword" 
              placeholder="Nueva contraseña" 
              required 
            />
          </div>
          <div class="form-group">
            <input 
              type="password" 
              class="form-control form-control-user" 
              v-model="confirmPassword" 
              placeholder="Confirmar contraseña" 
              required 
            />
          </div>
          <div class="form-group">
            <input 
              type="text" 
              class="form-control form-control-user" 
              v-model="code" 
              placeholder="Ingrese el código enviado a su correo" 
              required 
            />
          </div>
          <b-button type="submit" variant="primary" block>
            Actualizar contraseña
          </b-button>
        </form>
      </div>

      <!-- Mostrar errores -->
      <div v-if="error" class="alert alert-danger mt-3">
        {{ error }}
      </div>

      <hr>
      <div class="modal-footer">
        <router-link class="small forgot-password-link" to="/">¿Ya tienes una cuenta? Iniciar sesión</router-link>
        <router-link class="small forgot-password-link" to="/register">¿No tienes una cuenta? ¡Regístrate!</router-link>
      </div>
    </b-modal>
  </div>
</template>

<script>
import { requestResetCode, changePassword } from "@/services/authService"; // Importa tus servicios de API

export default {
  data() {
    return {
      email: "",
      newPassword: "",
      confirmPassword: "",
      code: "",
      error: null,
      showPasswordForm: false,
    };
  },
  methods: {
    // Enviar código de reseteo al correo
    async sendResetCode() {
      this.error = null; // Limpiar error previo
      try {
        await requestResetCode(this.email);
        this.showPasswordForm = true; // Mostrar los inputs adicionales
      } catch (err) {
        this.error = err.response?.data?.detail || "Error enviando el código. Intente de nuevo.";
      }
    },

    // Verificar código y actualizar contraseña
    async resetPassword() {
      this.error = null; // Limpiar error previo

      // Validar que las contraseñas coincidan
      if (this.newPassword !== this.confirmPassword) {
        this.error = "Las contraseñas no coinciden.";
        return;
      }

      try {
        await changePassword(this.email, this.newPassword, this.code);
        alert("¡Contraseña actualizada con éxito!");
        this.$router.push("/login"); // Redirigir a la página de login
      } catch (err) {
        this.error = err.response?.data?.detail || "Error actualizando la contraseña. Verifique el código.";
      }
    },
  },
};
</script>

<style scoped>
.modal-footer {
  justify-content: center;
}

.forgot-password-link {
  color: black;
  text-decoration: none;
}

.forgot-password-link:hover {
  text-decoration: underline;
}

.super_container {
  width: 100%;
  overflow: hidden;
  z-index: 10;
}

.hero_slider_container {
  width: 100%;
  height: 100%;
}

.hero_slide {
  width: 100%;
  height: 100%;
}

.back_img {
  background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url(../assets/img/slider_background.jpg);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 450px;
  background-size: cover;
  background-position: center center;
}

.hero_slide_container {
  width: 100%;
  height: 65vh;
  padding-top: 15vh;
  align-content: center;
}

.hero_slide_content {
  max-width: 80%;
  padding: 10px;
}

.hero_slide_content h1 {
  font-size: 62px;
  font-weight: 400;
  color: #ffffff;
}

.hero_slide_content h1 span {
  background: #ffb606;
  padding-left: 13px;
  padding-right: 13px;
  margin-left: -12px;
  margin-right: -12px;
}
</style>
