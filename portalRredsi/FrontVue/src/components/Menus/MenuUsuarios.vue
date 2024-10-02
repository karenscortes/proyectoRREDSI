<template>
    <header class="header d-flex flex-row position-relative">
        <div class="topbar_content d-flex flex-row align-items-center justify-content-start">

            <div class="logo_container">
                <div class="logo">
                    <img class="img-fluid" src="../../assets/img/logoRredsi.png" alt="">
                    <span>RREDSI</span>
                </div>
            </div>

            <nav class="main_nav_container">
                <div class="main_nav">
                    <ul class="main_nav_list d-flex justify-content-between">
                        <li class="main_nav_item" v-for="(tab, index) in left_tabs" :key="index"><a href="#" @click="selectComponent(tab.ruta)">{{ tab.nombre }}</a></li>
                        <li :class="['main_nav_item', visibilidad]" v-for="(tab, index) in mid_tabs" :key="index">
                            <div class="dropdown">
                                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    {{ tab.nombre }}
                                </a>
                                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                                <li v-for="(opcion, index) in tab.opciones" :key="index"><a href="#"  :class="['dropdown-item', opcion.uso, 'text-center']" aria-disabled="true" @click="selectComponent(opcion.ruta)">{{ opcion.nombre }}</a></li>
                                </ul>
                            </div>
                        </li>

                        
                        <li class="main_nav_item" v-if="user.id_rol === 1"><a href="#" @click="selectComponent('ConvocatoriaInfoPageView')">Convocatoria</a></li>
                        <li class="main_nav_item"><a href="#" @click="logout">Cerrar Sesión</a></li>
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

    <!-- Sidebar -->
    <div class="menu_container menu_mm">

        <!-- Menu Close Button -->
        <div class="menu_close_container">
            <div class="menu_close"></div>
        </div>

        <!-- Menu Items -->
        <div class="menu_inner menu_mm">
            <div class="menu menu_mm">
                <ul class="menu_list menu_mm ">
                    <li class="menu_item menu_mm"  v-for="(tab, index) in left_tabs" :key="index"><a href="#" @click="selectComponent(tab.ruta)">{{ tab.nombre }}</a></li>
                    <li :class="['menu_item menu_mm d-block ', visibilidad]" v-for="(tab, index) in mid_tabs" :key="index">
                        <div class="dropdown menu_mm">
                            <a class="nav-link dropdown-toggle menu_mm" href="#" id="navbarDropdown" role="button" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                                {{ tab.nombre }}
                            </a>
                            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                                <li v-for="(opcion, index) in tab.opciones" :key="index"><a href="#" :class="['dropdown-item', opcion.uso]" aria-disabled="true" @click="selectComponent(opcion.ruta)">{{ opcion.nombre }}</a></li>
                            </ul>
                        </div>
                    </li>
                    <li class="menu_item menu_mm" v-if="user.id_rol === 1"><a href="#" @click="selectComponent('ConvocatoriaInfoPageView')">Convocatoria</a></li>
                    <li class="menu_item menu_mm"><a href="#"  @click="logout">Cerrar sesión</a></li>
                </ul>

                <!-- Menu Social -->

                <div class="menu_social_container menu_mm">
                    <ul class="menu_social menu_mm">
                        <li class="menu_social_item menu_mm"><a href="https://www.instagram.com/rredsiquindio/"><i
                                    class="fab fa-instagram"></i></a></li>
                        <li class="menu_social_item menu_mm"><a
                                href="https://www.facebook.com/rredsi?mibextid=ZbWKwL"><i
                                    class="fab fa-facebook-f"></i></a></li>
                        <li class="menu_social_item menu_mm"><a href="https://x.com/Rredsi"><i
                                    class="fab fa-twitter"></i></a></li>
                    </ul>
                </div>

                <div class="menu_copyright menu_mm">ADSO 2670586 All rights reserved</div>
            </div>

        </div>

    </div>
</template>

<script>
import { obtenerFechasAsignaciones} from '@/services/delegadoService'
import { ref, onMounted} from "vue";
import { defineComponent,reactive } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/store";
import FlashMessage from '../FlashMessage.vue';

export default defineComponent({
    emits: ['component-selected'],
    components: {
        FlashMessage, // Registra el componente FlashMessage
    },
    setup(_,{emit}) {
        //propiedades para las opciones  del menú que se habilitan dependiendo dde la convocatoria en curso y sus fases 
        const asignacion1 = ref('disabled');
        const asignacion2 = ref('disabled');
        const otras_opciones = ref('');
        
        //obteniendo fecha actual
        const currentDate = ref(new Date().toISOString().split('T')[0]);

        //objeto reactivo que obtendrán las opciones del menú según el usuario logueado        
        const state = reactive({
            left_tabs: [],
            mid_tabs: [],
            visibilidad: "d-none",
        });

        //Se obtiene la info del usuario logueado
        const authStore = useAuthStore(); 
        const router = useRouter(); 
        const user = authStore.user;

        //Se obtiene y compara fechas de asignaciones y convocatoria con fecha actual
        const getAssignmentDates = async () => {
            try {
                const fechas = await obtenerFechasAsignaciones();
                if(currentDate.value >= fechas.data.call_period.fecha_inicio && currentDate.value <= fechas.data.call_period.fecha_fin)
                {
                    if(currentDate.value >= fechas.data.virtual_stage.inicio_virtual && currentDate.value <= fechas.data.virtual_stage.fin_virtual){
                        asignacion1.value='';
                    }
                    if(currentDate.value >= fechas.data.in_person_stage.inicio_presencial){
                        asignacion2.value='';
                    }
                }else{
                    otras_opciones.value = 'disabled';
                }

            } catch (error) {
                otras_opciones.value = 'disabled'
            }
        };

        if (user?.id_rol === 3) {
            Object.assign(state, {
                left_tabs: [{nombre:'Inicio', ruta:'InicioAdminView'}, {nombre:'Perfil', ruta:'PerfilAdmin'}, {nombre:'Cuentas', ruta:'DelegadosAdminView'},{nombre:'Rubricas', ruta:'RubricaAdminView'}],
                mid_tabs:[
                    {   nombre:"Eventos", 
                        opciones:[{nombre:'Salas', ruta:'SalasAdminView'}, {nombre:'Asistencia',ruta:'GestionarAsistentes'}, {nombre:'Convocatoria', ruta:'CrearConvocatoria'}]
                    }
                ],
                visibilidad:"d-inline-block"

            });
        } else if (user?.id_rol === 2) {
            
            Object.assign(state, {
                left_tabs: [{nombre:'Inicio', ruta:'PaginaInicioDelegado', uso: ''}, {nombre:'Perfil', ruta:'EditarPerfil', uso: ''}],
                mid_tabs:[
                    {   nombre:"Evaluadores", 
                        opciones:[{nombre:'Postulaciones', ruta:'PostulacionesEvaluadores', uso: otras_opciones}, {nombre:'Lista de Evaluadores',ruta:'ListaEvaluadores', uso: ''}]
                    },
                    {
                        nombre:"Proyectos", 
                        opciones:[{nombre:'Asignación de Proyectos', ruta:'AsignarProyectos',uso: asignacion1 }, {nombre:'Lista de Proyectos',ruta:'ListaProyectosDelegado', uso: otras_opciones}]
                    },
                    {
                        nombre:"Evento", 
                        opciones:[{nombre:'Salas', ruta:'ListaSalasDelegado',uso: asignacion2}, {nombre:'Asistencia',ruta:'AsistenciaEvento',uso: asignacion2}]
                    }
                ],
                visibilidad:"d-inline-block"
            });
            
        } else if (user?.id_rol === 1) {
            Object.assign(state, {
                left_tabs: [{nombre:'Inicio', ruta:'PaginaInicioEvaluadorView'}, {nombre:'Perfil', ruta:'EditarPerfil'}, {nombre:'Proyectos', ruta:'ProyectosAsignadosEvaluadorView'}],
                visibilidad:"d-none"
            });
        } else if(user?.id_rol == 6) {
            Object.assign(state, {
                left_tabs: [{nombre: "Inicio", ruta: "InicioSuperAdminView" }, {nombre: "Editar perfil", ruta: "EditarPerfil" },{nombre: "Gestionar Administradores", ruta: "ListaAdministradores" }],
                visibilidad: "d-none",
            });
        }

        const selectComponent = (componentName) => {
            emit('component-selected', componentName); // Emite un evento para seleccionar el componente
        };

        onMounted(() => {
            getAssignmentDates();
        });

        // Acción para cerrar sesión
        const logout = () => {
            authStore.logout(); 
            router.push('/'); 
        };      
        
        return {
            user,
            ...state,
            getAssignmentDates,
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
    a.disabled {
        pointer-events: none;  
        opacity: 0.5;          
        color:#a5a5a5;        
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
4. Menu
*********************************/

.menu_container {
	position: fixed;
	top: 0;
	right: -50vw;
	width: 50vw;
	height: 100vh;
	background: #FFFFFF;
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
	font-family: 'Open Sans', sans-serif;
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
	content: '';
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
4.1 Menu Social
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
4.2 Menu copyright
*********************************/

.menu_copyright {
	margin-top: 60px;
	margin-left: 5px;
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
}

.menu_container.active .menu_copyright {
	-webkit-transform: translateY(0px);
	-moz-transform: translateY(0px);
	-ms-transform: translateY(0px);
	-o-transform: translateY(0px);
	transform: translateY(0px);
	opacity: 1;
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
    .main_nav_item:last-child{
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

    .topbar_content
    {
        width: 100%;
        padding: 1.9rem;
        height: 100%;

    }
    .topbar_content::before
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
        .topbar_content
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
        .topbar_content
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