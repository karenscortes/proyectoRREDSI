<template>
  <div class="super_container">
    <header class="header d-flex flex-row">
      <div class="header_content with_button d-flex flex-row align-items-center justify-content-start">
        <div class="logo_container">
          <div class="logo">
            <img class="img-fluid" src="../../assets/img/logoRredsi.png" alt="" />
            <span>RREDSI</span>
          </div>
        </div>

        <nav class="main_nav_container">
          <div class="main_nav">
            <ul class="main_nav_list d-flex justify-content-between">
              <li class="main_nav_item">
                <!-- Componente que se remplazará por el Inicio Principal -->
                <a href="#" @click="selectComponent('InicioPrincipal')">Inicio</a>
              </li>
              <li class="main_nav_item">
                <div class="dropdown">
                  <a class=" dropdown-toggle " type="button" data-toggle="dropdown"
                      aria-expanded="false">
                      Proyectos
                  </a>
                  <div class="dropdown-menu text-center">
                    <a href="#" class="dropdown-item" @click="selectComponent('RegistroProyecto')">Registrar proyecto</a>
                    <a href="#" class="dropdown-item" @click="selectComponent('Rubricas_Calificadas')">Consultar proyecto</a>
                  </div>
                </div>
              </li>
              <li class="main_nav_item text-dark"><a href="#" @click="selectComponent('RegistroUsuario')">Evaluadores</a></li>
              <li class="main_nav_item"><a href="#" type="button" data-toggle="modal" data-target="#LoginModal">Login</a></li>
            </ul>
          </div>
        </nav>
      </div>
      <a href="#" class="header_side d-flex flex-row justify-content-center align-items-center">
        <h3 class="main_nav_item text-dark"><a @click="selectComponent('ContactInfoPage')">Contáctanos</a></h3>
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
            <li class="menu_item menu_mm"><a href="#" @click="selectComponent('InicioPrincipal')">Inicio</a></li>
            <li class="menu_item menu_mm dropdown">
              <a  href="#" class="dropdown-toggle" role="button" type="button"
                data-toggle="dropdown" aria-expanded="false">
                Proyectos
              </a>
              <div class="dropdown-menu text-center">
                <a class="dropdown-item" href="#" @click="selectComponent('RegistrarProyecto')">Registrar proyecto</a>
                <a class="dropdown-item" href="#" @click="selectComponent('ConsultarProyecto')">Consultar proyecto</a>
              </div>
            </li>
            <li class="menu_item menu_mm"><a href="#" @click="selectComponent('RegistroUsuario')">Evaluadores</a></li>
            <li class="menu_item menu_mm"><a href="#" type="button" data-toggle="modal" data-target="#LoginModal">Login</a></li>
            <li class="menu_item menu_mm"><a href="#" @click="selectComponent('ContactInfoPage')">Contáctanos</a></li>
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
            <p>ADSO 2670586 All rights reserved</p>  
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import { defineComponent} from "vue";

export default defineComponent({

  setup(_,{ emit }) { 
    const selectComponent = (componentName) => {
      emit('component-selected', componentName); // Emite un evento para seleccionar el componente
    };

    return {
      selectComponent
    };
  }
});
</script>
