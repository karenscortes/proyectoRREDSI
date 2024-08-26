<template>
  <div class="card">
    <h2 class="title">{{ tituloCard }}</h2>
    <img
      :src="require(`@/assets/${nombreImagen}`)"
      class="img-fluid w-25 pb-2"
      :alt="altImagen"
    />

    <div class="card-body">
      <!--info rubrica-->
      <div class="pb-1 mb-2">
        <h6 class="card-subtitle mb-2">Fase de proyecto:</h6>
        <p class="card-text">{{ etqFaseProyecto }}</p>
      </div>
      <div>
        <h6 class="card-subtitle mb-2">Modalidad proyecto:</h6>
        <p class="card-text">{{ etqModalidadProyecto }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  setup() {
    //Propiedades
    const tituloCard = "1";
    const nombreImagen = "logo.png";
    const altImagen = "imagen_ejemplo";
    const etqModalidadProyecto = "En curso";
    const etqFaseProyecto = "Presencial";

    return {
      tituloCard,
      nombreImagen,
      etqModalidadProyecto,
      etqFaseProyecto,
      altImagen,
    };
  },
};
</script>

<style scoped>
.card-subtitle {
  font-weight: bold;
}
.card {
  display: block;
  border-radius: 30px;
  height: auto;
  cursor: pointer;
  border: 2px solid black;
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
  border: 2px solid rgb(255, 217, 3);
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
