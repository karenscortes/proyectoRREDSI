<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <ListaDelegados></ListaDelegados>
  
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
import ListaDelegados from './components/superadmin/ListaDelegados.vue';

export default {
  name: 'App',
  components: {
    HelloWorld,
    ListaDelegados

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
