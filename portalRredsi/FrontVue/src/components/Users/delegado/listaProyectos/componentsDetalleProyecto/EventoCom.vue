<template>
    <div class="feature">
        <div class="icon">
            <i class="fa-solid fa-person-booth fa-1.5x text-dark mb-3"></i>
        </div>
        <h2 class="text-dark text-left font-weight-bold">Evento</h2>
        <p class="text-dark text-left">
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
            // Remover "PT" del inicio de la cadena
            duracion = duracion.replace('PT', '');

            let horas = 0;
            let minutos = '00';

            const partesHoras = duracion.split('H');

            if (partesHoras.length > 1) {
                // Si hay una parte con 'H', extraer las horas
                horas = parseInt(partesHoras[0]);
                duracion = partesHoras[1];  // El resto contiene minutos
            } else {
                duracion = partesHoras[0];
            }

            // Dividir la parte restante por la letra 'M' para obtener los minutos
            if (duracion.includes('M')) {
                minutos = parseInt(duracion.split('M')[0]);
            }

            // Formatear minutos para que siempre tenga dos dígitos
            minutos = minutos.toString().padStart(2, '0');

            // Convertir a formato militar y agregar AM/PM
            const isPM = horas >= 12;
            const horasFormato12 = horas % 12 || 12; // Ajustar horas para formato 12
            const ampm = isPM ? 'PM' : 'AM';

            return `${horasFormato12}:${minutos} ${ampm}`;
        },

    },
};
</script>


<style scoped>
h2 {
    font-size: 0.8rem;
    margin-bottom: 2px;
}

.text-left {
    text-align: left;
}
</style>