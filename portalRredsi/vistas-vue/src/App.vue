<template> 

  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <CalificarProyecto 
  tituloProyecto="Gestión de los sistemas financieron de la agricultura colombiana"
  ponentesProyecto="Johan Sebastian Usma Sanchez, Luisa Fernanda Agudelo"
  universidadProyecto="Universidad de los andes"
  nombreEvaluador="Miguel Angel"
  cedulaEvaluador="108810252754"
  universidadEvaluador="Univesidad Tecnológica de Pereira"
  emailEvaluador="miguelito@gmail.com"
  celularEvaluador="3008914235"
  />
</template>

<script>
import CalificarProyecto from './components/evaluador/CalificarProyecto.vue';
import HelloWorld from './components/HelloWorld.vue';
export default {
  name: 'App',
  components: {
    HelloWorld,
    CalificarProyecto
  }
}
</script>

<style>
* {
  font-family: 'Roboto', sans-serif
}
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
