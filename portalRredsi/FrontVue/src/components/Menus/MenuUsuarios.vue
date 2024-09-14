<template>
    <header class="header d-flex flex-row position-static">
        <div class="header_content d-flex flex-row align-items-center justify-content-start">

            <div class="logo_container">
                <div class="logo">
                    <img class="img-fluid" src="../../assets/logoRredsi.png" alt="">
                    <span>RREDSI</span>
                </div>
            </div>

            <nav class="main_nav_container">
                <div class="main_nav">
                    <ul class="main_nav_list d-flex justify-content-between">
                        <li class="main_nav_item" v-for="(tab, index) in left_tabs" :key="index"><a @click="selectComponent(tab.ruta)">{{ tab.nombre }}</a></li>
                        <li :class="['main_nav_item', visibilidad]" v-for="(tab, index) in mid_tabs" :key="index">
                            <div class="dropdown">
                                <a class=" dropdown-toggle text-dark" type="button" data-toggle="dropdown"
                                    aria-expanded="false">
                                    {{ tab.nombre }}
                                </a>
                                <div v-for="(opcion, index) in opciones" :key="index" class="dropdown-menu text-center">
                                    <a  :href="opcion.ruta">{{ opcion.nombre }}</a><br>
                                </div>
                            </div>
                        </li>
                        
                        <li class="main_nav_item" v-if="rol === 1"><a href="#">Convocatoria</a></li>
                        <li class="main_nav_item" v-else><a href="#" @click="logout">Cerrar Sesión</a></li>
                    </ul>
                </div>
            </nav>
        </div>

        <!-- Hamburger -->
        <div class="hamburger_container">
            <i class="fas fa-bars trans_200"></i>
        </div>

    </header>

    <!-- dividing line -->
    <div class="container-fluid" id="cont_ejemplo">
       
    </div>
</template>

<script>
import { defineComponent,reactive } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/store";
export default defineComponent({
  props: {
    rol: Number,
  },
  setup(props, { emit }) {
    console.log(props.rol)
        
        const state = reactive({
        left_tabs: [],
        mid_tabs: [],
        visibilidad: "d-none",
        });

        if (props.rol === 3) {
            Object.assign(state, {
                left_tabs: [{nombre:'Inicio', ruta:'AdminView'}, {nombre:'Perfil', ruta:'#'}, {nombre:'Cuentas', ruta:'#'},{nombre:'Rubricas', ruta:'RubricaAdminView'}],
                mid_tabs:[
                    {   nombre:"Eventos", 
                        opciones:[{nombre:'Salas', ruta:'SalasView'}, {nombre:'Asistencia',ruta:'#'}, {nombre:'Convocatoria', ruta:'#'}]
                    }
                ],
                visibilidad:"d-inline-block"

            });
        } else if (props.rol === 2) {
            Object.assign(state, {
                left_tabs: [{nombre:'Inicio', ruta:'ListaEvaluadores'}, {nombre:'Perfil', ruta:'AsistenciaEvento'}],
                mid_tabs:[
                    {   nombre:"Evaluadores", 
                        opciones:[{nombre:'Postulaciones', ruta:'#'}, {nombre:'Lista de Evaluadores',ruta:'#'}]
                    },
                    {
                        nombre:"Proyectos", 
                        opciones:[{nombre:'Asignacion de Proyectos', ruta:'#'}, {nombre:'Lista de Proyectos',ruta:'#'}]
                    },
                    {
                        nombre:"Evento", 
                        opciones:[{nombre:'Salas', ruta:'#'}, {nombre:'Asistencia',ruta:'#'}]
                    }
                ],
                visibilidad:"d-inline-block"
            });
        } else if (props.rol === 1) {
            Object.assign(state, {
                left_tabs: [{nombre:'Inicio', ruta:'#'}, {nombre:'Perfil', ruta:'#'}],
                mid_tabs:[
                    {
                        nombre:"Proyectos", 
                        opciones:[{nombre:'Primera Etapa', ruta:'#'}, {nombre:'Segunda Etapa',ruta:'#'}]
                    }
                ],
                visibilidad:"d-inline-block"
            });
        } else if(props.rol == 6) {
            Object.assign(state, {
                left_tabs: [{nombre: "Inicio", ruta: "SuperAdminView" }, {nombre: "Informacion delegados", ruta: "ListaDelegados" }],
                visibilidadLogin: "d-none",
            });
        }

        const authStore = useAuthStore(); 
        const router = useRouter(); 

        const selectComponent = (componentName) => {
            console.log(props.rol)
            emit('component-selected', componentName); // Emite un evento para seleccionar el componente
        };

        // Acción para cerrar sesión
        const logout = () => {
        authStore.logout(); 
        router.push('/'); 
        };

        return {
            ...state,
            selectComponent,
            logout
        };
    },
});
</script>

<style scoped>

    /*********************************
                1. General
    *********************************/
    *
    {
        margin: 0;
        padding: 0;
        -webkit-font-smoothing: antialiased;
        -webkit-text-shadow: rgba(0,0,0,.01) 0 0 1px;
        text-shadow: rgba(0,0,0,.01) 0 0 1px;
    }
    body
    {
        font-family: 'Roboto', sans-serif;
        font-size: 14px;
        font-weight: 400;
        background: #FFFFFF;
        color: #a5a5a5;
    }
    div
    {
        display: block;
        position: relative;
        -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
        box-sizing: border-box;
    }
    ul
    {
        list-style: none;
        margin-bottom: 0px;
    }
    p
    {
        font-family: 'Roboto', sans-serif;
        font-size: 14px;
        line-height: 2.29;
        font-weight: 400;
        color: #a5a5a5;
        -webkit-font-smoothing: antialiased;
        -webkit-text-shadow: rgba(0,0,0,.01) 0 0 1px;
        text-shadow: rgba(0,0,0,.01) 0 0 1px;
    }
    p a
    {
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
    a, a:hover, a:visited, a:active, a:link
    {
        text-decoration: none;
        -webkit-font-smoothing: antialiased;
        -webkit-text-shadow: rgba(0,0,0,.01) 0 0 1px;
        text-shadow: rgba(0,0,0,.01) 0 0 1px;
    }
    p a:active
    {
        position: relative;
        color: #FF6347;
    }
    p a:hover
    {
        color: #FFFFFF;
        background: #ffa07f;
    }
    p a:hover::after
    {
        opacity: 0.2;
    }
    ::selection
    {
        background: #FFD266;
        color: #C88E00;
    }
    p::selection
    {
        background: #FFD266;
        color: #C88E00;
    }
    
    .trans_200
    {
        -webkit-transition: all 200ms ease;
        -moz-transition: all 200ms ease;
        -ms-transition: all 200ms ease;
        -o-transition: all 200ms ease;
        transition: all 200ms ease;
    }  
   
    #cont_ejemplo{
        background-color:#ffb606 ;
        padding: 10px;
    }


/*********************************
            Hamburger
*********************************/

    .hamburger_container
    {
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
    .hamburger_container i
    {
        font-size: 24px;
        padding: 10px;
        color: #3a3a3a;
    }
    .hamburger_container:hover i
    {
        color: #ffb606;
    }

/*********************************
3.2 Main Nav
*********************************/

    .main_nav_container
    {
        display: inline-block;
        flex-grow: 3;
        justify-content: space-between;
        margin-left: 55px;
        padding-right: 55px;
        
    }
    .main_nav
    {
        margin-top: 8px;
    }
    .main_nav_item
    {
        display: inline-block;
    }
    .main_nav_item:last-child
    {
        margin-right: 0px;
    }
    .main_nav_item a
    {
        font-family: 'Open Sans', sans-serif;
        font-size: 15px;
        text-transform: uppercase;
        font-weight: 700;
        color: #3a3a3a;
        -webkit-transition: all 200ms ease;
        -moz-transition: all 200ms ease;
        -ms-transition: all 200ms ease;
        -o-transition: all 200ms ease;
        transition: all 200ms ease;
    }
    .main_nav_item a:hover
    {
        color: #ffb606;
    }

/*********************************
            Logo
*********************************/

    .logo_container
    {
        display: inline-block;
        padding-left: 5px;
    }
    .logo img{
        vertical-align: middle;
        max-width: 55px;
        margin-top: 8px;
    }
    .logo span
    {
        font-family: 'Open Sans', sans-serif;
        font-size: 30px;
        font-weight: 900;
        color: #3a3a3a;
        vertical-align: middle;
        text-transform: uppercase;
        margin-left: 2px;
    }

/*********************************
            Header
*********************************/

    .header
    {
        position: fixed;
        top: 0px;
        left: 50%;
        -webkit-transform: translateX(-50%);
        -moz-transform: translateX(-50%);
        -ms-transform: translateX(-50%);
        -o-transform: translateX(-50%);
        transform: translateX(-50%);
        width: 1318px;
        height: 104px;
        background: #FFFFFF;
        z-index: 8;
        -webkit-transition: all 200ms ease;
        -moz-transition: all 200ms ease;
        -ms-transition: all 200ms ease;
        -o-transition: all 200ms ease;
        transition: all 200ms ease;
    }

    .header_content
    {
        width: 100%;
        padding: 1.9rem;
        height: 100%;

    }
    .header_content::before
    {
        display: block;
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        content: '';
        z-index: -1;
    }

    @media only screen and (max-width: 1380px)
    {
        .header
        {
            width: 1200px;
        }
        .header_content
        {
            width: 100%;
        }
        .main_nav_container
        {
            padding-right: 63px;
        }
        .header_side
        {
            width: 219px;
        }
        .header_side span
        {
            font-size: 14px;
        }
        .header_side img
        {
            width: 20px;
            height: 20px;
        }
    }

    @media only screen and (max-width: 1280px)
    {
        .header
        {
            width: 90%;
        }
        .header_content
        {
            width: 100%;
        }
        .header_side
        {
            display: none !important;
        }
        .main_nav_container
        {
            padding-right: 53px;
        }
    }

    @media only screen and (max-width: 1024px)
    {
        .main_nav_item
        {
            margin-right: 33px;
        }
    }

    @media only screen and (max-width: 991px)
    {
        .main_nav_container
        {
            display: none;
        }
        .logo_container
        {
            padding-left: 30px;
        }
        .hamburger_container
        {
            display: block;
        }
    }

    @media only screen and (min-width: 991px) and (max-width: 1161px) 
    {
        .main_nav_container
        {
            display: none;
        }
        .logo_container
        {
            padding-left: 30px;
        }
        .hamburger_container
        {
            display: block;
        }
    }
 
    @media only screen and (max-width: 767px)
    {
        .menu_container
        {
            right: -100vw;
            width: 100vw;
            height: 100vh;
        }
        
    }

    @media only screen and (max-width: 575px)
    {
        h1{font-size: 24px;}
        p{font-size:13px;}
        .header
        {
            height: 74px;
        }
        .logo_container
        {
            padding-left: 15px;
        }
        .logo img
        {
            width: 30px;
        }
        .logo span
        {
            font-size: 16px;
        }
        .hamburger_container
        {
            right: 5px;
        }
        .menu
        {
            top: 70px;
        }
        .menu_item
        {
            margin-bottom: 0px;
        }
        .menu_item a
        {
            font-size: 24px;
        }
        .menu_copyright
        {
            display: none;
        }
        .menu_social_container
        {
            margin-top: 50px;
        }
        .menu_close_container
        {
            right: 30px;
            top: 34px;
        }
    }

    @media only screen and (max-width: 479px)
    {
        .header
        {
            height: 60px;
            top: 15px;
        }
        
    }

</style>