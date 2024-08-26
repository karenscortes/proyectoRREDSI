<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <ContainerMain></ContainerMain>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
import ContainerMain from './components/administrador/rubricas/ContainerMain.vue';
export default {
  name: 'App',
  components: {
    HelloWorld,
    ContainerMain,
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
