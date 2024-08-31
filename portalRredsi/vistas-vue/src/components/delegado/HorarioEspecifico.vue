<template>
    <div class="container">

        <!-- Tabla de horarios -->
        <div class="container mt-4">
            <div class="row justify-content-around">
                <div class="col-2">
                    <button class="btn btn-dark">
                        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                            fill="#e8eaed">
                            <path d="M400-80 0-480l400-400 71 71-329 329 329 329-71 71Z" />
                        </svg>
                    </button>
                </div>
                <div class="col-8">
                    <h3 class="text-center m-0">{{ today }}</h3>
                </div>
                <div class="col-2">
                    <button class="btn btn-dark">
                        <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="#e8eaed"><path d="m321-80-71-71 329-329-329-329 71-71 400 400L321-80Z"/></svg>
                    </button>
                </div>

            </div>
            <table class="table table-hover border table-responsive">
                <thead>
                    <tr>
                        <th class="text-center">Evaluadores</th>
                        <th v-for="time in timeSlots" :key="time" class="text-center time-slot">{{ time }}</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(evaluador, index) in evaluadores" :key="index">
                        <td class="text-center">{{ evaluador.nombreEvaluador }}</td>
                        <td v-for="(slot, i) in 24" :key="i"
                            :style="getStyle(i, evaluador.proyecto.inicio, evaluador.proyecto.fin)">
                            <span v-if="isProjectTime(i, evaluador.proyecto.inicio, evaluador.proyecto.fin)">
                                {{ evaluador.proyecto.titulo }}
                            </span>
                        </td>
                    </tr>
                </tbody>
                <tfoot>
                    <tr>
                        <th class="text-center text-secondary">Evaluadores</th>
                        <th v-for="time in timeSlots" :key="time" class="text-center  text-secondary time-slot">{{ time }}</th>
                    </tr>
                </tfoot>
            </table>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            evaluadores: [
                {
                    nombreEvaluador: "Christian Arce",
                    proyecto: {
                        titulo: "A001",
                        inicio: this.calcularPosicion("8:00am"),
                        fin: this.calcularPosicion("9:00am")
                    }
                },
                {
                    nombreEvaluador: "Maribel Obando",
                    proyecto: {
                        titulo: "A001",
                        inicio: this.calcularPosicion("8:00am"),
                        fin: this.calcularPosicion("9:00am")
                    }
                },
                {
                    nombreEvaluador: "Diego Legarda",
                    proyecto: {
                        titulo: "A002",
                        inicio: this.calcularPosicion("9:35am"),
                        fin: this.calcularPosicion("11:00am")
                    }
                },
                {
                    nombreEvaluador: "Christian Gonzalez",
                    proyecto: {
                        titulo: "A002",
                        inicio: this.calcularPosicion("9:30am"),
                        fin: this.calcularPosicion("11:00am")
                    }
                },
                {
                    nombreEvaluador: "Maria Antonieta",
                    proyecto: {
                        titulo: "A003",
                        inicio: this.calcularPosicion("11:30am"),
                        fin: this.calcularPosicion("12:30pm")
                    }
                },
                {
                    nombreEvaluador: "Juan Perez",
                    proyecto: {
                        titulo: "A003",
                        inicio: this.calcularPosicion("11:30am"),
                        fin: this.calcularPosicion("12:30pm")
                    }
                },
                {
                    nombreEvaluador: "Luis Ramirez",
                    proyecto: {
                        titulo: "A004",
                        inicio: this.calcularPosicion("7:00am"),
                        fin: this.calcularPosicion("8:30am")
                    }
                },
                {
                    nombreEvaluador: "Ana Torres",
                    proyecto: {
                        titulo: "A004",
                        inicio: this.calcularPosicion("7:00am"),
                        fin: this.calcularPosicion("8:30am")
                    }
                },
                {
                    nombreEvaluador: "Carlos Mendoza",
                    proyecto: {
                        titulo: "A005",
                        inicio: this.calcularPosicion("13:30pm"),
                        fin: this.calcularPosicion("16:30pm")
                    }
                },
                {
                    nombreEvaluador: "Rosa Gomez",
                    proyecto: {
                        titulo: "A005",
                        inicio: this.calcularPosicion("13:30pm"),
                        fin: this.calcularPosicion("16:30pm")
                    }
                }
            ],
            timeSlots: [
                "6:00am", "6:30am", "7:00am", "7:30am", "8:00am", "8:30am",
                "9:00am", "9:30am", "10:00am", "10:30am", "11:00am", "11:30am",
                "12:00pm", "12:30pm", "1:00pm", "1:30pm", "2:00pm", "2:30pm",
                "3:00pm", "3:30pm", "4:00pm", "4:30pm", "5:00pm", "5:30pm", "6:00pm", "6:30pm"
            ],
        };
    },
    computed: {
        today() {
            const currentDate = new Date();
            const options = { year: 'numeric', month: 'long', day: 'numeric' };
            return currentDate.toLocaleDateString(undefined, options);
        }
    },
    methods: {
        calcularPosicion(hora) {
            let [horas, minutos] = hora.split(":").map((v) => parseInt(v, 10));
            let posicion = (horas - 6) * 2;
            if (minutos >= 30) {
                posicion += 1;
            }
            console.log(minutos)
            return posicion;
        },
        isProjectTime(i, inicio, fin) {
            return i >= inicio && i <= fin;
        },
        getStyle(i, inicio, fin) {
            if (this.isProjectTime(i, inicio, fin)) {
                return {
                    backgroundColor: 'rgb(255, 182, 6)',
                    textAlign: 'center',
                    color: 'black'
                };
            }
            return {};
        }
    }
};
</script>
