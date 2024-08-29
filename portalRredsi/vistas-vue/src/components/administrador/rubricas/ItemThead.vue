<template>
  <tr class="tr_rubrica align-items-center">
    <td class="titulo_rubrica">{{ titulo }}</td>
    <td colspan="5" class="text-center">
      <input type="text" :name="name_imput" :id="id" class="form-control rounded-5" />
    </td>
  </tr>
</template>
<script>
export default {
  props:{
    titulo:{
      type: String,
      require
    },
    name_imput: {
      type: String,
      require
    },
    id: {
      type: Number,
      require
    }
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
