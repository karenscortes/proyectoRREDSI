<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div class="events page_section mb-5">
        <div class="container">
            <div class="row mt-0">
                <div class="col">
                    <div class="section_title text-center">
                        <h1>Próximos eventos</h1>
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
                                    <div class="event_location">{{ event.location }}</div>
                                    <p>{{ event.description }}</p>
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

<script>
export default {
    data() {
        return {
            events: [
                {
                    day: "02",
                    month: "Marzo",
                    name: "Incripciones abiertas",
                    location: "Portal rredsi",
                    description:
                        "In aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempor nisl ligula vel nunc. Proin quis mi malesuada, finibus tortor.",
                    image: "../plantilla/images/event_1.jpg",
                    alt: "Event Image 1",
                },
                {
                    day: "12",
                    month: "Mayo",
                    name: "Primera publicación de resultados",
                    location: "Portal rredsi",
                    description:
                        "In aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempor nisl ligula vel nunc. Proin quis mi malesuada, finibus tortor.",
                    image: "../plantilla/images/event_2.jpg",
                    alt: "Event Image 2",
                },
                {
                    day: "22",
                    month: "Junio",
                    name: "Evento presencial",
                    location: "Auditorio Jorge Roa",
                    description:
                        "In aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempor nisl ligula vel nunc. Proin quis mi malesuada, finibus tortor.",
                    image: "../plantilla/images/event_3.jpg",
                    alt: "Event Image 3",
                },
                {
                    day: "30",
                    month: "Junio",
                    name: "Segunda publicación de resultados",
                    location: "Portal rredsi",
                    description:
                        "In aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempor nisl ligula vel nunc. Proin quis mi malesuada, finibus tortor.",
                    image: "../plantilla/images/event_2.jpg",
                    alt: "Event Image 4",
                },
            ],
        };
    },
};
</script>

<style scoped>
/* General Section Styles */
.events {
    padding: 50px 0;
}

.section_title h1 {
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 30px;
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