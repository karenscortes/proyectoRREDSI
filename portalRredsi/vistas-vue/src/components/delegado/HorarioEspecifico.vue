<template>
    <div class="container">
        <ComponenteHorario :proyecto="proyecto" :evaluadores="EvaluadoresAsignados" :horario="horario" />
    </div>
</template>

<script>
import ComponenteHorario from './ComponenteHorario.vue';

export default {
    components: {
        ComponenteHorario
    },
    data() {
        return {
            proyecto: {
                codigoProyecto: "AA01",
                titulo: "BigDataIA",
                institucion: "UTP",
                modalidad: "Ciencias Sociales",
                autores: [{ nombre: "Francisco Sanchez" }, { nombre: "Sara Perez" }, { nombre: "Nicolas SinApellido" }, { nombre: "Santiago Alarcón" }],
                areaConocimiento: "Sistemas",
                posiblesEvaluadores: [
                    { nombreEvaluador: "Santa teresita" },
                    { nombreEvaluador: "Nicolas Uribe" }
                ]
            },
            EvaluadoresAsignados: [
                { nombreEvaluador: "Este es el evaluador 1" },
                { nombreEvaluador: "Este es el evaluador 2" }
            ],
            horario: {
                fecha: "28-08-2024",
                hora_inicio: "7:00",
                hora_fin: "8:00"
            }

        }
    }
}

</script>

<style></style>