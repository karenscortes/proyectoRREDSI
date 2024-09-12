
<template>
<<<<<<< HEAD
  <div>
    <!-- HEADER -->
    <MenuPrincipal :rol="user?.id_rol" />

    <main class="content mt-5">
      <!-- Componente dinámico -->
      <DynamicComponentSuperAdmin :currentComponent="currentComponent" />
    </main>

    <footer class="bg-dark mt-5 text-white text-center py-3">
      <h2>ESTE ES EL FOOTER</h2>
    </footer>
  </div>
</template>

<script>
import { markRaw } from 'vue';
import MenuPrincipal from '../components/Menus/MenuPrincipal.vue';
import InicioSuperAdminView from './InicioSuperAdminView.vue';


import DynamicComponentSuperAdmin from '../components/Users/superadmin/DynamicComponentSuperAdmin.vue';
import { useAuthStore } from '@/store';
import { useRouter } from 'vue-router';

export default {
  components: {
    DynamicComponentSuperAdmin,
    MenuPrincipal: markRaw(MenuPrincipal),
    InicioSuperAdminView: markRaw(InicioSuperAdminView)

  },
  data() {
    return {
        currentComponent: InicioSuperAdminView
    };
  },
  methods: {
    changeComponent(componentName) {
      const componentMap = {
        
      };
      
=======
    <!-- Título -->
        <div class="row mb-5 mt-2">
          <div class="col">
            <div class="section_title text-center">
              <h1>Información delegados</h1>
            </div>
          </div>
        </div>
  
        <!-- Buscador -->
        <div class="row mb-4 justify-content-end">
          <div class="col-8 col-sm-6">
            <div class="row justify-content-end">
              <div class="col-8">
                <input type="text" v-model="busqueda" class="form-control" placeholder="Buscar...">
              </div>
              <div class="col-4">
                <button class="btn w-100 font-weight-bold" style="background: rgb(255, 182, 6);" @click="buscarDelegado">
                  Buscar
                </button>
              </div>
            </div>
          </div>
        </div>
    <div class="table-responsive">
      <table id="basic-datatables" class="display table table-striped table-hover text-dark">
        <thead class="bg-warning">
          <tr>
            <th class="bg-warning">Identificación</th>
            <th class="bg-warning">Delegado</th>
            <th class="bg-warning">Área de conocimiento</th>
            <th class="bg-warning">Institución</th>
            <th class="bg-warning">Estado</th>
            <th class="bg-warning">Detalle</th>
            <th class="bg-warning">Historial</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(delegado, index) in delegados" :key="index">
            <td>{{ delegado.identificacion }}</td>
            <td>{{ delegado.delegado }}</td>
            <td>{{ delegado.areaConocimiento }}</td>
            <td>{{ delegado.institucion }}</td>
            <td>
              <div class="form-check form-switch">
                <input class="form-check-input bg-warning border-warning" type="checkbox" role="switch" :checked="delegado.estado">
              </div>
            </td>
            <td>
              <a @click="emitirDelegadoSeleccionado(delegado)" type="button" data-bs-toggle="modal" data-bs-target="#detalleModal">
                <i class="far fa-eye" style="font-size: 25px;"></i>
              </a>
            </td>
            <td>
              <a @click="emitirDelegadoSeleccionado(delegado)" type="button" data-bs-toggle="modal" data-bs-target="#historialModal">
                <i class="far fa-list-alt" style="font-size: 25px;"></i>
              </a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

  </template>
  
  <script>
  import FooterPrincipal from '../components/Footers/FooterPrincipal.vue';

  export default {
    components: {
      FooterPrincipal
    },
    props: {
      delegados: Array
    },
    methods: {
      emitirDelegadoSeleccionado(delegado) {
        this.$emit('delegadoSeleccionado', delegado);
      }
>>>>>>> origin
    }
  },
  setup() {
    const authStore = useAuthStore();
    const router = useRouter();

    const user = authStore.user;
    const permissions = authStore.permissions;

    const logout = () => {
      authStore.logout();
      router.push('/');
    };

    return {
      user,
      permissions,
      logout
    };
  }
};
</script>

<style scoped>
.content {
  padding-top: 100px;
}
</style>
