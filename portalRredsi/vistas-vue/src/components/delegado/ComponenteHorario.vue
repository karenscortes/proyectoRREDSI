<template>
    <div class="container mt-4">
                    <!-- Encabezado con fecha y botones -->
                    <div class="">
                        <h3 class="text-center m-0">{{ horario.fecha }}</h3>
                    </div>
                    <table class="table table-hover border table-responsive">
                        <thead>
                            <tr id="headerRow">
                                <th class="text-center">Evaluadores</th>
                                <th class="text-center time-slot" data-time="6am">6:00am</th>
                                <th class="text-center time-slot" data-time="6am">6:30am</th>
                                <th class="text-center time-slot" data-time="7am">7:00am</th>
                                <th class="text-center time-slot" data-time="7am">7:30am</th>
                                <th class="text-center time-slot" data-time="8am">8:00am</th>
                                <th class="text-center time-slot" data-time="8am">8:30am</th>
                                <th class="text-center time-slot" data-time="9am">9:00am</th>
                                <th class="text-center time-slot" data-time="9am">9:30am</th>
                                <th class="text-center time-slot" data-time="10am">10:00am</th>
                                <th class="text-center time-slot" data-time="10am">10:30am</th>
                                <th class="text-center time-slot" data-time="11am">11:00am</th>
                                <th class="text-center time-slot" data-time="11am">11:30am</th>
                                <th class="text-center time-slot" data-time="12pm">12:00pm</th>
                                <th class="text-center time-slot" data-time="12pm">12:30pm</th>
                                <th class="text-center time-slot" data-time="1pm">1:00pm</th>
                                <th class="text-center time-slot" data-time="1pm">1:30pm</th>
                                <th class="text-center time-slot" data-time="2pm">2:00pm</th>
                                <th class="text-center time-slot" data-time="2pm">2:30pm</th>
                                <th class="text-center time-slot" data-time="3pm">3:00pm</th>
                                <th class="text-center time-slot" data-time="3pm">3:30pm</th>
                                <th class="text-center time-slot" data-time="4pm">4:00pm</th>
                                <th class="text-center time-slot" data-time="4pm">4:30pm</th>
                                <th class="text-center time-slot" data-time="5pm">5:00pm</th>
                                <th class="text-center time-slot" data-time="5pm">5:30pm</th>
                                <th class="text-center time-slot" data-time="6pm">6:00pm</th>
                                <th class="text-center time-slot" data-time="6pm">6:30pm</th>
                            </tr>
                        </thead>
                        <tbody id="scheduleBody">
                            <tr v-for="(evaluador,index) in evaluadores" :key="index">
                                <td class="text-center">{{ evaluador.nombreEvaluador }}</td>
                                <td style="background-color: rgb(255, 182, 6);">{{ proyecto.titulo }}</td>
                                <td></td>
                                <td></td>
                                <td></td>
                                <td></td>
                                <td></td>
                                <td></td>
                                <td></td>
                                <td></td>
                                <td></td>
                                <td></td>
                                <td></td>
                                <td></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
</template>


<script>
    export default{
        props:{
            evaluadores: Array,
            proyecto: Object,
            horario : Object
        }
    }
</script>