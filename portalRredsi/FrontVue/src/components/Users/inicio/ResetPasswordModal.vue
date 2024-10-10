<template>
    <div class="modal fade" id="ResetPasswordModal" tabindex="-1" aria-labelledby="ResetPasswordModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="ResetPasswordModalLabel">¿Recordar contraseña?</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <div class="text-center">
              <p>Simplemente ingrese su dirección de correo electrónico a continuación y le enviaremos un código para restablecer su contraseña.</p>
            </div>
  
            <!-- Fase 1: Ingreso de email para enviar código de reseteo -->
            <div v-if="!showPasswordForm">
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
                <button type="submit" class="btn btn-primary btn-user btn-block">
                  Enviar código
                </button>
              </form>
            </div>
  
            <!-- Fase 2: Introducción de código, nueva contraseña y confirmación -->
            <div v-if="showPasswordForm">
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
                <button type="submit" class="btn btn-primary btn-user btn-block">
                  Actualizar contraseña
                </button>
              </form>
            </div>
  
            <!-- Mostrar errores -->
            <div v-if="error" class="alert alert-danger mt-3">
              {{ error }}
            </div>
          </div>
        </div>
      </div>
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
  

  