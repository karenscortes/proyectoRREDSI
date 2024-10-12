<template>
    <div class="modal fade show" id="changePasswordModal" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content border border-dark  rounded-5 text-dark">
                <div class="text-center ">
                    <button type="button" class="close mr-3 mt-1 fs-2" @click="closeModal()">
                        <span aria-hidden="true">&times;</span>
                    </button>
                    <h3 class="modal-title mt-5" id="modalLabel">Cambiar Contraseña</h3>
                    
                </div>
                <div class="modal-body mt-3">
                    <form>
                        <div class="form-group row justify-content-center">
                          <label for="colFormLabelSm" class="col-5 col-form-label col-form-label-sm text-center fw-bold">Contraseña Actual: </label>
                          <div class="col-5 pr-5">
                            <input type="password" class="form-control form-control-sm" id="colFormLabelSm">
                          </div>
                        </div>
                        <div class="form-group row justify-content-center">
                            <label for="colFormLabelSm" class="col-5 col-form-label col-form-label-sm text-center fw-bold">Nueva Contraseña: </label>
                            <div class="col-5 pr-5">
                              <input type="password" class="form-control form-control-sm " id="colFormLabelSm">
                              <small id="passwordHelpBlock" class="form-text text-muted w-100">
                                8-20 characters long
                              </small>
                            </div>
                        </div>
                        <div class="form-group row  mb-5 justify-content-center">
                            <label for="colFormLabelSm" class="col-5 col-form-label col-form-label-sm text-center fw-bold">Confirmar Contraseña: </label>
                            <div class="col-5 pr-5">
                              <input type="password" class="form-control form-control-sm " id="colFormLabelSm">
                            </div>
                        </div>
                        <div class="text-center">
                            <button type="submit" class="btn btn-warning font-weight-bold">Guardar Cambios</button>
                        </div>                        
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    emits: ["close"],
    setup(_, { emit }) {
                
        const closeModal = () => {
            emit("close");
        };


        return {
            closeModal
        }
    },
}

</script>
<style scoped>
#changePasswordModal{
    display: block;
}
</style>