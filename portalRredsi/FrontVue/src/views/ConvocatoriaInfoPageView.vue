<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div class="events">
        <div class="container">
            <div class="row mt-0">
                <div class="col">
                    <div class="section_title text-center">
                        <h1>Información de la convocatoria</h1>
                    </div>
                </div>
            </div>
            <div class="event_items">
                <div v-for="(event, index) in events" :key="index" class="row event_item">
                    <div class="col">
                        <div class="row d-flex flex-row align-items-end">
                            <div class="col-lg-2 order-lg-1 order-2">
                                <div class="event_date d-flex flex-column align-items-center justify-content-center ">
                                    <div class="event_day">{{ event.day }}</div>
                                    <div class="event_month">{{ event.month }}</div>
                                </div>
                            </div>
                            <div class="col-lg-6 order-lg-2 order-3 ">
                                <div class="event_content">
                                    <div class="event_name p-3">
                                        <a class="trans_200" href="#">{{ event.name }}</a>
                                    </div>
                                    <p class="fs-6">{{ event.description }}</p>
                                </div>
                            </div>
                            <div class="col-lg-4 order-lg-3 order-1">
                                <div class="event_image">
                                    <img :src="event.image" :alt="event.alt" />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<!-- <template>
    <div class="events">
        <div class="container">
            <div class="row mt-0">
                <div class="col">
                    <div class="section_title text-center">
                        <h1>Información de la convocatoria</h1>
                        <h2 class="text-muted">{{ tituloEtapa }}</h2>  Título dinámico 
                    </div>
                </div>
            </div>
            <div class="event_items">
                <div v-for="(fases, index) in listaFases" :key="index" class="row event_item">
                    <div class="col">
                        <div class="row d-flex flex-row align-items-end">
                            <div class="col-lg-2 order-lg-1 order-2">
                                <div class="event_date d-flex flex-column align-items-center justify-content-center ">
                                    <div class="event_day">{{ fases.fecha_inicio }}</div>
                                    <div class="event_month">{{ fases.month }}</div> 
                                </div>
                            </div>
                            <div class="col-lg-6 order-lg-2 order-3 ">
                                <div class="event_content">
                                    <div class="event_name p-3">
                                        <a class="trans_200" href="#">{{ fases.nombre_fase }}</a>
                                    </div>
                                     <p class="fs-6">{{ event.description }}</p>
                                </div>
                            </div>
                            <div class="col-lg-4 order-lg-3 order-1">
                                <div class="event_image">
                                    <img :src="imagenes[index]" :alt="event.alt" />
                                </div> 
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template> -->


<script>
    import {obtenerProgramacionFases, obtenerEtapaActual}  from '../services/evaluadorService';
    import { useToastUtils } from '@/utils/toast'; 

    const { showErrorToast, showInfoToast } = useToastUtils();

    export default {
        data() {
            return {
                listaFases: [],
                currentEtapa: '', // Almacena la etapa actual
                events: [
                    {
                        day: "30",
                        month: "Mayo",
                        name: "Asignaciones",
                        location: "Portal rredsi",
                        description:
                        "En esta etapa se asignarán los proyectos a los evaluadores más adecuados según su perfíl académico y area de conocimiento. Cada evaluador recibirá los detalles correspondientes del proyecto.",
                        image: new URL('@/assets/img/event_1.jpg', import.meta.url).href,
                        alt: "Event Image 1",
                    },
                    {
                        day: "22",
                        month: "Junio",
                        name: "Evento",
                        location: "Auditorio Jorge Roa",
                        description:
                        "Este evento presencial reunirá a los evaluadores y participantes para las ponencias de los proyectos. Los evaluadores deberán emitir su evaluación final durante el evento, ya que es la fecha límite para calificar.",
                        image: new URL('@/assets/img/event_3.jpg', import.meta.url).href,
                        alt: "Event Image 3",
                    },
                    {
                        day: "30",
                        month: "Junio",
                        name: "Publicación de resultados",
                        location: "Portal rredsi",
                        description:
                        "Una vez recopiladas todas las evaluaciones, los resultados finales serán publicados para que los participantes puedan consultarlos. Los resultados estarán disponibles en el portal de RREDSI.",
                        image: new URL('@/assets/img/news_3.jpg', import.meta.url).href,
                        alt: "Event Image 4",
                    },
                ],
            };
        },
        computed: {
            // Computed para el título dinámico
            tituloEtapa() {
                return this.currentEtapa === 'Virtual' ? 'Primera Etapa' : 'Segunda Etapa';
            }
        },
        methods: {
            async obtenerFases() {
                try {

                    // Obtener etapa actual
                    const response2 = await obtenerEtapaActual();
                    this.currentEtapa = response2.nombre_etapa; // Asignar la etapa


                    const response = await obtenerProgramacionFases(this.currentEtapa);
                    this.listaFases = response.data; 

               

                    showInfoToast("Fases de la convocatoria obtenidas con éxito");
                    
                } catch (error) {
                    console.log(error);
                    showErrorToast("Error al obtener las fases de la convocatoria");
                }
            },
        },
        mounted() {
            this.obtenerFases();
        },
    };
</script>

<style scoped>

    .text-muted {
        font-size: 1.2rem;
        color: #999;
    }


    /* Event Items */
    .event_items {
        margin-top: 30px;
    }

    .event_item {
        margin-bottom: 30px;
        padding: 20px;
        border-bottom: 1px solid #e5e5e5;
    }

    .event_date {
        width: 100px;
        height: 100px;
        background-color: #fff;
        border: 2px solid #ffb400;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        font-family: Arial, sans-serif;
    }

    .event_day {
        font-size: 28px;
        font-weight: bold;
        color: #ffb400;
    }

    .event_month {
        font-size: 16px;
        color: #ffb400;
    }

    /* Event Content */
    .event_content {
        margin-left: 20px;
    }

    .event_name a {
        font-size: 20px;
        font-weight: bold;
        color: #333;
        text-decoration: none;
        transition: color 0.3s;
        cursor: default;
    }

    .event_name a:hover {
        color: #ffb400;
    }

    .event_location {
        font-size: 16px;
        color: #666;
        margin-bottom: 10px;
    }

    /* Event Image */
    .event_image {
        width: 100%;
        height: auto;
        overflow: hidden;
        border-radius: 5px;
    }

    .event_image img {
        width: 100%;
        height: auto;
        object-fit: cover;
    }

</style>