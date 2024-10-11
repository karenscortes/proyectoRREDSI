<template>
    <div class="feature">
        <div class="icon-custom text-center">
            <i class="fa-solid fa-calendar fa-3x"></i>
        </div>
        <h2 class="text-left font-weight-bold text-yellow">Evento</h2>
        <p class="text-dark text-left event-details">
            Fecha: {{ fecha }}<br>
            Horario: {{ obtenerHoraMinutos(horaInicio) }} - {{ obtenerHoraMinutos(horaFin) }}<br>
            Sala: {{ sala }}
        </p>
    </div>
</template>

<script>
export default {
    name: 'EventoComponent',
    props: {
        fecha: {
            type: String,
            required: true,
        },
        horaInicio: {
            type: String,
            required: true,
        },
        horaFin: {
            type: String,
            required: true,
        },
        sala: {
            type: String,
            required: true,
        },
    },
    methods: {
        obtenerHoraMinutos(duracion) {
            duracion = duracion.replace('PT', '');

            let horas = 0;
            let minutos = '00';

            const partesHoras = duracion.split('H');

            if (partesHoras.length > 1) {
                horas = parseInt(partesHoras[0]);
                duracion = partesHoras[1];
            }
            if (duracion.includes('M')) {
                minutos = parseInt(duracion.split('M')[0]);
            }
            minutos = minutos.toString().padStart(2, '0');

            // Convertir a formato de 12 horas y agregar AM/PM
            const isPM = horas >= 12;
            const horasFormato12 = horas % 12 || 12; 
            const ampm = isPM ? 'PM' : 'AM';

            return `${horasFormato12}:${minutos} ${ampm}`;
        },
    },
};
</script>

<style scoped>
.icon-custom {
    color: #ffb606;
    margin-bottom: 0.5rem;
}

.text-yellow {
    color: #ffb606;
}

h2 {
    font-size: 1.1rem;
    margin-bottom: 5px;
}

.event-details {
    font-size: 0.8rem; 
    color: #000; 
}

.text-left {
    text-align: left;
}

p {
    margin-bottom: 0.5rem;
}
</style>
