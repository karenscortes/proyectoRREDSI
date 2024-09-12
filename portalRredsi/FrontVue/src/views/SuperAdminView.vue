
<template>
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
    }
  };
  </script>
  