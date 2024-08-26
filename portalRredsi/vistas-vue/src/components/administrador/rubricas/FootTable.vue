<template>
  <tr class="tr_item_rubrica">
    <td class="td_boton text-center" colspan="3">
      <h2>Puntaje total:</h2>
    </td>

    <td class="td_valor_max"></td>
    <td class="td_calificacion"></td>
    <td class="td_observacion"></td>
  </tr>
  <tr class="tr_item_rubrica">
    <td class="td_boton" colspan="3">
      <h2>Nombre del evaluador:</h2>
    </td>
    <td class="td_valor_max"></td>
    <td class="td_calificacion"></td>
    <td class="td_observacion">
      <h2>Cédula:</h2>
    </td>
  </tr>
  <tr class="tr_item_rubrica">
    <td class="td_boton" colspan="3">
      <h2>
        Universidad:
      </h2>
    </td>
    <td class="td_valor_max"></td>
    <td class="td_calificacion"></td>
    <td class="td_observacion"></td>
  </tr>
  <tr class="tr_item_rubrica">
    <td class="td_boton" colspan="3">
      <h2>Email:</h2>
    </td>

    <td class="td_valor_max"></td>
    <td class="td_calificacion"></td>
    <td class="td_observacion">
      <h2>Celular:</h2>
    </td>
  </tr>
</template>
<script></script>
<style scoped>
.td_valor_max {
  width: 5%;
}
.td_calificacion {
  width: 25%;
}
.td_observacion {
  width: 25%;
}
.tr_rubrica {
  border-bottom: 1px solid black;
}
h2 {
  text-transform: uppercase;
  font-size: 15px;
  font-weight: bold;
}
.tr_item_rubrica {
  border-bottom: 1px solid black;
}

.tr_item_rubrica > td {
  border-right: 1px solid black;
  text-align: start;
}
</style>
