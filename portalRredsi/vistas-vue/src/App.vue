<template>
  
  <PaginaPrincipalView/>

</template>

<script>

import PaginaPrincipalView from './views/PaginaPrincipalView.vue';

export default {
  name: 'App',
  components: {
    PaginaPrincipalView
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
