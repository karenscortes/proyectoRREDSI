<template>
  <tr class="text-center">
    <td>{{ infoDelegado.nombres}} {{ infoDelegado.apellidos }}</td>
    <td>{{ infoDelegado.nombre_institucion }}</td>
    <td>
      <div class="form-check form-switch">
        <input
          class="form-check-input td_check"
          :checked="infoDelegado.estado == 'activo'"
          @change="cambiarEstado()"
          type="checkbox"
          id="estado"
        />
      </div>
    </td>
    <td class="text-center">
      <a
        href="#"
        class="btn-sm font-weight-bold text-dark"
        type="button"
        @click="openModal()"
      >
        <i class="far fa-address-card h4"></i>
      </a>
    </td>
  </tr>
</template>
<script setup>
  const props = defineProps({
    infoDelegado: {
      type: Object,
      required: true,
      validator(value) {
        return (
          typeof value.id_usuario === 'number' &&
          typeof value.nombres === 'string' &&
          typeof value.apellidos === 'string' &&
          typeof value.tipo_documento === 'string' &&
          typeof value.documento === 'string' &&
          typeof value.nombre_institucion === 'string' &&
          typeof value.primer_area === 'string' &&
          typeof value.segunda_area === 'string' &&
          typeof value.url_titulo === 'string' &&
          typeof value.estado  === 'string' &&
          typeof value.celular === 'string' &&
          typeof value.correo === 'string' 
        );
      },
    },
    index: {
      type: Number,
      required: true
    }
})
//Definiendo los eventos que emitiran a el componente padre. 
const emit = defineEmits(["open", "check"]);
const openModal = () => emit("open", props.infoDelegado);
const cambiarEstado = () => emit("check", props.index);
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