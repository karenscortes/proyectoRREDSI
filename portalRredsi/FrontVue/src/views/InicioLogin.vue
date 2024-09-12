<template>
  <div class="super_container">
    <!-- Header -->
    <MenuPrincipal></MenuPrincipal>
    
  </div>

  <!-- Home -->

  <div class="home">
    <!-- Hero Slider -->
    <div class="hero_slider_container">
      <div class="hero_slider owl-carousel">
        <!-- Hero Slide -->
        <div class="hero_slide">
          <div
            class="hero_slide_background"
            style="
              background-image: url(../assets/img/slider_background.jpg);
            "
          ></div>
          <div
            class="hero_slide_container d-flex flex-column align-items-center justify-content-center"
          >
            <div class="hero_slide_content text-center">
              <h1
                data-animation-in="fadeInUp"
                data-animation-out="animate-out fadeOut"
              >
                Inscripciones <span>abiertas</span> 2024!
              </h1>
            </div>
          </div>
        </div>

        <!-- Hero Slide -->
        <div class="hero_slide">
          <div
            class="hero_slide_background"
            style="
              background-image: url(../plantilla/images/slider_background.jpg);
            "
          ></div>
          <div
            class="hero_slide_container d-flex flex-column align-items-center justify-content-center"
          >
            <div class="hero_slide_content text-center">
              <h1
                data-animation-in="fadeInUp"
                data-animation-out="animate-out fadeOut"
              >
                Evaluadores <span>certificados</span> !
              </h1>
            </div>
          </div>
        </div>

        <!-- Hero Slide -->
        <div class="hero_slide">
          <div
            class="hero_slide_background"
            style="
              background-image: url(../plantilla/images/slider_background.jpg);
            "
          ></div>
          <div
            class="hero_slide_container d-flex flex-column align-items-center justify-content-center"
          >
            <div class="hero_slide_content text-center">
              <h1
                data-animation-in="fadeInUp"
                data-animation-out="animate-out fadeOut"
              >
                Proyectos <span>investigativos</span> !
              </h1>
            </div>
          </div>
        </div>
      </div>

      <div class="hero_slider_left hero_slider_nav trans_200">
        <span class="trans_200">prev</span>
      </div>
      <div class="hero_slider_right hero_slider_nav trans_200">
        <span class="trans_200">next</span>
      </div>
    </div>
  </div>
  <div class="hero_boxes">
    <div class="hero_boxes_inner">
      <div class="container">
        <div class="row">
          <div class="col-lg-4 hero_box_col">
            <div
              class="hero_box d-flex flex-row align-items-center justify-content-start"
            >
              <img src="../plantilla/images/books.svg" class="svg" alt="" />
              <div class="hero_box_content">
                <h2 class="hero_box_title">Convocatorias</h2>
                <a
                  href="https://rredsi.com.co/xiv-encuentro-departamental-de-semilleros-de-investigacion-de-risaralda/"
                  class="hero_box_link"
                  >ver más</a
                >
              </div>
            </div>
          </div>

          <div class="col-lg-4 hero_box_col">
            <div
              class="hero_box d-flex flex-row align-items-center justify-content-start"
            >
              <img
                src="../plantilla/images/earth-globe.svg"
                class="svg"
                alt=""
              />
              <div class="hero_box_content">
                <h2 class="hero_box_title">RREDSI</h2>
                <a href="https://rredsi.com.co/" class="hero_box_link"
                  >ver más</a
                >
              </div>
            </div>
          </div>

          <div class="col-lg-4 hero_box_col">
            <div
              class="hero_box d-flex flex-row align-items-center justify-content-start"
            >
              <img src="../plantilla/images/professor.svg" class="svg" alt="" />
              <div class="hero_box_content">
                <h2 class="hero_box_title">Pertenecer</h2>
                <a
                  href="https://rredsi.com.co/como-pertenecer-a-rredsi/"
                  class="hero_box_link"
                  >ver más</a
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Events -->

  <div class="events page_section mb-5">
    <div class="container">
      <div class="row mt-0">
        <div class="col">
          <div class="section_title text-center">
            <h1>Próximos eventos</h1>
          </div>
        </div>
      </div>

      <div class="event_items">
        <!-- Event Item -->
        <div class="row event_item">
          <div class="col">
            <div class="row d-flex flex-row align-items-end">
              <div class="col-lg-2 order-lg-1 order-2">
                <div
                  class="event_date d-flex flex-column align-items-center justify-content-center"
                >
                  <div class="event_day">02</div>
                  <div class="event_month">Marzo</div>
                </div>
              </div>

              <div class="col-lg-6 order-lg-2 order-3">
                <div class="event_content">
                  <div class="event_name">
                    <a class="trans_200" href="#">Incripciones abiertas</a>
                  </div>
                  <div class="event_location">Portal rredsi</div>
                  <p>
                    In aliquam, augue a gravida rutrum, ante nisl fermentum
                    nulla, vitae tempor nisl ligula vel nunc. Proin quis mi
                    malesuada, finibus tortor.
                  </p>
                </div>
              </div>

              <div class="col-lg-4 order-lg-3 order-1">
                <div class="event_image">
                  <img
                    src="../assets/img/event_1.jpg"
                    alt="https://unsplash.com/@theunsteady5"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Event Item -->
        <div class="row event_item">
          <div class="col">
            <div class="row d-flex flex-row align-items-end">
              <div class="col-lg-2 order-lg-1 order-2">
                <div
                  class="event_date d-flex flex-column align-items-center justify-content-center"
                >
                  <div class="event_day">12</div>
                  <div class="event_month">Mayo</div>
                </div>
              </div>

              <div class="col-lg-6 order-lg-2 order-3">
                <div class="event_content">
                  <div class="event_name">
                    <a class="trans_200" href="#"
                      >Primera publicación de resultados</a
                    >
                  </div>
                  <div class="event_location">Portal rredsi</div>
                  <p>
                    In aliquam, augue a gravida rutrum, ante nisl fermentum
                    nulla, vitae tempor nisl ligula vel nunc. Proin quis mi
                    malesuada, finibus tortor.
                  </p>
                </div>
              </div>

              <div class="col-lg-4 order-lg-3 order-1">
                <div class="event_image">
                  <img
                    src="../assets/img/event_2.jpg"
                    alt="https://unsplash.com/@claybanks1989"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Event Item -->
        <div class="row event_item">
          <div class="col">
            <div class="row d-flex flex-row align-items-end">
              <div class="col-lg-2 order-lg-1 order-2">
                <div
                  class="event_date d-flex flex-column align-items-center justify-content-center"
                >
                  <div class="event_day">22</div>
                  <div class="event_month">Junio</div>
                </div>
              </div>

              <div class="col-lg-6 order-lg-2 order-3">
                <div class="event_content">
                  <div class="event_name">
                    <a class="trans_200" href="#">Evento presencial</a>
                  </div>
                  <div class="event_location">Auditorio Jorge Roa</div>
                  <p>
                    In aliquam, augue a gravida rutrum, ante nisl fermentum
                    nulla, vitae tempor nisl ligula vel nunc. Proin quis mi
                    malesuada, finibus tortor.
                  </p>
                </div>
              </div>

              <div class="col-lg-4 order-lg-3 order-1">
                <div class="event_image">
                  <img
                    src="../assets/img/event_3.jpg"
                    alt="https://unsplash.com/@juanmramosjr"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Event Item -->
        <div class="row event_item">
          <div class="col">
            <div class="row d-flex flex-row align-items-end">
              <div class="col-lg-2 order-lg-1 order-2">
                <div
                  class="event_date d-flex flex-column align-items-center justify-content-center"
                >
                  <div class="event_day">30</div>
                  <div class="event_month">Junio</div>
                </div>
              </div>

              <div class="col-lg-6 order-lg-2 order-3">
                <div class="event_content">
                  <div class="event_name">
                    <a class="trans_200" href="#"
                      >Segunda publicación de resultados</a
                    >
                  </div>
                  <div class="event_location">Portal rredsi</div>
                  <p>
                    In aliquam, augue a gravida rutrum, ante nisl fermentum
                    nulla, vitae tempor nisl ligula vel nunc. Proin quis mi
                    malesuada, finibus tortor.
                  </p>
                </div>
              </div>

              <div class="col-lg-4 order-lg-3 order-1">
                <div class="event_image">
                  <img
                    src="../plantilla/images/event_2.jpg"
                    alt="https://unsplash.com/@claybanks1989"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
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
// Styles
import "../assets/Styles/main_styles.css";
import '../assets/Styles/responsive_main.css';
import '../assets/plugins/OwlCarousel2-2.2.1/owl.carousel.css';
import '../assets/plugins/OwlCarousel2-2.2.1/animate.css';
import '../assets/plugins/OwlCarousel2-2.2.1/owl.theme.default.css';
import '../assets/plugins/fontawesome-free-5.0.1/css/fontawesome-all.css';

// Plugins and scripts
import '../assets/plugins/OwlCarousel2-2.2.1/owl.carousel';
import '../assets/plugins/greensock/TweenMax.min.js';
import '../assets/plugins/greensock/TimelineMax.min.js';

import '../assets/plugins/scrollTo/jquery.scrollTo.min.js';
import '../assets/plugins/easing/easing.js';
import '../assets/js/custom.js';


export default {
  components: {
    FooterPrincipal,
    MenuPrincipal,
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
