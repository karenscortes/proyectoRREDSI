<template>
    <div class="col col-10 col-sm-6 col-lg-4 mb-3">
        <div class="card shadow-lg border rounded-3">
            <div class="card-header d-flex align-items-center justify-content-between text-dark">
                <div>
                    <strong class="mb-0 text-white h4">{{ proyecto.id_proyecto }}</strong>
                </div>
                <div class="mb-3 bg-warning">
                    <input class="form-check-input mr-2" type="checkbox" value="" id="estado">
                </div>

            </div>
            <div class="card-body">
                <h3 class="text-lg mt-2">{{proyecto.titulo }}</h3>
                <p class="mt-2">{{ proyecto.institucion }}</p>
            </div>
            <div class="card-footer">
                <div class="d-flex flex-column text-center">
                    <strong class="text-muted mb-1" style="line-height: 1;">{{ proyecto.estado }}</strong>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "CardProyectos",
    props: {
        proyecto: Object,
        index: Number 
    }
};
</script>

<style>
.card {
    width: 100%;
    max-width: 300px;
    height: 260px; 
    display: flex;
    flex-direction: column;
}

.card-header {
    background: rgb(255, 182, 6);
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
    padding: 8px;
}

.card-body {
    flex-grow: 1; 
    overflow: hidden; 
    min-height: 100px; 
    max-height: 150px; 
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.card-body h4 {
    font-size: 1rem; 
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap; 
}

.card-footer {
    padding: 8px;
    font-size: 0.8rem;
    box-shadow: 0px -2px 4px rgba(0, 0, 0, 0.1);
    height: 50px; 
}
</style>

