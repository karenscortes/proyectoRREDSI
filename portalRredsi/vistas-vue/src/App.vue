<template> 

  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <ListaSalasView></ListaSalasView>
</template>
<script>
import HelloWorld from './components/HelloWorld.vue';
import ListaSalasView from './components/administrador/salas/ListaSalasView.vue';
export default {
  name: 'App',
  components: {
    HelloWorld,
    ListaSalasView,
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
