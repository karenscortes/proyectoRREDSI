<template>
<div class="modal fade show" id="modalMensaje"  data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content border border-0 bg-transparent">
            <div class="modal-body" id="container">  
              <!-- para mensajes informativos             -->
                <div id="info-box" v-if="tipo == 1">
                    <div class="face">
                    <div class="eye"></div>
                    <div class="eye right"></div>
                    <div class="mouth surprised"></div>
                    </div>
                    <div class="shadow scale"></div>
                    <div class="message ">
                        <h1 class="alert mb-3">{{ titulo }}</h1>
                        <p>{{ mensaje }}</p>
                    </div>
                    <button type="button" class="button-box mt-2 pt-2" @click="closeModal()"><h1 class="blue fw-bold">okay</h1></button>
                </div>
                <!-- para mensajes de exito -->
                <div id="success-box" v-else-if="tipo == 2">
                  <div class="face2">
                  <div class="eye"></div>
                  <div class="eye right"></div>
                  <div class="mouth happy"></div>
                  </div>
                  <div class="shadow scale"></div>
                  <div class="message ">
                      <h1 class="alert mb-3">{{ titulo }}</h1>
                      <p>{{ mensaje }}</p>
                  </div>
                  <button type="button" class="button-box mt-2 pt-2" @click="closeModal()"><h1 class="green fw-bold">okay</h1></button>
                </div>
                <!-- para mensajes de error -->
                <div id="error-box" v-else-if="tipo == 3">
                    <div class="face3">
                        <div class="eye"></div>
                        <div class="eye right"></div>
                        <div class="mouth sad"></div>
                    </div>
                    <div class="shadow move"></div>
                    <div class="message">
                        <h1 class="alert mb-3">{{ titulo }}</h1>
                        <p>{{ mensaje }}</p>
                    </div>
                    <button class="button-box mt-2 pt-2"  @click="closeModal()"><h1 class="red fw-bold">okay</h1></button>
                </div>
            </div>
        </div>
    </div>
</div>
    
</template>
<script setup>

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
  max-width: 300px; 
  min-width: 300px;
  margin: 0 auto; 
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

.blue{
  color:#5460bc;
}

.green {
  color: #99DBB4;
}

.red {
  color:#EF8D9C;
}

.alert {
  font-weight: 700;
  letter-spacing: 5px;
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
  min-height: 300px;
  background: linear-gradient(to bottom right, #86c1f2 40%, #5460bc 100%);
  border-radius: 40px;
  box-shadow: 5px 5px 20px rgba(#CBCDD3, 10%);

}

#success-box {
  min-width: 100%;
  min-height: 300px;
  background: linear-gradient(to bottom right, #B0DB7D 40%, #99DBB4 100%);
  border-radius: 40px;
  box-shadow: 5px 5px 20px rgba(#CBCDD3, 10%);

}

#error-box {
  min-width: 100%;
  min-height: 300px;
  background: linear-gradient(to bottom left, #EF8D9C 40%,  #e02e49 100%);
  border-radius: 40px;
  box-shadow: 5px 5px 20px rgba(#CBCDD3, 10%);
}

.dot {
  width: 8px;
  height: 8px;
  background: var(--white);
  border-radius: 50%;
  position: absolute;
  top: 4%;
  right: 6%;
}

.dot:hover {
    background: darken(var(--white, 20%));
}

.two {
  right: 12%;
  opacity: .5;
}

.face {
  position: absolute;
  width: 22%;
  height: 22%;
  background: var(--white);
  border-radius: 50%;
  border: 1px solid var(--dark);
  top: 10%;
  left: 37.5%;
  z-index: 2;
  animation: shake 3s ease-in-out infinite;
}

.face2 {
  position: absolute;
  width: 22%;
  height: 22%;
  background: var(--white);
  border-radius: 50%;
  border: 1px solid var(--dark);
  top: 10%;
  left: 37.5%;
  z-index: 2;
  animation: bounce 1s ease-in infinite;
}

.face3 {
  position: absolute;
  width: 22%;
  height: 22%;
  background: var(--white);
  border-radius: 50%;
  border: 1px solid var(--dark);
  top: 10%;
  left: 37.5%;
  z-index: 2;
  animation: roll 3s ease-in-out infinite;
}

.eye {
  position: absolute;
  width: 5px;
  height: 5px;
  background: var(--dark);
  border-radius: 50%;
  top: 40%;
  left: 20%;
}

.right {
  left: 68%;
}

.mouth {
  position:absolute;
  top: 43%;
  left: 41%;
  width: 7px;
  height: 7px;
  border-radius: 50%;
}

.happy {
  border: 2px solid;
  border-color: transparent black black transparent;
  transform: rotate(45deg);
}

.surprised {
  border: 2px solid;
  border-color: black;
  transform: rotate(45deg);
}

.sad {
  top: 49%;
  border: 2px solid;
  border-color: black transparent transparent black;
  transform: rotate(45deg);
}

.shadow {
  position: absolute;
  width: 21%;
  height: 3%;
  opacity: .5;
  background: black;
  left: 40%;
  top: 33%;
  border-radius: 50%;
  z-index: 1;
}

.scale {
  animation: scale 1s ease-in infinite;
}
.move {
  animation: move 3s ease-in-out infinite;
}


.message {
  position: absolute;
  width: 100%;
  text-align: center;
  height: 40%;
  top: 40%;
}

.button-box {
  position: absolute;
  background: var(--white);
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

@keyframes bounce {
  50% {
     transform: translateY(-10px);
  }
}

@keyframes scale {
  50% {
    transform: scale(0.9);
  }
}

@keyframes roll {
  0% {
    transform: rotate(0deg);
    left: 25%;
  }
  50% {
    left: 60%;
    transform: rotate(168deg);
  }
  100% {
    transform: rotate(0deg);
    left: 25%;
  }
}

@keyframes move {
  0% {
    left: 25%;
  }
  50% {
    left: 60%;
  }
  100% {
    left: 25%;
  }
}

@keyframes shake{
  0% {
    transform: rotate(-50deg);
    right: 70%;
  }
  50% {
    transform: rotate(50deg);
  }  
}
</style>