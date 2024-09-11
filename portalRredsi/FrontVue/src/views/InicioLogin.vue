<template>
    <div class="super_container">
        <!-- Header -->
        <header class="header d-flex flex-row">
            <div class="header_content with_button d-flex flex-row align-items-center justify-content-start">
                <div class="logo_container">
                    <div class="logo">
                        <img class="img-fluid" src="../../assets/logoRredsi.png" alt="Logo" />
                        <span>RREDSI</span>
                    </div>
                </div>

                <nav class="main_nav_container">
                    <div class="main_nav">
                        <ul class="main_nav_list d-flex justify-content-between">
                            <li class="main_nav_item" v-for="(tab, index) in left_tabs" :key="`left-${index}`">
                                <a :href="tab.ruta">{{ tab.nombre }}</a>
                            </li>
                            <li class="main_nav_item" v-for="(tab, index) in mid_tabs" :key="`mid-${index}`">
                                <div class="dropdown">
                                    <a class="dropdown-toggle text-dark" href="#" role="button" 
                                       data-bs-toggle="dropdown" aria-expanded="false">
                                        {{ tab.nombre }}
                                    </a>
                                    <div class="dropdown-menu text-center">
                                        <a v-for="(opcion, opcionIndex) in tab.opciones" :key="`option-${opcionIndex}`"
                                            :href="opcion.ruta">
                                            {{ opcion.nombre }}
                                        </a>
                                    </div>
                                </div>
                            </li>
                            <li :class="['main_nav_item', visibilidad]"><a href="#">{{ tab_name }}</a></li>
                            <li :class="['main_nav_item', visibilidadLogin]">
                                <a href="#" type="button" data-bs-toggle="modal" data-bs-target="#LoginModal">Login</a>
                            </li>
                        </ul>
                    </div>
                </nav>
            </div>

            <a href="#" class="header_side d-flex flex-row justify-content-center align-items-center">
                <h3 class="main_nav_item text-dark">{{ yellow_tab }}</h3>
            </a>

            <!-- Hamburger -->
            <div class="hamburger_container">
                <i class="fas fa-bars trans_200"></i>
            </div>
        </header>

        <!-- Sidebar -->
        <div class="menu_container menu_mm">
            <!-- Sidebar content here -->
        </div>

        <!-- Modal de Login -->
        <div class="modal fade" id="LoginModal" tabindex="-1" aria-labelledby="LoginModalLabel"
            aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title" id="LoginModalLabel">Login</h5>
                        <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <!-- Formulario de login -->
                        <form>
                            <div class="form-group">
                                <label for="email" class="text-dark">Correo electrónico</label>
                                <input type="email" class="form-control" id="email" v-model="email"
                                    placeholder="Ingrese su correo">
                            </div>
                            <div class="form-group mt-3">
                                <label for="password" class="text-dark">Contraseña</label>
                                <input type="password" class="form-control" id="password" v-model="password"
                                    placeholder="Contraseña">
                            </div>
                        </form>
                        <p v-if="errorMessage" class="text-danger mt-3">{{ errorMessage }}</p>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
                        <button type="button" data-bs-dismiss="modal" aria-label="Close" class="btn btn-primary custom-login-button" @click="handleLogin">Iniciar Sesión</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { ref, reactive } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/store'; // Ajusta la ruta del store según tu estructura de proyecto

export default {
    props: {
        rol: String,
    },
    setup(props) {
        // Obtén la instancia del store y el router
        const authStore = useAuthStore();
        const router = useRouter();

        const user = ref({})
        // Define las propiedades reactivas para el email, la contraseña y el mensaje de error
        const email = ref('');
        const password = ref('');
        const errorMessage = ref(null);

        // Define las propiedades dinámicas según el rol
        const state = reactive({
            left_tabs: [],
            mid_tabs: [],
            tab_name: '',
            visibilidad: 'd-none',
            visibilidadLogin: 'd-inline-block',
            yellow_tab: 'Contáctanos',
        });

        if (props.rol === 'Administrador') {
            Object.assign(state, {
                left_tabs: [{ nombre: 'Inicio', ruta: '#' }, { nombre: 'Perfil', ruta: '#' }, { nombre: 'Cuentas', ruta: '#' }, { nombre: 'Rubricas', ruta: '#' }],
                mid_tabs: [{ nombre: 'Eventos', opciones: [{ nombre: 'Salas', ruta: '#' }, { nombre: 'Asistencia', ruta: '#' }, { nombre: 'Convocatoria', ruta: '#' }] }],
                tab_name: '',
                visibilidadLogin: 'd-none',
                visibilidad: 'd-none',
                yellow_tab: 'Cerrar Sesión'
            });
        } else if (props.rol === 'Delegado') {
            Object.assign(state, {
                left_tabs: [{ nombre: 'Inicio', ruta: '#' }, { nombre: 'Perfil', ruta: '#' }],
                mid_tabs: [
                    { nombre: 'Evaluadores', opciones: [{ nombre: 'Postulaciones', ruta: '#' }, { nombre: 'Lista de Evaluadores', ruta: '#' }] },
                    { nombre: 'Proyectos', opciones: [{ nombre: 'Asignacion de Proyectos', ruta: '#' }, { nombre: 'Lista de Proyectos', ruta: '#' }] },
                    { nombre: 'Evento', opciones: [{ nombre: 'Salas', ruta: '#' }, { nombre: 'Asistencia', ruta: '#' }] },
                ],
                tab_name: '',
                visibilidadLogin: 'd-none',
                visibilidad: 'd-none',
                yellow_tab: 'Cerrar Sesión'
            });
        } else if (props.rol === 'Evaluador') {
            Object.assign(state, {
                left_tabs: [{ nombre: 'Inicio', ruta: '#' }, { nombre: 'Perfil', ruta: '#' }],
                mid_tabs: [{ nombre: 'Proyectos', opciones: [{ nombre: 'Primera Etapa', ruta: '#' }, { nombre: 'Segunda Etapa', ruta: '#' }] }],
                tab_name: 'Convocatoria',
                visibilidadLogin: 'd-none',
                visibilidad: 'd-inline-block',
                yellow_tab: 'Cerrar Sesión'
            });
        } else {
            Object.assign(state, {
                left_tabs: [{ nombre: 'Inicio', ruta: '#' }],
                mid_tabs: [{ nombre: 'Proyectos', opciones: [{ nombre: 'Registrar Proyecto', ruta: '#' }, { nombre: 'Consultar Proyecto', ruta: '#' }] }],
                tab_name: 'Evaluadores',
                visibilidadLogin: 'd-inline-block',
                visibilidad: 'd-inline-block',
                yellow_tab: 'Contáctanos'
            });
        }

        // Método para manejar el login
        const handleLogin = async () => {
            try {
                await authStore.login(email.value, password.value);

                if (authStore.authError) {
                    errorMessage.value = authStore.authError;
                } else {
                    
                    const user = authStore.user;
                    console.log(user)
                    // const permissions = authStore.permissions;
                    if(user?.id_rol == 2){
                     // Reemplaza '/dashboard' con la ruta deseada
                        router.push('/principal-delegado');
                    }else if(user?.id_rol == 1){
                        router.push('/principal-evaluador');
                    }
                }
            } catch (error) {
                errorMessage.value = 'Error durante el login: ' + error.message;
            }
        };

        return {
            ...state,
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



<style scoped>
@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,600,700,800|Roboto:400,500,700");
/*********************************
              1. General
  *********************************/

* {
    margin: 0;
    padding: 0;
    -webkit-font-smoothing: antialiased;
    -webkit-text-shadow: rgba(0, 0, 0, 0.01) 0 0 1px;
    text-shadow: rgba(0, 0, 0, 0.01) 0 0 1px;
}

body {
    font-family: "Roboto", sans-serif;
    font-size: 14px;
    font-weight: 400;
    background: #ffffff;
    color: #a5a5a5;
}

ul {
    list-style: none;
    margin-bottom: 0px;
}

p {
    font-family: "Roboto", sans-serif;
    font-size: 14px;
    line-height: 2.29;
    font-weight: 400;
    color: #a5a5a5;
    -webkit-font-smoothing: antialiased;
    -webkit-text-shadow: rgba(0, 0, 0, 0.01) 0 0 1px;
    text-shadow: rgba(0, 0, 0, 0.01) 0 0 1px;
}

p a {
    display: inline;
    position: relative;
    color: inherit;
    border-bottom: solid 1px #ffa07f;
    -webkit-transition: all 200ms ease;
    -moz-transition: all 200ms ease;
    -ms-transition: all 200ms ease;
    -o-transition: all 200ms ease;
    transition: all 200ms ease;
}

a,
a:hover,
a:visited,
a:active,
a:link {
    text-decoration: none;
    -webkit-font-smoothing: antialiased;
    -webkit-text-shadow: rgba(0, 0, 0, 0.01) 0 0 1px;
    text-shadow: rgba(0, 0, 0, 0.01) 0 0 1px;
}

p a:active {
    position: relative;
    color: #ff6347;
}

p a:hover {
    color: #ffffff;
    background: #ffa07f;
}

p a:hover::after {
    opacity: 0.2;
}

::selection {
    background: #ffd266;
    color: #c88e00;
}

p::selection {
    background: #ffd266;
    color: #c88e00;
}

h1 {
    font-size: 36px;
}

h3 {
    font-size: 18px;
}

h1,
h3 {
    font-family: "Roboto", sans-serif;
    -webkit-font-smoothing: antialiased;
    -webkit-text-shadow: rgba(0, 0, 0, 0.01) 0 0 1px;
    text-shadow: rgba(0, 0, 0, 0.01) 0 0 1px;
}

.trans_200 {
    -webkit-transition: all 200ms ease;
    -moz-transition: all 200ms ease;
    -ms-transition: all 200ms ease;
    -o-transition: all 200ms ease;
    transition: all 200ms ease;
}

.super_container {
    width: 100%;
    overflow: hidden;
}

/*********************************
              2. Header
  *********************************/

.header {
    position: fixed;
    top: 45px;
    left: 50%;
    -webkit-transform: translateX(-50%);
    -moz-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    -o-transform: translateX(-50%);
    transform: translateX(-50%);
    width: 1318px;
    height: 104px;
    background: #ffffff;
    z-index: 10;
    -webkit-transition: all 200ms ease;
    -moz-transition: all 200ms ease;
    -ms-transition: all 200ms ease;
    -o-transition: all 200ms ease;
    transition: all 200ms ease;
}

.header_content {
    width: calc(100% - 280px);
    height: 100%;
}

.header_content::before {
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    content: "";
    box-shadow: 0px 20px 49px rgba(0, 0, 0, 0.67);
    z-index: -1;
}

/*********************************
              3. Logo
  *********************************/

.logo_container {
    display: inline-block;
    padding-left: 5px;
}

.logo img {
    vertical-align: middle;
    max-width: 115px;
    margin-top: 8px;
}

.logo span {
    font-family: "Open Sans", sans-serif;
    font-size: 30px;
    font-weight: 900;
    color: #3a3a3a;
    vertical-align: middle;
    text-transform: uppercase;
    margin-left: 3px;
}

/*********************************
              4. Main Nav
  *********************************/

.main_nav_container {
    display: inline-block;
    flex-grow: 3;
    justify-content: space-between;
    margin-left: 50px;
    padding-right: 10px;
}

.main_nav {
    margin-top: 8px;
}

.main_nav_item {
    display: inline-block;

    margin-right: 40px;
}

.main_nav_item:last-child {
    margin-right: 0px;
}

.main_nav_item a {
    font-family: "Open Sans", sans-serif;
    font-size: 14px;
    text-transform: uppercase;
    font-weight: 700;
    color: #3a3a3a;
    -webkit-transition: all 200ms ease;
    -moz-transition: all 200ms ease;
    -ms-transition: all 200ms ease;
    -o-transition: all 200ms ease;
    transition: all 200ms ease;
}

.main_nav_item a:hover {
    color: #ffb606;
}

/*********************************
              5. Header Side
  *********************************/

.header_side {
    width: 100px;
    height: 100%;
    background: #ffb606;
}

.header_side img {
    width: 30px;
    height: 30px;
}

.header_side span {
    display: block;
    position: relative;
    font-size: 18px;
    font-weight: 500;
    color: #ffffff;
    padding-left: 12px;
}

/*********************************
              6. Hamburger
  *********************************/

.hamburger_container {
    position: absolute;
    top: 50%;
    -webkit-transform: translateY(-50%);
    -moz-transform: translateY(-50%);
    -ms-transform: translateY(-50%);
    -o-transform: translateY(-50%);
    transform: translateY(-50%);
    right: 20px;
    display: none;
    cursor: pointer;
}

.hamburger_container i {
    font-size: 24px;
    padding: 10px;
    color: #3a3a3a;
}

.hamburger_container:hover i {
    color: #ffb606;
}

/*********************************
              7. Menu
  *********************************/

.menu_container {
    position: fixed;
    top: 0;
    right: -50vw;
    width: 50vw;
    height: 100vh;
    background: #ffffff;
    z-index: 12;
    -webkit-transition: all 0.6s ease;
    -moz-transition: all 0.6s ease;
    -ms-transition: all 0.6s ease;
    -o-transition: all 0.6s ease;
    transition: all 0.6s ease;
    visibility: hidden;
    opacity: 0;
}

.menu_container.active {
    visibility: visible;
    opacity: 1;
    right: 0;
}

.menu {
    position: absolute;
    top: 150px;
    left: 0;
    padding-left: 15%;
}

.menu_list {
    -webkit-transform: translateY(3.5rem);
    -moz-transform: translateY(3.5rem);
    -ms-transform: translateY(3.5rem);
    -o-transform: translateY(3.5rem);
    transform: translateY(3.5rem);
    -webkit-transition: all 200ms ease;
    -moz-transition: all 200ms ease;
    -ms-transition: all 200ms ease;
    -o-transition: all 200ms ease;
    transition: all 1000ms 600ms ease;
    opacity: 0;
}

.menu_container.active .menu_list {
    -webkit-transform: translateY(0px);
    -moz-transform: translateY(0px);
    -ms-transform: translateY(0px);
    -o-transform: translateY(0px);
    transform: translateY(0px);
    opacity: 1;
}

.menu_item {
    margin-bottom: 9px;
}

.menu_item a {
    font-family: "Open Sans", sans-serif;
    font-size: 30px;
    font-weight: 700;
    color: #3a3a3a;
    -webkit-transition: all 200ms ease;
    -moz-transition: all 200ms ease;
    -ms-transition: all 200ms ease;
    -o-transition: all 200ms ease;
    transition: all 200ms ease;
}

.menu_item a:hover {
    color: #ffb606;
}

.menu_close_container {
    position: absolute;
    top: 86px;
    right: 79px;
    width: 21px;
    height: 21px;
    cursor: pointer;
    -webkit-transform: rotate(45deg);
    -moz-transform: rotate(45deg);
    -ms-transform: rotate(45deg);
    -o-transform: rotate(45deg);
    transform: rotate(45deg);
}

.menu_close {
    top: 9px;
    width: 21px;
    height: 3px;
    background: #3a3a3a;
    -webkit-transition: all 200ms ease;
    -moz-transition: all 200ms ease;
    -ms-transition: all 200ms ease;
    -o-transition: all 200ms ease;
    transition: all 200ms ease;
}

.menu_close::after {
    display: block;
    position: absolute;
    top: -9px;
    left: 9px;
    content: "";
    width: 3px;
    height: 21px;
    background: #3a3a3a;
    -webkit-transition: all 200ms ease;
    -moz-transition: all 200ms ease;
    -ms-transition: all 200ms ease;
    -o-transition: all 200ms ease;
    transition: all 200ms ease;
}

.menu_close_container:hover .menu_close,
.menu_close_container:hover .menu_close::after {
    background: #ffb606;
}

/*********************************
                  8. Menu Social
      *********************************/

.menu_social_container {
    margin-top: 100px;
    -webkit-transform: translateY(3.5rem);
    -moz-transform: translateY(3.5rem);
    -ms-transform: translateY(3.5rem);
    -o-transform: translateY(3.5rem);
    transform: translateY(3.5rem);
    -webkit-transition: all 1000ms 1000ms ease;
    -moz-transition: all 1000ms 1000ms ease;
    -ms-transition: all 1000ms 1000ms ease;
    -o-transition: all 1000ms 1000ms ease;
    transition: all 1000ms 1000ms ease;
    opacity: 0;
    padding-left: 4px;
}

.menu_social_item {
    display: inline-block;
    margin-right: 30px;
}

.menu_social_item a i {
    color: #3a3a3a;
}

.menu_social_item a i:hover {
    color: #ffb606;
}

.menu_container.active .menu_social_container {
    -webkit-transform: translateY(0px);
    -moz-transform: translateY(0px);
    -ms-transform: translateY(0px);
    -o-transform: translateY(0px);
    transform: translateY(0px);
    opacity: 1;
}

/*********************************
              9. Menu copyright
  *********************************/
.menu_copyright {
    margin-top: 60px;
    -webkit-transform: translateY(3.5rem);
    -moz-transform: translateY(3.5rem);
    -ms-transform: translateY(3.5rem);
    -o-transform: translateY(3.5rem);
    transform: translateY(3.5rem);
    -webkit-transition: all 1000ms 1200ms ease;
    -moz-transition: all 1000ms 1200ms ease;
    -ms-transition: all 1000ms 1200ms ease;
    -o-transition: all 1000ms 1200ms ease;
    transition: all 1000ms 1200ms ease;
    opacity: 0;
    padding-left: 3px;
}

.menu_container.active .menu_copyright {
    -webkit-transform: translateY(0px);
    -moz-transform: translateY(0px);
    -ms-transform: translateY(0px);
    -o-transform: translateY(0px);
    transform: translateY(0px);
    opacity: 1;
}

@media only screen and (max-width: 1920px) {
    .header_side {
        width: 285px;
    }

    .main_nav_container {
        padding-right: 63px;
    }
}

@media only screen and (max-width: 1600px) {
    .header_side {
        width: 285px;
    }

    .main_nav_container {
        padding-right: 63px;
    }
}

@media only screen and (max-width: 1440px) {
    .header_side {
        width: 285px;
    }

    .main_nav_container {
        padding-right: 63px;
    }
}

@media only screen and (max-width: 1380px) {
    .header {
        width: 1200px;
    }

    .header_content {
        width: 100%;
    }

    .main_nav_container {
        padding-right: 63px;
    }

    .header_side {
        width: 219px;
    }
}

@media only screen and (max-width: 1024px) {
    .main_nav_item {
        margin-right: 33px;
    }
}

@media only screen and (max-width: 991px) {
    .main_nav_container {
        display: none;
    }

    .logo_container {
        padding-left: 30px;
    }

    .hamburger_container {
        display: block;
    }
}

@media only screen and (max-width: 767px) {
    .menu_container {
        right: -100vw;
        width: 100vw;
        height: 100vh;
    }
}

@media only screen and (max-width: 575px) {
    h1 {
        font-size: 24px;
    }

    p {
        font-size: 13px;
    }

    .header {
        height: 74px;
    }

    .logo_container {
        padding-left: 15px;
    }

    .logo img {
        width: 30px;
    }

    .logo span {
        font-size: 16px;
    }

    .hamburger_container {
        right: 5px;
    }

    .menu {
        top: 70px;
    }

    .menu_item {
        margin-bottom: 0px;
    }

    .menu_item a {
        font-size: 24px;
    }

    .menu_copyright {
        display: none;
    }

    .menu_social_container {
        margin-top: 50px;
    }

    .menu_close_container {
        right: 30px;
        top: 34px;
    }
}

@media only screen and (max-width: 479px) {
    .header {
        height: 60px;
        top: 15px;
    }
}

.scroll-div {
    width: 1000px;
    height: 400px;
    overflow-y: auto;
    overflow-x: hidden;
}

body {
    font-family: Arial, sans-serif;
    margin: 20px;
    background-color: #f7f7f7;
}

.form-section {
    background-color: #f8f9fa;
    border: 1px solid #ced4da;
    padding: 20px;
    border-radius: 5px;
    max-width: 800px;
    margin: auto;
}

.form-section h2 {
    color: rgb(255, 182, 6);
    text-align: center;
}

.form-section .title-icon {
    color: rgb(255, 182, 6);
    margin-right: 10px;
    font-size: 1.5rem;
    margin-bottom: 10px;
}

.title-line {
    border-top: 2px solid rgb(255, 182, 6);
    margin-top: -10px;
}

.btn:hover {
    box-shadow: none;
    color: #494949;
    background-color: rgb(255, 182, 6);
}

.accordion-button:focus {
    box-shadow: none;
    background-color: rgb(255, 182, 6);
    outline: none;
}

.span_acor {
    font-size: 18px
}

.modal-header .icon {
    color: rgb(255, 182, 6);
    font-size: 2rem;
    margin-right: 10px;
}

.modal-header {
    color: #000000;
    font-size: 2rem;
    margin-right: 10px;
}

.enlace {
    padding: 0.6rem;
    text-decoration: none;
    text-align: center;
    color: black;
    transition: all 0.4s ease-in-out;
}

.enlace:focus {
    background-color: rgb(255, 182, 6);
    color: black;
}

#cont_consultarProyecto {
    scroll-margin-top: 104px;
}

.botonAbrir {
    width: 30%;
    font-size: 18px;
}

.w-30 {
    width: 30% !important;
}

.btn-custom {
    display: inline-flex;
    align-items: center;
    padding: 0.5rem 1rem;
    border: 1px solid transparent;
    border-radius: 0.375rem;
    font-size: 1rem;
    text-align: center;
    text-decoration: none;
    background-color: rgb(255, 182, 6);
    color: black;
}

.btn-custom:hover {
    background-color: #e0a800;
    color: black;
}

.btn-custom i {
    margin-right: 0.5rem;
}

.scroll-div {
    width: 1000px;
    height: 400px;
    overflow-y: auto;
    overflow-x: hidden;
    width: 1000px;
    height: 400px;
    overflow-y: auto;
    overflow-x: hidden;
}

body {
    font-family: Arial, sans-serif;
    margin: 20px;
    background-color: #f7f7f7;
}

.form-section {
    background-color: #f8f9fa;
    /* Color más oscuro que el blanco */
    border: 1px solid #ced4da;
    /* Borde del div */
    background-color: #f8f9fa;
    border: 1px solid #ced4da;
    padding: 20px;
    border-radius: 5px;
    max-width: 800px;
    margin: auto;
}

.form-section h2 {
    color: rgb(255, 182, 6);
    /* Color del encabezado */
    color: rgb(255, 182, 6);
    text-align: center;
}

.form-section .title-icon {
    color: rgb(255, 182, 6);
    /* Color del ícono */
    color: rgb(255, 182, 6);
    margin-right: 10px;
    font-size: 1.5rem;
    /* Tamaño del ícono más grande */
    font-size: 1.5rem;
    margin-bottom: 10px;
}

.title-line {
    border-top: 2px solid rgb(255, 182, 6);
    /* Color de la línea */
    border-top: 2px solid rgb(255, 182, 6);
    margin-top: -10px;
    margin-bottom: 20px;
}

.form-row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 20px;
}

.form-row>div {
    flex: 1;
    margin-right: 20px;
}

.form-row>div:last-child {
    margin-right: 0;
}



input[type="text"],
select {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    font-size: 16px;
}

.custom-file-upload {
    border: 2px dashed #ced4da;
    border-radius: 10px;
    text-align: center;
    padding: 20px;
    cursor: pointer;
}

.custom-file-upload:hover {
    border-color: rgb(255, 182, 6);
}

.custom-file-upload i {
    font-size: 2rem;
    color: rgb(0, 123, 255);
}

.custom-file-upload span {
    display: block;
    margin-top: 10px;
    font-weight: bold;
}

.custom-file-upload a {
    color: rgb(0, 0, 0);
    text-decoration: none;
}

.add-author-btn {
    background-color: rgb(255, 182, 6);
    color: black;
    border: none;
    padding: 5px;
    border-radius: 3px;
    font-size: 18px;
    text-align: center;
    cursor: pointer;
}

.modal-content {
    background-color: #fefefe;
    margin: 15% auto;
    padding: 10px;
    border: 1px solid #888;
    width: 400px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}

.modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: bold;
    margin-bottom: 15px;
}

.modal-header span {
    cursor: pointer;
    font-size: 1.5rem;
}

.modal-body {
    margin-bottom: 15px;
}

.modal-footer {
    text-align: center;
}

.modal-footer button {
    margin: 0 10px;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 14px;
}

.add-btn {
    color: rgb(0, 0, 0);
}

.close-btn {
    background-color: #b7b7b7;
    color: rgb(0, 0, 0);
}

#listaAutores div {
    margin-top: 5px;
    padding: 5px;
    background-color: #f1f1f1;
    border-radius: 5px;
}

.accordion {
    display: none;
}

@media only screen and (max-width:767px) {
    .contenedor_principal {
        display: none;
    }

    .accordion {
        display: block;
    }

    .card {
        width: 100%;
        text-align: left;
        text-decoration: none;
        background-color: #f7f7f7;
        border: 1px solid black;
        margin-bottom: 2rem;
    }

    .card button {
        font-weight: 700;
        text-align: center;
    }

    .toggle-button:not(.collapsed) {
        color: rgb(255, 182, 6);
    }

}


.custom-login-button {
    background-color: #ffb606;
    /* Background color for the button */
    border-color: #ffb606;
}

.custom-login-button:hover {
    background-color: #e5a305;
    /* Darker shade for hover effect */
    border-color: #e5a305;
}
</style>