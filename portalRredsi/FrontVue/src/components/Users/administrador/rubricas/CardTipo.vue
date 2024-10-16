<template>
  <div class="card" @click="oprimir()">
    <img
      src=/src/assets/img/rubrica.png
      class="img-fluid w-50 pb-2 pt-3"
      alt="Imagen rubrica"
    />

    <div class="card-body">
      <!--info rubrica-->
      <div class="mb-2">
        <h6 class="card-subtitle mb-2">Etapa:</h6>
        <p class="card-text">{{ infoCard.nombreEtapa }}</p>
      </div>
      <div>
        <h6 class="card-subtitle mb-2">Modalidad:</h6>
        <p class="card-text">{{ infoCard.nombreModalidad }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  infoCard: {
    type: Object,
    required: true,
    validator(value) {
      return (
        typeof value.nombreModalidad === "string" &&
        typeof value.nombreEtapa === "string" && 
        typeof value.id_rubrica === 'number'
      );
    }
  }
});

const emit = defineEmits(["cardSeleccionada"]);

const oprimir = () => {
  emit("cardSeleccionada", props.infoCard.id_rubrica);
};
</script>

<style scoped>
.card-subtitle {
  font-weight: bold;
  font-size: 15px;
}
.card {
  display: block;
  border-radius: 30px;
  height: auto;
  cursor: pointer;
  border: 4px solid black;
  margin-top: 10px;
}

@keyframes dance {
  0%,
  100% {
    transform: translateX(0);
  }
  25% {
    transform: translateX(-4px);
  }
  50% {
    transform: translateX(4px);
  }
  75% {
    transform: translateX(-4px);
  }
}

.card:hover {
  border: 4px solid rgb(255, 217, 3);
  animation: dance 0.5s ease-in-out;
}

.col_card {
  padding-left: 16px;
  padding-right: 16px;
  padding-top: 10px;
}
.card-img-top {
  border-top-left-radius: 0px;
  border-top-right-radius: 0px;
}
.card-body {
  padding-top: 0px;
  padding-bottom: 0px;
}
.card-title {
  margin-top: 10px;
}
.card-title a {
  font-size: 22px;
  font-weight: 500;
  color: #1a1a1a;
  line-height: 1.2;
}
.card-title a:hover {
  color: #a5a5a5;
}
.card-text {
  font-size: 13px;
  font-weight: 500;
  color: #4e4e4e;
  margin-top: -12px;
}
</style>
