<template>
  <tr class="tr_item_rubrica">
    <td class="td_item">
      <div>
        <h4 class="d-inline-block mb-0 me-1">{{ infoItem.titulo }}</h4>
        <span>
          {{ infoItem.componente }}
        </span>
      </div>
    </td>
    <td class="td_boton">
      <!--Boton editar-->
      <button class="botones_rubrica" @click="accionEditar()">
        <i class="fas fa-edit"></i>
      </button>
    </td>
    <td class="td_boton text-center">
      <!--Boton eliminar-->
      <button
        class="botones_rubrica" @click="accionEliminar()"
      >
        <i class="fas fa-trash-alt"></i>
      </button>
    </td>
    <td class="td_valor_max text-center">{{ infoItem.valor_max }}</td>
    <td class="td_calificacion"></td>
    <td class="td_resultado"></td>
  </tr>
</template>

<script setup>
import { reactive } from 'vue';

const props = defineProps({
  infoItem: {
    type: Object,
    required: true,
    validator(value) {
      return (
        typeof value.id_item_rubrica === "number" &&
        typeof value.id_rubrica === "number" &&
        typeof value.titulo === "string" &&
        typeof value.componente === "string" &&
        typeof value.valor_max === "number"
      );
    },
  },
});

const infoEliminar = reactive({
  'id_rubrica': props.infoItem.id_rubrica, 
  'id_item_rubrica': props.infoItem.id_item_rubrica,
});

const emit = defineEmits(["editarItem", "eliminarItem"]);

const accionEditar = () => {
  emit("editarItem", props.infoItem);
};

const accionEliminar = () => {
  emit("eliminarItem", infoEliminar); 
}
</script>

<style scoped>
td {
  line-height: 19px;
  font-family: "Roboto", sans-serif;
}
i {
  font-size: 24px;
}
.td_boton {
  vertical-align: middle !important;
  width: 5%;
}
.botones_rubrica {
  width: 40px;
  height: 40px;
  border: none;
  border-radius: 5px;
  background-color: rgb(255, 182, 6);
}
h4 {
  font-size: 16px;
  font-family: "Roboto", sans-serif;
  font-weight: 600;
}
.btn {
  font-size: 16px;
  font-family: "Roboto", sans-serif;
  font-weight: 600;
}
.tr_item_rubrica {
  border-bottom: 1px solid black;
}
.tr_item_rubrica > td {
  border-right: 1px solid black;
  text-align: start;
}
span {
  font-size: 15px;
}
.td_item {
  width: 30%;
}
.td_valor_max {
  width: 5%;
}
.td_calificacion {
  width: 25%;
}
.td_resultado {
  width: 25%;
}
</style>
