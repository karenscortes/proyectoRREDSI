<template>

    <div class="container-fluid">

        <!-- 404 Error Text -->
        <div class="row justify-content-center informative_msg" style="height: 600px;">
            <div class="col-6 align-content-center">
                <div class="row text-center" style="height: 200px;">
                    <h1 class="error mx-auto" data-text="503">503</h1>
                    <h2 class="lead text-gray-800">Servicio No Disponible</h2>
                    <p class="text-gray-500 mb-0">Ups... Desafortunadamente, parece que algo salió mal. Intenta de nuevo más tarde.</p>
                </div>
            </div>
        </div>

    </div>

</template>
<script>
export default {
  data() {
    return {
      lipsCount: 8 // Número de labios
    };
  }
};
</script>
<style scoped>
    .informative_msg h1 , h2
    {
        display: block;
        color: #1a1a1a;
        font-weight: 500;
        padding-top: 24px;
    }
    h1{
        font-size: 7rem;
    }
</style>