<template>
  <div class="container pt-5">
    <div class="row mb-5 mt-2">
      <!--Titulo Principal-->
      <div class="col">
        <div class="section_title text-center">
          <h1>Gestionar Cuentas Delegados</h1>
        </div>
      </div>
    </div>

    <div class="row justify-content-center">
      <!-- tabla -->
      <div class="table-responsive row d-flex justify-content-center">
        <table class="display table table-striped table-hover text-dark">
          <thead class="text-center">
            <tr class="cabecero">
              <th class="thTable" colspan="3">
                <!-- Buscador -->
                <div class="row justify-content-start">
                  <div class="col-md-5 col-6">
                    <input
                      type="text"
                      id="busqueda"
                      class="form-control"
                      placeholder="Buscar..."
                    />
                  </div>
                  <div class="col-md-2 col-4">
                    <button class="btn btn-dark w-100 font-weight-bold">
                      Buscar
                    </button>
                  </div>
                </div>
              </th>
              <th class="thTable">
                <a
                  href="#"
                  class="btn-sm font-weight-bold text-dark"
                  type="button"
                  data-toggle="modal"
                  data-target="#createAccount"
                  ><i class="fas fa-plus extra-bold-icon"></i>
                </a>
              </th>
            </tr>
            <tr>
              <th>Usuario</th>
              <th>Institucion</th>
              <th>Estado</th>
              <th>Perfil</th>
            </tr>
          </thead>
          <tbody class="text-center"></tbody>
        </table>
      </div>
    </div>
  </div>
</template>
<style scoped>
.thTable {
  background-color: rgb(255, 182, 6);
}
.extra-bold-icon {
  font-size: 26px; 
  color: black; 
  text-shadow: 1px 1px 0 black, -1px -1px 0 black, -1px 1px 0 black, 1px -1px 0 black;
}
h1{
  color: black;
}
</style>
