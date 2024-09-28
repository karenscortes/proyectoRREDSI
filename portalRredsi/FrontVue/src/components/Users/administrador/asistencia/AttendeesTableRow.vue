<template>
    <tr class="text-center">
        <td>{{ infoAsistente.documento}}</td>
        <td>{{ infoAsistente.nombres}} {{ infoAsistente.apellidos }}</td>
        <td>{{ infoAsistente.celular }}</td>
        <td>{{ infoAsistente.correo }}</td>
        <td style="vertical-align: middle;">
            <a :href="infoAsistente.url_comprobrante_pago" target="_blank" style="color: black;">
                <i class="fas fa-eye fa-2x"></i>
            </a>
        </td>   
        <td style="vertical-align: middle;">
            <a href="#" class="btn-sm font-weight-bold text-dark" type="button" @click="openModal()">
                <i class="fas fa-edit fa-2x"></i>
            </a>
        </td>
    </tr>
  </template>
  <script setup>
    const props = defineProps({
      infoAsistente: {
        type: Object,
        required: true,
        validator(value) {
          return (
            typeof value.id_usuario === 'number' &&
            typeof value.documento === 'string' &&
            typeof value.nombres === 'string' &&
            typeof value.apellidos === 'string' &&
            typeof value.celular === 'string' &&
            typeof value.correo === 'string' && 
            typeof value.url_comprobrante_pago === 'string'
          );
        },
      },
      index: {
        type: Number,
        required: true
      }
    })

    const emit = defineEmits("open");
    const openModal = () => emit("open", props.infoAsistente);
  
  </script>
  <style>
  .form-check{
    padding-left: 2.5rem;
  }
  .form-check-input{
    border: 1px solid rgb(187, 187, 187);
  }
  .form-check-input:focus{
    border: 1px solid rgb(187, 187, 187);
  }
  </style>