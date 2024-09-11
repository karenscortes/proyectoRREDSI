<template>
  <tr>
    <td>{{ infoSala.numSala }}</td>
    <td>{{ infoSala.areaConocimiento }}</td>
    <td>{{ infoSala.delegado }}</td>
    <td>
      <a type="button"
          data-bs-toggle="modal"
          data-bs-target="#editSala"
        ><i class="far fa-edit"></i
      ></a>
    </td>
  </tr>
</template>
<script>
export default{
  props: {
    infoSala: {
      type: Object,  
      required: true,
      validator(value){
        return(
          typeof value.delegado === 'string' &&
          typeof value.numSala === 'string' &&
          typeof value.areaConocimiento == 'string'
        );
      }
    }
  }
}
</script>
<style>
td{
  font-size: 16px
}
i{
  font-size: 25px
}
</style>
