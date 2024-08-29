<template>
    <div class="container mt-4">
        <!-- Encabezado con fecha -->
        <div class="">
            <h3 class="text-center m-0">{{ horario.fecha }}</h3>
        </div>
        <table class="table table-hover border table-responsive">
            <thead>
                <tr>
                    <th class="text-center">Evaluadores</th>
                    <th class="text-center">6:00am</th>
                    <th class="text-center">6:30am</th>
                    <th class="text-center">7:00am</th>
                    <th class="text-center">7:30am</th>
                    <th class="text-center">8:00am</th>
                    <th class="text-center">8:30am</th>
                    <th class="text-center">9:00am</th>
                    <th class="text-center">9:30am</th>
                    <th class="text-center">10:00am</th>
                    <th class="text-center">10:30am</th>
                    <th class="text-center">11:00am</th>
                    <th class="text-center">11:30am</th>
                    <th class="text-center">12:00pm</th>
                    <th class="text-center">12:30pm</th>
                    <th class="text-center">1:00pm</th>
                    <th class="text-center">1:30pm</th>
                    <th class="text-center">2:00pm</th>
                    <th class="text-center">2:30pm</th>
                    <th class="text-center">3:00pm</th>
                    <th class="text-center">3:30pm</th>
                    <th class="text-center">4:00pm</th>
                    <th class="text-center">4:30pm</th>
                    <th class="text-center">5:00pm</th>
                    <th class="text-center">5:30pm</th>
                    <th class="text-center">6:00pm</th>
                    <th class="text-center">6:30pm</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(evaluador, index) in evaluadores" :key="index">
                    <td class="text-center">{{ evaluador.nombreEvaluador }}</td>
                    <td v-for="slot in timeSlots" :key="slot" :style="getSlotStyle(slot)">
                        <span v-if="isProjectScheduled(slot)">{{ proyecto.titulo }}</span>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
    props: {
        evaluadores: Array,
        proyecto: Object,
        horario: Object
    },
    computed: {
        timeSlots() {
            const slots = [];
            for (let hour = 6; hour <= 18; hour++) {
                for (let half = 0; half < 2; half++) {
                    const minutes = half === 0 ? "00" : "30";
                    slots.push(`${hour.toString().padStart(2, '0')}:${minutes}`);
                }
            }
            return slots;
        }
    },
    methods: {
        getSlotStyle(slot) {
            if (slot >= this.horario.hora_inicio && slot <= this.horario.hora_fin) {
                return "background-color: rgb(255, 182, 6);";
            }
            return "";
        },
        isProjectScheduled(slot) {
            return slot >= this.horario.hora_inicio && slot <= this.horario.hora_fin;
        }
    }
}
</script>
