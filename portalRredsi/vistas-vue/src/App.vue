<template> 

  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <ListaDelegadosView></ListaDelegadosView>
</template>
<script>
import HelloWorld from './components/HelloWorld.vue';
import ListaDelegadosView from './components/administrador/gest_delegado/ListaDelegadosView.vue';


export default {
  name: 'App',
  components: {
    HelloWorld,
    ListaDelegadosView,
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
