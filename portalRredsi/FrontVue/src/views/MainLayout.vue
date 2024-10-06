<template>
    <div class="super_container">
        <!-- Header -->
        <MenuPrincipal @component-selected="changeComponent"/>
    </div>

    <!-- Mostrar la imagen de fondo en las otras opciones del menú  -->
    <div v-if="componente == 'Registrar Proyecto' || componente == 'Evaluadores' || componente == 'Consultar Proyecto' || componente == 'Consultar Proyecto'" class="hero_slide">
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
                    <h5 class="modal-title" id="LoginModalLabel">Login</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <!-- Formulario de login -->
                    <form>
                        <div class="form-group">
                            <label for="email" class="text-dark">Correo electrónico</label>
                            <input type="email" class="form-control" id="email" v-model="email"
                                placeholder="Ingrese su correo" />
                        </div>
                        <div class="form-group mt-3">
                            <label for="password" class="text-dark">Contraseña</label>
                            <input type="password" class="form-control" id="password" v-model="password"
                                placeholder="Contraseña" />
                        </div>
                    </form>
                    <p v-if="errorMessage" class="text-danger mt-3">
                        {{ errorMessage }}
                    </p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">
                        Cerrar
                    </button>
                    <button type="button" data-dismiss="modal" aria-label="Close"
                        class="btn btn-primary custom-login-button" @click="handleLogin">
                        Iniciar Sesión
                    </button>
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
            componente.value=componentName;

            if(componentName == 'RegistroProyecto'){
                componente.value= 'Registrar Proyecto';
            }else if(componentName == 'RegistroUsuario'){
                componente.value= 'Evaluadores';
            }else if(componentName == 'Rubricas_Calificadas'){
                componente.value= 'Consultar Proyecto';
            }
        };

        const authStore = useAuthStore();
        const route = useRouter();

        const user = ref(null);
        const email = ref("");
        const password = ref("");
        const errorMessage = ref(null);

        const handleLogin = async () => {
            try {

                await authStore.login(email.value, password.value);

                if (authStore.authError) {
                } else {
                    const user = authStore.user;
                    console.log(user);

                    route.push('/pagina-usuario');

                }
            } catch (error) {
                errorMessage.value = "Error durante el login: " + error.message;
            }
        };


        return {
            user,
            email,
            password,
            errorMessage,
            route,
            currentComponent,
            componente,
            changeComponent,
            handleLogin,
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
</style>
