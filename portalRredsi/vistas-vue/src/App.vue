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
  :componentes="[
      { titulo: 'Resumen', descripcion: 'Debe contener una exposición clara y concisa de la propuesta de investigación (máximo 120 palabras) y Palabras Claves. ', valorMaximo: 10, calificacion: 0, observaciones: '' },
      { titulo: 'Referente Teórico', descripcion: 'Mínimo dos autores con una pequeña contextualización del aporte teórico a la propuesta de investigación.', valorMaximo: 15, calificacion: 0, observaciones: '' },
      { titulo: 'Resultados esperados', descripcion:'Productos de investigación o pertinencia de los resultados esperados con los objetivos propuestos.', valorMaximo: 20, calificacion: 0, observaciones: '' },
      { titulo: 'Testeo', descripcion:'Esto es un testing.', valorMaximo: 20, calificacion: 0, observaciones: '' }
    ]"
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
