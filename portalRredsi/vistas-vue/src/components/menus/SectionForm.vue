<!-- src/components/SectionForm.vue -->
<template>
    <div :id="id" class="section-form mt-4">
      <h4 class="text-dark"><i :class="icon"></i> {{ title }}</h4>
      <slot></slot> <!-- Contenido de la sección -->
    </div>
  </template>
  
  <script>
  export default {
    props: {
      id: {
        type: String,
        required: true,
      },
      title: {
        type: String,
        required: true,
      },
      icon: {
        type: String,
        required: true,
      },
    },
  };
  </script>
  
  <style scoped>
  .section-form {
    padding: 15px;
    border: 1px solid #ccc;
    border-radius: 8px;
    margin-bottom: 20px;
  }
  </style>
  