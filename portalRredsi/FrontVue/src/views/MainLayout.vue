<template>
    <div class="super_container">
        <!-- Header -->
        <MenuPrincipal @component-selected="changeComponent"/>
    </div>

    <!-- Mostrar la imagen de fondo en las otras opciones del menú  -->
    <div v-if="componente == 'RegistroProyecto' || componente == 'RegistroUsuario' || componente == 'ConsultarProyecto'">
        <img src="../assets/img/slider_background.jpg" alt height="200px" width="100%">
    </div>
    <div v-else>
        
    </div>

    <div class="container pt-5">
        <ComponenteDinamico :currentComponent="currentComponent"/>
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
import { ref , markRaw} from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/store";
import FooterPrincipal from "../components/Footers/FooterPrincipal.vue";
import MenuPrincipal from "../components/Menus/MenuPrincipal.vue";
import ComponenteDinamico from "../components/ComponenteDinamico.vue";
import RegistroUsuario from "../components/Users/inicio/RegistroUsuario.vue";
import RegistroProyecto from '../components/Users/inicio/RegistroProyecto.vue';
import Registro_fases from "../components/Users/inicio/Registro_fases.vue";
import Rubricas_Calificadas from "../components/Users/inicio/Rubricas_Calificadas.vue";

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
        Registro_fases:markRaw(Registro_fases),
        Rubricas_Calificadas:markRaw(Rubricas_Calificadas),
        
        //Componente Por defecto
        NotAvailable: markRaw(NotAvailable),
        ComponenteDinamico,
    },
    setup() {

        const currentComponent = ref(NotAvailable);           
        const componente = ref("")
        const changeComponent = (componentName) => {
            const componentMap = {
                NotAvailable: NotAvailable,
                RegistroUsuario: RegistroUsuario,
                RegistroProyecto:RegistroProyecto,
                Registro_fases:Registro_fases,
                Rubricas_Calificadas:Rubricas_Calificadas,
                
            };

            currentComponent.value = componentMap[componentName] || NotAvailable;
            componente.value=componentName;
            console.log(componentName);
        };

        const authStore = useAuthStore();
        const route = useRouter();

        // Define las propiedades reactivas 
        const user = ref(null);
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
        script.src = 'src/assets/js/custom.js'; // Ruta del archivo JS
        script.async = true; // Opcional, para cargarlo de forma asíncrona
        document.head.appendChild(script);
    }


};
</script>
<style scoped>
    .container{
        min-height: 600px;
    }
</style>