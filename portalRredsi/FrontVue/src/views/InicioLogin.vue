<template>
  <div class="super_container">
    <!-- Header -->
    <MenuPrincipal></MenuPrincipal>
    
  </div>
  
  <FooterPrincipal />
  <!-- Modal de Login -->
  <div 
  class="modal fade"
  id="LoginModal"
  tabindex="-1"
  aria-labelledby="LoginModalLabel"
  aria-hidden="false"
>
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="LoginModalLabel">Login</h5>
        <button
          type="button"
          class="close"
          data-bs-dismiss="modal"
          aria-label="Close"
        >
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
        <!-- Formulario de login -->
        <form>
          <div class="form-group">
            <label for="email" class="text-dark">Correo electrónico</label>
            <input
              type="email"
              class="form-control"
              id="email"
              v-model="email"
              placeholder="Ingrese su correo"
            />
          </div>
          <div class="form-group mt-3">
            <label for="password" class="text-dark">Contraseña</label>
            <input
              type="password"
              class="form-control"
              id="password"
              v-model="password"
              placeholder="Contraseña"
            />
          </div>
        </form>
        <p v-if="errorMessage" class="text-danger mt-3">
          {{ errorMessage }}
        </p>
      </div>
      <div class="modal-footer">
        <button
          type="button"
          class="btn btn-secondary"
          data-bs-dismiss="modal"
        >
          Cerrar
        </button>
        <button
          type="button"
          data-bs-dismiss="modal"
          aria-label="Close"
          class="btn btn-primary custom-login-button"
          @click="handleLogin"
        >
          Iniciar Sesión
        </button>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import { ref, nextTick } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/store"; // Ajusta la ruta del store según tu estructura de proyecto
import FooterPrincipal from "../components/Footers/FooterPrincipal.vue";
import '../assets/Styles/main_styles.css'
import MenuPrincipal from "../components/Menus/MenuPrincipal.vue";
import MenuUsuarios from "../components/Menus/MenuUsuarios.vue";

export default {
  components: {
    FooterPrincipal,
    MenuPrincipal,
    MenuUsuarios
  },
  setup(){
    const authStore = useAuthStore();
    const router = useRouter();

    const user = ref(null);
    // Define las propiedades reactivas para el email, la contraseña y el mensaje de error
    const email = ref("");
    const password = ref("");
    const errorMessage = ref(null);

    // Método para manejar el login
    const handleLogin = async () => {
      try {

        await authStore.login(email.value, password.value);

        if (authStore.authError) {
        } else {
          const user = authStore.user;
          console.log(user);
          // const permissions = authStore.permissions;

          if (user?.id_rol == 2) {
            // Reemplaza '/dashboard' con la ruta deseada
            router.push("/principal-delegado");

          } else if (user?.id_rol == 1) {
            router.push("/principal-evaluador");
          }else if(user?.id_rol == 6){
            router.push('/super-admin');
          }
          
        }
      } catch (error) {
        errorMessage.value = "Error durante el login: " + error.message;
      }
    };
    
    return {
      email,
      password,
      errorMessage,
      handleLogin,
      user,
      // permissions
    };

  },
  
};
</script>
