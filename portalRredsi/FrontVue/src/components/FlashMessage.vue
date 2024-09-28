<template>
<div class="modal fade show" id="modalMensaje"  data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content border border-0 bg-transparent">
            <div class="modal-body">  
              <!-- para mensajes informativos             -->
                <div id="info-box" class="border border-5 border-dark">
                    <div class="face">
                        <i class="fa-solid fa-circle-info blue" v-if="tipo == 1"></i>
                        <i class="fa-solid fa-triangle-exclamation green" v-else-if="tipo == 2"></i>
                        <i class="fa-solid fa-circle-xmark red" v-else-if="tipo == 3"></i>
                    </div>
                    <div class="message ">
                        <h1 :class="`${tittle} mb-3`">{{ titulo }}</h1>
                        <p>{{ mensaje }}</p>
                    </div>
                    <button type="button" :class="`${boton} mt-2 pt-2`" @click="closeModal()"><h1 class="text-white fw-bold">okay</h1></button>
                </div>
            </div>
        </div>
    </div>
</div>
    
</template>
<script setup>
import { ref } from "vue";
const props = defineProps({
    tipo: {
        type: Number,
        required: true,
        default:1
    },
    titulo: {
      type: String,
      default: 'Acción Exitosa!'
    },
    mensaje: {
      type: String,
      default: 'Contenido del modal'
    }
});

const boton = ref('button-info');
const title = ref('alert-info');

if(props.tipo == 2){
  boton.value = 'button-success';
  title.value ='alert-success';

}else if(props.tipo == 3){
  boton.value = 'button-error';
  title.value ='alert-error';
}

const emit = defineEmits(['close', 'actualizarRubrica']);
const closeModal = () => {
  emit('close'); 
}
</script>

<style scoped>
:root{
    --white: #FCFCFC;
    --gray: #CBCDD3;
    --dark: #777777;
    --error: #EF8D9C;
    --orange: #FFC39E;
    --success: #FFD266;
    --secondary: #C88E00;
}

#modalMensaje{
  display: block;
  overflow: hidden;
  font-family: 'Roboto', sans-serif;
  text-transform: uppercase;
  text-align: center;
}


.modal-dialog {
  max-width: 315px; 
  min-width: 315px;
  margin: 0 auto; 
}

.blue{
  font-size: 3rem;
  color: #233bf0;
}

.green{
  font-size: 3rem;
  color: #99DBB4;
}

.red{
  font-size: 3rem;
  color: #e02e49;
}

h1 {
  font-size: 15px;
  font-weight: 100;
  letter-spacing: 3px;
  padding-top: 5px;
  color: var(--white);
  padding-bottom: 5px;
  text-transform: uppercase;
}

.alert-info {
  font-weight: 700;
  letter-spacing: 5px;
  color:#233bf0;
}

.alert-success {
  font-weight: 700;
  letter-spacing: 5px;
  color:#99DBB4;
}

.alert-error {
  font-weight: 700;
  letter-spacing: 5px;
  color:#e02e49;
}


p {
  
  font-size: 12px;
  font-weight: 100;
  color: black;
  letter-spacing: 1px;
}

button, .dot {
  cursor: pointer;
}

#info-box {
  min-width: 100%;
  min-height: 315px;
  background: white;
  border-radius: 40px;
  box-shadow: 5px 5px 20px rgba(#CBCDD3, 10%);

}

.face {
  position: absolute;
  width: 22%;
  height: 22%;
  background: white;
  top: 10%;
  left: 37.5%;
  z-index: 2;
}

.message {
  position: absolute;
  width: 100%;
  text-align: center;
  height: 40%;
  top: 30%;
}

.button-info {
  position: absolute;
  background: #233bf0;
  width: 50%;
  height: 15%;
  border-radius: 20px;
  top: 73%;
  left: 25%;
  outline: 0;
  border: none;
  box-shadow: 2px 2px 10px rgba(black, .5);
  transition: all .5s ease-in-out;
}

.button-success {
  position: absolute;
  background: #99DBB4;
  width: 50%;
  height: 15%;
  border-radius: 20px;
  top: 73%;
  left: 25%;
  outline: 0;
  border: none;
  box-shadow: 2px 2px 10px rgba(black, .5);
  transition: all .5s ease-in-out;
}

.button-error {
  position: absolute;
  background: #e02e49;
  width: 50%;
  height: 15%;
  border-radius: 20px;
  top: 73%;
  left: 25%;
  outline: 0;
  border: none;
  box-shadow: 2px 2px 10px rgba(black, .5);
  transition: all .5s ease-in-out;
}


.button-box:hover {
    background: darken(var(--white, 5%));
    transform: scale(1.05);
    transition: all .3s ease-in-out;
}

</style>