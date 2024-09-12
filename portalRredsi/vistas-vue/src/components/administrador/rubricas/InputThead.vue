<template>
  <tr class="tr_rubrica align-items-center">
    <td class="titulo_rubrica">{{ infoImputs.p_titulo }}</td>
    <td colspan="5" class="text-center">
      <input type="text" :name="infoImputs.p_name_imput" :id="infoImputs.p_id" class="form-control rounded-5" />
    </td>
  </tr>
</template>
<script>
export default {
  props:{
    infoImputs: {
      type: Object,  
      required: true,
      validator(value){
        return(
          typeof value.p_titulo === 'string' &&
          typeof value.p_name_imput === 'string' &&
          typeof value.p_id == 'string'
        );
      }
    },
  }
};
</script>
<style scoped>
.form-control {
  height: 35px;
  border: 1px solid black;
}
.table-bordered-dark tr:first-child td {
  border-top: 1px solid black;
}
.titulo_rubrica {
  font-size: 18px;
  font-weight: bold;
  text-align: center;
}
</style>
