<template>
    <div class="super_container">
        <!-- Header -->
        <MenuPrincipal @component-selected="changeComponent" />
    </div>

    <!-- Mostrar la imagen de fondo en las otras opciones del menú -->
    <div v-if="componente == 'Registrar Proyecto' || componente == 'Evaluadores' || componente == 'Consultar Proyecto'" class="hero_slide">
        <div class="back_img"></div>
        <div class="hero_slide_container d-flex flex-column align-items-center justify-content-center">
            <div class="hero_slide_content text-center">
                <h1>{{componente}}</h1>
            </div>
        </div>
    </div>
    <div class="cont-slides" v-else>
        <Carrusel />
    </div>

    <div class="container">
        <ComponenteDinamico :currentComponent="currentComponent" />
    </div>

    <FooterPrincipal />

    <!-- Modal de Login -->
<div class="modal fade" id="LoginModal" tabindex="-1" aria-labelledby="LoginModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <!-- Hacer la palabra Login o ¿Recordar contraseña? más grande y del color del botón -->
                <h5 class="modal-title title-styling" id="LoginModalLabel">{{ showResetPasswordForm ? '¿Recordar contraseña?' : 'Login' }}</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close" @click="resetModalState">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="modal-body">
                <!-- Formulario de login -->
                <div v-if="!showResetPasswordForm">
                    <form>
                        <div class="form-group">
                            <label for="email" class="text-dark font-weight-bold">Correo electrónico</label>
                            <input type="email" class="form-control" id="email" v-model="email" placeholder="Ingrese su correo" />
                        </div>
                        <div class="form-group mt-3">
                            <label for="password" class="text-dark font-weight-bold">Contraseña</label>
                            <input type="password" class="form-control" id="password" v-model="password" placeholder="Contraseña" />
                        </div>
                    </form>

                    <!-- Enlace de "Se te olvidó la contraseña" más grande y en negrilla -->
                    <div class="text-center mt-3">
                        <a href="#" class="forgot-password-link" @click="openResetPasswordModal">¿Has olvidado tu contraseña?</a>
                    </div>

                </div>

                <!-- Formulario de restauración de contraseña -->
                <div v-if="showResetPasswordForm">
                    <div v-if="!showPasswordForm">
                        <p class="mb-4 font-weight-bold">Ingrese su correo electronico vinculado a su cuenta</p>
                        <form @submit.prevent="sendResetCode" class="user">
                            <div class="form-group">
                                <input type="email" class="form-control" v-model="email" placeholder="Ingrese su correo electrónico" required />
                            </div>
                            <button type="submit" class="btn btn-block">Enviar código</button>
                        </form>
                    </div>
                    <div v-if="showPasswordForm">
                        <form @submit.prevent="resetPassword" class="user">
                            <div class="form-group">
                                <input type="password" class="form-control" v-model="newPassword" placeholder="Nueva contraseña" required />
                            </div>
                            <div class="form-group">
                                <input type="password" class="form-control" v-model="confirmPassword" placeholder="Confirmar contraseña" required />
                            </div>
                            <div class="form-group">
                                <input type="text" class="form-control" v-model="code" placeholder="Ingrese el código enviado a su correo" required />
                            </div>
                            <button type="submit" class="btn btn-block">Actualizar contraseña</button>
                        </form>
                    </div>
                </div>
            </div>
            <div class="modal-footer" v-if="!showResetPasswordForm">
                <button type="button" data-dismiss="modal" aria-label="Close" class="btn custom-login-button" @click="handleLogin">Iniciar Sesión</button>
            </div>
        </div>
    </div>
</div>

</template>

<script>
import { ref, markRaw } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/store";
import FooterPrincipal from "../components/Footers/FooterPrincipal.vue";
import MenuPrincipal from "../components/Menus/MenuPrincipal.vue";
import ComponenteDinamico from "../components/ComponenteDinamico.vue";
import RegistroUsuario from "../components/Users/inicio/RegistroUsuario.vue";
import RegistroProyecto from '../components/Users/inicio/RegistroProyecto.vue';
import Rubricas_Calificadas from "../components/Users/inicio/Rubricas_Calificadas.vue";
import Carrusel from "../components/Users/inicio/Carrusel.vue";
import InicioPrincipal from "../components/Users/inicio/InicioPrincipal.vue";
import NotAvailable from "./NotAvailable.vue";
import { requestResetCode, changePassword } from "@/services/authService";
import { useToastUtils } from "@/utils/toast"; // Importar librería de toast

// Styles
import "../assets/Styles/main_styles.css";
import '../assets/Styles/responsive_main.css';
import '../assets/plugins/fontawesome-free-5.0.1/css/fontawesome-all.css';

export default {
    components: {
        MenuPrincipal: markRaw(MenuPrincipal),
        FooterPrincipal: markRaw(FooterPrincipal),
        RegistroUsuario: markRaw(RegistroUsuario),
        RegistroProyecto: markRaw(RegistroProyecto),
        Rubricas_Calificadas: markRaw(Rubricas_Calificadas),
        InicioPrincipal: markRaw(InicioPrincipal),
        Carrusel: markRaw(Carrusel),
        NotAvailable: markRaw(NotAvailable),
        ComponenteDinamico,
    },
    setup() {
        const currentComponent = ref(InicioPrincipal);
        const componente = ref("");
        const changeComponent = (componentName) => {
            const componentMap = {
                NotAvailable: NotAvailable,
                RegistroUsuario: RegistroUsuario,
                RegistroProyecto: RegistroProyecto,
                Rubricas_Calificadas: Rubricas_Calificadas,
                InicioPrincipal: InicioPrincipal
            };

            currentComponent.value = componentMap[componentName] || NotAvailable;
            componente.value = componentName;

            if (componentName == 'RegistroProyecto') {
                componente.value = 'Registrar Proyecto';
            } else if (componentName == 'RegistroUsuario') {
                componente.value = 'Evaluadores';
            } else if (componentName == 'Rubricas_Calificadas') {
                componente.value = 'Consultar Proyecto';
            }
        };

        const authStore = useAuthStore();
        const route = useRouter();

        const user = ref(null);
        const email = ref("");
        const password = ref("");
        const newPassword = ref("");
        const confirmPassword = ref("");
        const code = ref("");
        const errorMessage = ref(null);
        const error = ref(null);
        const showResetPasswordForm = ref(false);
        const showPasswordForm = ref(false);

        // Importar funciones de toast
        const { showSuccessToast, showErrorToast } = useToastUtils();

        const handleLogin = async () => {
            try {
                await authStore.login(email.value, password.value);

                if (!authStore.authError) {
                    const user = authStore.user;
                    console.log(user);
                    showSuccessToast("¡Inicio de sesión exitoso!");
                    route.push('/pagina-usuario');
                }
            } catch (error) {
                errorMessage.value = "Error durante el login: " + error.message;
                showErrorToast(errorMessage.value); // Mostrar alerta de error
            }
        };

        const openResetPasswordModal = () => {
            showResetPasswordForm.value = true;
        };

        const resetModalState = () => {
            // Resetea las variables al estado inicial del modal
            showResetPasswordForm.value = false;
            showPasswordForm.value = false;
            email.value = "";
            password.value = "";
            newPassword.value = "";
            confirmPassword.value = "";
            code.value = "";
            errorMessage.value = null;
            error.value = null;
        };

        const sendResetCode = async () => {
            error.value = null; // Limpiar error previo
            try {
                await requestResetCode(email.value);
                showPasswordForm.value = true; // Mostrar los inputs adicionales
                showSuccessToast("Código de recuperación enviado a su correo."); // Mostrar alerta de éxito
            } catch (err) {
                error.value = err.response?.data?.detail || "Error enviando el código. Intente de nuevo.";
                showErrorToast(error.value); // Mostrar alerta de error
            }
        };

        const resetPassword = async () => {
            error.value = null; // Limpiar error previo

            if (newPassword.value !== confirmPassword.value) {
                error.value = "Las contraseñas no coinciden.";
                showErrorToast(error.value); // Mostrar alerta de error
                return;
            }

            try {
                await changePassword(email.value, newPassword.value, code.value);
                showSuccessToast("¡Contraseña actualizada con éxito!");
                resetModalState(); // Volver al formulario de login
            } catch (err) {
                error.value = err.response?.data?.detail || "Error actualizando la contraseña. Verifique el código.";
                showErrorToast(error.value); // Mostrar alerta de error
            }
        };

        return {
            user,
            email,
            password,
            newPassword,
            confirmPassword,
            code,
            errorMessage,
            error,
            showResetPasswordForm,
            showPasswordForm,
            route,
            currentComponent,
            componente,
            changeComponent,
            handleLogin,
            openResetPasswordModal,
            resetModalState,
            sendResetCode,
            resetPassword,
        };
    },
    mounted() {
        const script = document.createElement('script');
        script.src = 'src/assets/js/custom.js';
        script.async = true;
        document.head.appendChild(script);
    }
};
</script>



<style scoped>
.custom-login-button{
    border: 0;
    color: #000;
}
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

.back_img{
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
	color: #FFFFFF;
}

.hero_slide_content h1 span {
	background: #ffb606;
	padding-left: 13px;
	padding-right: 13px;
	margin-left: -12px;
	margin-right: -12px;
}
.title-styling {
    font-size: 1rem; /* Tamaño más grande */
    color: #FFC107; /* Color del botón */
    font-weight: bold; /* Negrita */
}


.forgot-password-link:hover {
    text-decoration: underline; /* Subrayar en hover si lo deseas */
}

.font-weight-bold {
    font-weight: bold; /* Negrita en el texto */
}


.btn {
    color: rgb(255, 182, 6);
    color: #000000;
    font-size: medium;
  }
  
  .btn:hover:hover {
    background-color: rgb(0, 0, 0);
    color: white;
  }
  

</style>
