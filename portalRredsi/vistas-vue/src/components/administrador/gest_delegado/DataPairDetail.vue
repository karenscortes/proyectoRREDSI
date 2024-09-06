<template>
  <div>
    <div class="col-5 text-dark font-weight-bold">{{ info.p_dato }}:</div>
    <div class="col-5 border mb-3">
      <span class="text-dark" id="conocimiento">{{ info.p_valor }}</span>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    info: {
      type: Object,
      required: true,
      validator(value) {
        return (
          typeof value.p_dato === "string" &&
          typeof value.p_valor === "string"
        );
      },
    },
  },
  setup() {},
};
</script>
