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
            <InicioPrincipal/>
        </div>
    </div>
</template>


<script>
import InicioPrincipal from '../components/Users/inicio/InicioPrincipal.vue';
export default {
  components: {
    InicioPrincipal,
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