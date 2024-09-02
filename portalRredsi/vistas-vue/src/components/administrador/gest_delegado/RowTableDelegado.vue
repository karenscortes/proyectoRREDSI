<template>
  <tr class="text-center">
    <td>{{ infoDelegado.p_nombres}} {{ infoDelegado.p_apellidos }}</td>
    <td>{{ infoDelegado.p_institucion }}</td>
    <td>
      <div class="form-check form-switch">
        <input
          class="form-check-input td_check"
          :checked="infoDelegado.p_estado == 'activo'"
          @change="handleCheckboxChange()"
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
<script>
export default {
  props: {
    infoDelegado: {
      type: Object,
      required: true,
      validator(value) {
        return (
          typeof value.p_idDelegado === "number",
          typeof value.p_nombres === "string" &&
          typeof value.p_apellidos === "string" &&
          typeof value.p_institucion === "string" &&
          typeof value.p_estado === "string" &&
          typeof value.p_tipoDocumento === "string" &&
          typeof value.p_documento === "string" &&
          typeof value.p_areaConocimiento === "string" &&
          typeof value.p_telefono == "string" &&
          typeof value.p_correo === "string" 
        );
      },
    },
    index: {
      type: Number,
      required: true
    }
  },
  emits: ["open", "check"],
  setup(props, { emit }){
    const openModal = () => {
      emit("open");
    };
    const handleCheckboxChange = () => emit("check", props.index);
    return {openModal, handleCheckboxChange};
  },
};
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