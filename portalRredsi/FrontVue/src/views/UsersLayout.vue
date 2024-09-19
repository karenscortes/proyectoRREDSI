<template>
    <MenuUsuarios @component-selected="changeComponent" />
    
    <div class="container mt-5">
        <ComponenteDinamico :currentComponent="currentComponent"/>
    </div>

    <FooterSecundario />
</template>

<script>
import { markRaw, ref } from "vue";
import { useAuthStore } from "@/store";
import MenuUsuarios from '../components/Menus/MenuUsuarios.vue';
import FooterSecundario from '../components/Footers/FooterSecundario.vue';
import ComponenteDinamico from '../components/ComponenteDinamico.vue';
import InicioSuperAdminView from "./InicioSuperAdminView.vue";
import RubricaAdminView from "./RubricaAdminView.vue";
import SalasAdminView from "./SalasAdminView.vue";
import DelegadosAdminView from "./DelegadosAdminView.vue";
import AsignarProyectos from "../components/Users/delegado/AsignarProyectos/AsignarProyectos.vue";
import AsistenciaEvento from "../components/Users/delegado/asistencia/AsistenciaEvento.vue";
import PaginaInicioEvaluadorView from './PaginaInicioEvaluadorView.vue';
import ListaEvaluadores from "../components/Users/delegado/listaEvaluadores/ListaEvaluadores.vue";
import PostulacionesEvaluadores from "../components/Users/delegado/postulaciones/PostulacionesEvaluadores.vue";
import ProyectosAsignadosEvaluadorView from './ProyectosAsignadosEvaluadorView.vue';
import CalificarProyecto from "../components/Users/evaluador/CalificarProyecto.vue";
import ListaAdministradores from '../components/Users/superadmin/ListaAdministradores.vue';
import HistorialActividades from "../components/Users/superadmin/HistorialActividades.vue";
import EditarPerfilSuperAdmin from "../components/Users/superadmin/EditarPerfilSuperAdmin.vue";
import NotAvailable from "./NotAvailable.vue";
import ListaSalasDelegado from "../components/Users/delegado/listaSalas/ListaSalasDelegado.vue";
import ListaProyectosDelegado from "../components/Users/delegado/listaProyectos/ListaProyectosDelegado.vue";


import InicioAdminView from "./InicioAdminView.vue";

// Styles
import '../assets/plugins/fontawesome-free-5.0.1/css/fontawesome-all.css';


export default {
    components: {
        MenuUsuarios: markRaw(MenuUsuarios),
        FooterSecundario: markRaw(FooterSecundario),

        //Componentes Admin
        InicioAdminView: markRaw(InicioAdminView),
        RubricaAdminView: markRaw(RubricaAdminView),
        SalasAdminView: markRaw(SalasAdminView),
        DelegadosAdmin: markRaw(DelegadosAdminView),

        //Componentes Delegado
        AsignarProyectos: markRaw(AsignarProyectos),
        AsistenciaEvento: markRaw(AsistenciaEvento),
        ListaEvaluadores: markRaw(ListaEvaluadores),
        PostulacionesEvaluadores: markRaw(PostulacionesEvaluadores),
        ListaSalasDelegado: markRaw(ListaSalasDelegado),
        ListaProyectosDelegado: markRaw(ListaProyectosDelegado),

        //Componentes Evaluador
        PaginaInicioEvaluadorView: markRaw(PaginaInicioEvaluadorView),
        ProyectosAsignadosEvaluadorView: markRaw(ProyectosAsignadosEvaluadorView),
        CalificarProyecto: markRaw(CalificarProyecto),

        //Componentes SuperAdmin
        InicioSuperAdminView: markRaw(InicioSuperAdminView),
        ListaAdministradores: markRaw(ListaAdministradores),
        HistorialActividades: markRaw(HistorialActividades),
        EditarPerfilSuperAdmin: markRaw (EditarPerfilSuperAdmin),

        //Componente Por defecto
        NotAvailable: markRaw(NotAvailable),

        ComponenteDinamico,
    },
    setup() {

        const authStore = useAuthStore();
        const user = authStore.user;
        const currentComponent = ref(NotAvailable);

        const changeComponent = (componentName) => {
            const componentMap = {
                NotAvailable: NotAvailable,

                //Admin
                InicioAdminView: InicioAdminView,
                RubricaAdminView: RubricaAdminView,
                SalasAdminView: SalasAdminView,
                DelegadosAdminView: DelegadosAdminView,

                //Delegado
                AsignarProyectos: AsignarProyectos,
                AsistenciaEvento: AsistenciaEvento,
                ListaEvaluadores: ListaEvaluadores,
                PostulacionesEvaluadores: PostulacionesEvaluadores,
                ListaSalasDelegado: ListaSalasDelegado,
                ListaProyectosDelegado: ListaProyectosDelegado,


                //Evaluador
                PaginaInicioEvaluadorView: PaginaInicioEvaluadorView,
                ProyectosAsignadosEvaluadorView: ProyectosAsignadosEvaluadorView,
                CalificarProyecto: CalificarProyecto,

                //SuperAdmin
                InicioSuperAdminView: InicioSuperAdminView ,
                ListaAdministradores: ListaAdministradores,
                HistorialActividades: HistorialActividades,
                EditarPerfilSuperAdmin: EditarPerfilSuperAdmin,

            };

            currentComponent.value = componentMap[componentName] || NotAvailable;
        };


        return {
            user,
            currentComponent,
            changeComponent,
        };

    },
    mounted() {
        const script = document.createElement('script');
        script.src = 'src/assets/js/custom.js'; // Ruta del archivo JS
        script.async = true; // Opcional, para cargarlo de forma asíncrona
        document.head.appendChild(script);
    }
}

</script>
<style scoped>
    .container{
        min-height: 600px;
    }
</style>