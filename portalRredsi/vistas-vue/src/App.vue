<template> 

  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <MenuUsuarios rol="Delegado"></MenuUsuarios>
</template>
<script>
import HelloWorld from './components/HelloWorld.vue';
import MenuUsuarios from './components/menus/MenuUsuarios.vue';


export default {
  name: 'App',
  components: {
    HelloWorld,
    MenuUsuarios,
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
