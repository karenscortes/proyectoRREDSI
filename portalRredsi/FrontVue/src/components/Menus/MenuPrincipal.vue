<template>
  <div class="super_container">
    <header class="header d-flex flex-row">
      <div class="header_content with_button d-flex flex-row align-items-center justify-content-start">
        <div class="logo_container">
          <div class="logo">
            <img class="img-fluid" src="../assets/logoRredsi.png" alt="" />
            <span>RREDSI</span>
          </div>
        </div>

        <nav class="main_nav_container">
          <div class="main_nav">
            <ul class="main_nav_list d-flex justify-content-between">
              <li class="main_nav_item" v-for="(tab, index) in left_tabs" :key="index"><a class="text-dark" @click="selectComponent(tab.ruta)">{{ tab.nombre
                  }}</a></li>
              <li class="main_nav_item" v-for="(tab, index) in mid_tabs" :key="index">
                <div class="dropdown">
                  <a class=" dropdown-toggle text-dark" type="button" data-toggle="dropdown" aria-expanded="false">
                    {{ tab.nombre }}
                  </a>
                  <div v-for="(opcion, index) in opciones" :key="index" class="dropdown-menu text-center">
                    <a :href="opcion.ruta">{{ opcion.nombre }}</a><br>
                  </div>
                </div>
              </li>
              <li :class="['main_nav_item', visibilidad]"><a href="#">{{ tab_name }}</a></li>
              <li :class="['main_nav_item', visibilidadLogin]">
                <a href="#" type="button" data-toggle="modal" data-target="#LoginModal">Login</a>
              </li>
            </ul>
          </div>
        </nav>
      </div>
      <a href="#" class="header_side d-flex flex-row justify-content-center align-items-center">
        <h3 class="main_nav_item text-dark" @click="logout">{{ yellow_tab }}</h3>
      </a>

      <!-- Hamburger -->
      <div class="hamburger_container">
        <i class="fas fa-bars trans_200"></i>
      </div>
    </header>

    <!-- Sidebar -->
    <div class="menu_container menu_mm">
      <div class="menu_close_container">
        <div class="menu_close"></div>
      </div>

      <div class="menu_inner menu_mm">
        <div class="menu menu_mm">
          <ul class="menu_list menu_mm">
            <li class="menu_item menu_mm"><a href="#">Inicio</a></li>
            <li class="menu_item menu_mm dropdown">
              <a class="dropdown-toggle text-dark" role="button" type="button"
                style="font-family: 'Open Sans', sans-serif" data-toggle="dropdown" aria-expanded="false">
                Proyectos
              </a>
              <div class="dropdown-menu text-center">
                <a href="#">Registrar proyecto</a>
                <a href="#cont_consultarProyecto">Consultar proyecto</a>
              </div>
            </li>
            <li class="menu_item menu_mm"><a href="#">Evaluadores</a></li>
            <li class="menu_item menu_mm"><a href="#">Login</a></li>
            <li class="menu_item menu_mm"><a href="#">Contacto</a></li>
          </ul>

          <div class="menu_social_container menu_mm">
            <ul class="menu_social menu_mm">
              <li class="menu_social_item menu_mm">
                <a href="https://www.instagram.com/rredsiquindio/"><i class="fab fa-instagram"></i></a>
              </li>
              <li class="menu_social_item menu_mm">
                <a href="https://www.facebook.com/rredsi?mibextid=ZbWKwL"><i class="fab fa-facebook-f"></i></a>
              </li>
              <li class="menu_social_item menu_mm">
                <a href="https://x.com/Rredsi"><i class="fab fa-twitter"></i></a>
              </li>
            </ul>
          </div>

          <div class="menu_copyright menu_mm">
            ADSO 2670586 All rights reserved
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import { defineComponent, toRefs } from 'vue';
import { useAuthStore } from '@/store';
import { useRouter } from 'vue-router'; 

export default defineComponent({
  props: {
    rol: String,
  },
  data() {
    // Lógica condicional basada en el rol
    if (this.rol === 3) { // Administrador
      return {
        left_tabs: [{ nombre: 'Inicio', ruta: '#' }, { nombre: 'Perfil', ruta: '#' }, { nombre: 'Cuentas', ruta: '#' }, { nombre: 'Rubricas', ruta: '#' }],
        mid_tabs: [
          {
            nombre: "Eventos",
            opciones: [{ nombre: 'Salas', ruta: '#' }, { nombre: 'Asistencia', ruta: '#' }, { nombre: 'Convocatoria', ruta: '#' }]
          }
        ],
        tab_name: '',
        visibilidadLogin: "d-none",
        visibilidad: "d-none",
        yellow_tab: 'Cerrar Sesión'
      };
      
    }
     else if (this.rol === 6) { // Superadmin
      return {
        left_tabs: [{ nombre: 'Inicio', ruta: 'super-admin' }],
        mid_tabs: [{nombre: "Informacion delegados", ruta: 'informacion-delegados' }],
        visibilidadLogin: "d-none",
        visibilidad: "d-inline-block",
        yellow_tab: 'Cerrar Sesión'
      };
    }
     else if (this.rol === 2) { // Delegado
      return {
        left_tabs: [{ nombre: 'Inicio', ruta: 'PostulacionesEvaluadoresView' }, { nombre: 'Perfil', ruta: '#' }],
        mid_tabs: [
          {
            nombre: "Evaluadores",
            opciones: [{ nombre: 'Postulaciones', ruta: '' }, { nombre: 'Lista de Evaluadores', ruta: '#' }]
          },
          {
            nombre: "Proyectos",
            opciones: [{ nombre: 'Asignacion de Proyectos', ruta: '#' }, { nombre: 'Lista de Proyectos', ruta: '#' }]
          },
          {
            nombre: "Evento",
            opciones: [{ nombre: 'Salas', ruta: '#' }, { nombre: 'Asistencia', ruta: '#' }]
          }
        ],
        tab_name: '',
        visibilidadLogin: "d-none",
        visibilidad: "d-none",
        yellow_tab: 'Cerrar Sesión'
      };
    } else if (this.rol === 1) { // Evaluador
      return {
        left_tabs: [{ nombre: 'Inicio', ruta: '#' }, { nombre: 'Perfil', ruta: '#' }],
        mid_tabs: [
          {
            nombre: "Proyectos",
            opciones: [{ nombre: 'Primera Etapa', ruta: '#' }, { nombre: 'Segunda Etapa', ruta: '#' }]
          }
        ],
        tab_name: 'Convocatoria',
        visibilidadLogin: "d-none",
        visibilidad: "d-inline-block",
        yellow_tab: 'Cerrar Sesión'
      };
    } else { // Visitante
      return {
        left_tabs: [{ nombre: 'Inicio', ruta: '#' }],
        mid_tabs: [
          {
            nombre: "Proyectos",
            opciones: [{ nombre: 'Registrar Proyecto', ruta: '#' }, { nombre: 'Consultar Proyecto', ruta: '#' }]
          }
        ],
        tab_name: 'Evaluadores',
        visibilidadLogin: "d-inline-block",
        visibilidad: "d-inline-block",
        yellow_tab: 'Contáctanos'
      };
    }
  },
  setup(_, { emit }) {
    const authStore = useAuthStore(); // Accede al store de autenticación
    const { permissions } = toRefs(authStore); // Desestructura y hace reactiva la propiedad permissions
    const router = useRouter();
    const user = authStore.user;

    // Función para cerrar sesión
    const logout = () => {
      authStore.logout();
      router.push('/');
    };

    // Función para seleccionar componentes dinámicamente
    const selectComponent = (componentName) => {
      emit('component-selected', componentName);
    };

    return {
      user,
      permissions,
      logout,
      selectComponent
    };
  }
});


</script>

<style>
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
</style>