<template>
    <div class="col col-10 col-sm-6 col-lg-4 mb-3">
        <div class="card shadow-lg border rounded-3">
            <div class="card-header d-flex align-items-center justify-content-between text-dark">
                <div>
                    <strong class="mb-0 text-white h4">{{ cod_proyecto }}</strong>
                </div>
                <div class="mb-3 bg-warning">
                    <input class="form-check-input mr-2" type="checkbox" value="" id="estado">
                </div>

            </div>
            <div class="card-body">
                <h4 class="text-lg mt-2">{{ titulo }}</h4>
                <p class="mt-2">{{ institucion }}</p>
            </div>
            <div class="card-footer">
                <div class="d-flex flex-column text-center">
                    <strong class="text-muted mb-1" style="line-height: 1;">{{ estado }}</strong>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        cod_proyecto:String,
        titulo: String,
        institucion: String,
        estado: String,
    },
};
</script>

<style>
.card {
    width: 300px;
    height: 200px;
}

.card-header {
    background: rgb(255, 182, 6);
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
}

.card-footer{
    box-shadow: 0px -2px 4px rgba(0, 0, 0, 0.1);
}
</style>