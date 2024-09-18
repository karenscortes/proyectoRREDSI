<template>
    <div class="col-lg-4 teacher">
        <div class="card">
            <div class="card-header d-flex align-items-center justify-content-between text-dark"
                style="background: rgb(255, 182, 6); box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);">
                <strong class="mb-0 text-white h4">{{ sala.numero_sala }}</strong>
            </div>
            <div class="card-img">
                <div class="card_plus trans_200 text-center"><a @click="selectComponent('DetalleSala',sala)">+</a></div>
                <img class="card-img-top trans_200" src="@/assets/img/tiempo.png" alt="imagen_tiempo">
            </div>
            <div class="card-body text-center">
                <div class="card-title">{{ sala.nombres_delegado }} {{ sala.apellidos_delegado }}</div>
                <div class="card-text">{{ sala.nombre_area_conocimiento }} </div>
            </div>
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
    props: {
        sala: Object,
        index: Number
    },
    emits: ['component-selected'],
    methods: {
            selectComponent(componentName,sala) {
                this.$emit('component-selected', componentName,sala);
            }
        }
});
</script>


<style scoped>
.teacher {
    margin-bottom: 20px;
}

.card {
    display: block;
    border: none;
    background: #f8f9fb;
    width: 250px;
    height: auto;
    margin: 0 auto;
}

.card:hover .card-img-top {
    background: #1a1a1a;
    opacity: 0.6;
}

.card:hover .card_plus {
    visibility: visible;
    opacity: 1;
    transform: translate(-50%, -50%) scale(1);
}

.card-img {
    padding: 10px;
    position: relative;
    text-align: center;
}

.card-img-top {
    max-width: 100%;
    max-height: 80px;
    width: auto;
    height: auto;
    margin: 0 auto;
    display: block;
}

.card-header {
    padding: 10px 15px;
    font-size: 14px;
}

.card-header .h4 {
    font-size: 20px;
    margin: 0;
}

.card_plus {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0.5);
    width: 75px;
    height: 75px;
    background: #ffb606;
    z-index: 10;
    cursor: pointer;
    visibility: hidden;
    opacity: 0;
}

.card_plus a {
    display: block;
    font-size: 24px;
    line-height: 75px;
    color: #FFFFFF;
}

.card-body {
    padding: 5px;
    border-radius: 10px;
    box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
    margin: 10px 0;
}

.card-title {
    margin-top: 5px;
    font-size: 22px;
    font-weight: 500;
    color: #1a1a1a;
    line-height: 1.4;
}

.card-text {
    font-size: 14px;
    font-weight: 500;
    color: #a5a5a5;
    margin-top: 5px;
}

.teacher_social {
    margin-top: 34px;
}
</style>