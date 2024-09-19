<template>
  <tr>
    <td>{{ infoSala.p_numSala }}</td>
    <td>{{ infoSala.p_areaConocimiento }}</td>
    <td>{{ infoSala.p_delegado }}</td>
    <td>
      <a type="button"
          @click="accionEditar(infoSala)"
        ><i class="far fa-edit"></i
      ></a>
    </td>
  </tr>
</template>
<script>
export default{
  props: {
    //Objeto con la informacion de la sala asignada
    infoSala: {
      type: Object,  
      required: true,
      validator(value){
        return(
          typeof value.p_idDelegado === 'number' &&
          typeof value.p_delegado === 'string' &&
          typeof value.p_idSala === 'number' &&
          typeof value.p_numSala === 'string' &&
          typeof value.p_idAreaConocimiento === 'number' &&
          typeof value.p_areaConocimiento === 'string'
        );
      }
    }
  },
  //Evento para avisarle a la vista rúbrica principal
  emits: ['editarRow'],
  setup(props, { emit }) { 
    const accionEditar = () => {

      emit('editarRow', props.infoSala); 
    };
    return { accionEditar };
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
