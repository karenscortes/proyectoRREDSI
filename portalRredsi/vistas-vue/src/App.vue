<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <HistorialActividades></HistorialActividades>
  <ProyectosAsignados numeroProyecto="2"/>
</template>

<script>
import ProyectosAsignados from './components/evaluador/ProyectosAsignados.vue';
import HelloWorld from './components/HelloWorld.vue';
import HistorialActividades from './components/superadmin/HistorialActividades.vue';
export default {
  name: 'App',
  components: {
    HelloWorld,
    HistorialActividades,
    ProyectosAsignados
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
