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
                    <form @submit.prevent="changePassword()">
                        <div class="form-group row justify-content-center">
                          <label for="colFormLabelSm" class="col-5 col-form-label col-form-label-sm text-center fw-bold">Contraseña Actual: </label>
                          <div class="col-5 pr-5">
                            <input v-model="CurrentPass" type="password" class="form-control form-control-sm" id="colFormLabelSm">
                          </div>
                        </div>
                        <div class="form-group row justify-content-center">
                            <label for="colFormLabelSm" class="col-5 col-form-label col-form-label-sm text-center fw-bold">Nueva Contraseña: </label>
                            <div class="col-5 pr-5">
                              <input v-model="NewPass" type="password" class="form-control form-control-sm " id="colFormLabelSm">
                            </div>
                        </div>
                        <div class="form-group row  mb-5 justify-content-center">
                            <label for="colFormLabelSm" class="col-5 col-form-label col-form-label-sm text-center fw-bold">Confirmar Contraseña: </label>
                            <div class="col-5 pr-5">
                              <input v-model="Confirmation" type="password" class="form-control form-control-sm " id="colFormLabelSm">
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
import {ref} from 'vue';
import { useToastUtils } from '@/utils/toast';
import { resetPassword } from '../../services/UsuarioService';

export default {
    props:{
        email:{
            type: String,
            required: true
        }
    },
    emits: ["close"],
    setup(props, { emit }) {
        const { showErrorToast,showInfoToast,showSuccessToast} = useToastUtils();
        const CurrentPass = ref('');
        const NewPass = ref('');
        const Confirmation = ref('');

                
        const closeModal = () => {
            emit("close");
        };

        const changePassword = async()=>{
            if(NewPass.value!=Confirmation.value){
                showInfoToast('Las Contraseñas no coinciden');
            }else if(NewPass.value == CurrentPass.value){
                showInfoToast('La Contraseña nueva es igual a la actual');
            }else{
                try{
                    await resetPassword(CurrentPass.value,NewPass.value,props.email);
                    showSuccessToast('Contraseña restablecida con éxito')
                }catch{
                    showErrorToast('Error en restablecer contraseña')
                }
            }
        }

        return {
            closeModal,
            CurrentPass,
            NewPass,
            Confirmation,
            changePassword
        }
    },
}

</script>
<style scoped>
#changePasswordModal{
    display: block;
}
</style>