<template>
    <div>
        <div class="container mt-4">
            <div class="my-3 row">
                <div class="col-4">
                    <h2 class="text-dark fs-3">SALA {{ sala.numero_sala }}</h2>
                </div>
                <div class="col-4">
                    <h2 class="text-dark fs-3 text-center">{{ sala.nombre_sala }}</h2>
                </div>
            </div>
            <div>
                <strong class="fs-5">Delegado: </strong><span class="fs-5">{{ sala.nombres_delegado }} {{ sala.apellidos_delegado }}</span>
            </div>
            <div class="mt-3">
                <h3 class="text-center mb-3">Sep 6 de 2024</h3>
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

                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        sala: Object,
        index: Number
    },
}
</script>