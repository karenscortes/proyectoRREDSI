<template>
  <!--Modal confirmación eliminar rúbrica-->
  <div
    class="modal fade"
    id="modalEliminar"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    tabindex="-1"
    aria-labelledby="staticBackdropLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered" style="max-width: 25%">
      <div class="modal-content rounded-st-1 shadow-lg modal-responsiven">
        <button
          type="button"
          class="btn-close"
          data-bs-dismiss="modal"
          aria-label="Close"
        ></button>
        <div class="modal-body">
          <form action="">
            <div class="row">
              <div class="col-md-12 mb-4">
                <h2 class="mensaje_body">
                  ¿Seguro que quieres eliminar este ítem?
                </h2>
              </div>
            </div>
          </form>
        </div>
        <div
          class="modal-footer"
        >
          <button class="btn mx-auto" data-bs-dismiss="modal">
            Cancelar
          </button>
          <button class="btn mx-auto" data-bs-dismiss="modal">
            Aceptar
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<style scoped>
.btn-close{
    margin-left: auto
}
.mensaje_body{
    font-size: 24px; color: black
}
.btn{
  background-color: rgb(255, 182, 6);
  font-weight: 700;
}
.btn:focus{
  border: none;
  box-shadow: none;
  color: #494949;
  background-color: rgb(255, 182, 6);
}
.modal-footer{
    border: 1px solid yellow;
}
@media only screen and (min-width: 500px) and (max-width: 768px) {
  .modal-dialog {
    min-width: 97%;
  }
}
</style>
