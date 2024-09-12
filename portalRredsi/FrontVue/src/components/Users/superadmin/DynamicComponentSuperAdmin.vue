<template>
    <!-- Render dinámico basado en el valor de currentComponent -->
    <component :is="currentComponent"></component>
  </template>
  
  <script>
  export default {
    props: {
      currentComponent: {
        type: [String, Object], // Acepta tanto nombres de componentes como objetos
        required: true
      }
    }
  };
  </script>
  