<template>
    <div class="col-xl-4 col-md-6 col-sm-12 align-items-center">
        <ul class="cards justify-content-center">
            <li>
                <a class="card">
                    <div class="text-center pt-5 card__image">
                        <a :href="proyecto.url_propuesta_escrita" class="d-inline-flex" target="_blank">
                            <button type="button" class="btn btn-warning rounded-circle border border-dark mx-2">
                                <i class="far fa-file-alt h3"></i>
                            </button>
                        </a>
                        <button type="button" class="btn btn-warning rounded-circle border border-dark mx-2" @click="selectComponent('CalificarProyectoEvaluadorView', proyecto)">
                            <i class="fa-solid fa-list-check fa-xl"></i>
                        </button>
                    </div>
                    <div class="card__overlay">
                        <div class="card__header">
                            <svg class="card__arc" xmlns="http://www.w3.org/2000/svg">
                                <path d="M 40 80 c 22 0 40 -22 40 -40 v 40 Z"/>
                            </svg>
                            <div class="border border-white text-white card__thumb text-center pt-3">
                                <h2>{{ proyecto.id_proyecto }}</h2>
                            </div>
                            <div class="card__header-text text-justify">
                                <h3 class="text-left texto-recortado">{{ proyecto.titulo }}</h3>
                                <h4 class="text-left texto-recortado">{{ proyecto.institucion }}</h4>
                            </div>
                        </div>
                        <div class="card__footer text-center">
                            <div>
                                <p class="card__description"><strong>Modalidad:</strong> {{ proyecto.modalidad }}</p>
                                <p class="card__description"><strong>Estado:</strong> {{ proyecto.estado_evaluacion }}</p>
                            </div>
                        </div>
                    </div>
                </a>
            </li>
        </ul>
    </div>
</template>

<script>
    import { defineComponent } from 'vue';

    export default defineComponent({
        props: {
            proyecto: {
                type: Object,
                required: true
            }
        },
        emits: ['component-selected'],
        methods: {
            selectComponent(componentName, proyecto) {
                this.$emit('component-selected', { componentName, proyecto });
            }
        }
    });
</script>


<style>
    :root {
        --surface-color: rgb(255, 182, 6);
        --curve: 40;
    }
</style>

<style scoped> 
    .texto-recortado {
        width: 200px; 
        overflow: hidden;
        display: -webkit-box;
        -webkit-box-orient: vertical;
        -webkit-line-clamp: 2; 
        line-clamp: 2;
        text-overflow: ellipsis;
    }
  
    div {
        display: block;
        position: relative;
        -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
        box-sizing: border-box;
    }

    ul {
        list-style: none;
        margin-bottom: 0px;
    }

    p {
        font-family: 'Roboto', sans-serif;
        font-size: 14px;
        line-height: 2.29;
        font-weight: 400;
        color: #a5a5a5;
        -webkit-font-smoothing: antialiased;
        -webkit-text-shadow: rgba(0,0,0,.01) 0 0 1px;
        text-shadow: rgba(0,0,0,.01) 0 0 1px;
    }

    p a {
        display: inline;
        position: relative;
        color: inherit;
        border-bottom: solid 1px #ffa07f;
        -webkit-transition: all 200ms ease;
        -moz-transition: all 200ms ease;
        -ms-transition: all 200ms ease;
        -o-transition: all 200ms ease;
        transition: all 200ms ease;
    }
  
    p a:active {
        position: relative;
        color: #FF6347;
    }

    p a:hover {
        color: #FFFFFF;
        background: #ffa07f;
    }

    p a:hover::after {
        opacity: 0.2;
    }

    ::selection {
        background: #FFD266;
        color: #C88E00;
    }

    p::selection {
        background: #FFD266;
        color: #C88E00;
    }
  
    h1 { font-size: 33px; }
    h2 { font-size: 22px; }
    h3 { font-size: 18px; }
    h4 { font-size: 14px; }
    h5 { font-size: 11px; }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Roboto', sans-serif;
        -webkit-font-smoothing: antialiased;
        -webkit-text-shadow: rgba(0,0,0,.01) 0 0 1px;
        text-shadow: rgba(0,0,0,.01) 0 0 1px;
    }
  
    .card {
        border-radius: 30px; 
        height: auto; 
        cursor: default;
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

    .card:hover {
        color: black !important;
    }

    .card-text {
        font-size: 13px;
        font-weight: 500;
        color: #4e4e4e;
        margin-top: -12px;
    }
</style>
  
<style src="../../../assets/Styles/listaProyectos_evaluadorEtapa2_styles.css" scoped></style>