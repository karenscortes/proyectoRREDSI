<template>
    <div>
        <!-- Tabla de horarios -->
        <div class="container mt-4">
            <div>
                <!-- <h3 class="text-center m-0">{{ horario.fecha }}</h3> -->
            </div>
            <table class="table table-hover border table-responsive">
                <thead>
                    <tr>
                        <th class="text-center">Evaluadores</th>
                        <th v-for="time in timeSlots" :key="time" class="text-center time-slot">{{ time }}</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(detalle, index) in detalleSala" :key="index">
                        <td class="text-center">{{ detalle.nombre_evaluador }}</td>
                        <td v-for="(slot, i) in 24" :key="i"
                            :style="getStyle(i, detalle.hora_inicio, detalle.hora_fin)">
                            <span v-if="isProjectTime(i, detalle.hora_inicio, detalle.hora_fin)">
                                {{ detalle.id_proyecto }}
                            </span>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import { obtenerDetalleSala } from "@/services/salasDelegadoService";

export default{
    props:{
        sala: Object
    },
    data() {
        return {
            timeSlots: [
                "6:00am", "6:30am", "7:00am", "7:30am", "8:00am", "8:30am", "9:00am", "9:30am",
                "10:00am", "10:30am", "11:00am", "11:30am", "12:00pm", "12:30pm", "1:00pm", "1:30pm",
                "2:00pm", "2:30pm", "3:00pm", "3:30pm", "4:00pm", "4:30pm", "5:00pm", "5:30pm", "6:00pm", "6:30pm"
            ],
            detalleSala: [],
            evaluadores: [],
        }
        
    },
    methods: {
        calcularPosicion(hora) {
            let [horas, minutos] = hora.split(":").map(Number);
            let posicion = (horas - 6) * 2;
            if (minutos >= 30) {
                posicion += 1;
            }
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
        },
        async obtenerDatosSala() {
            try {
                const datosSala = await obtenerDetalleSala(this.sala.id_sala);
                this.detalleSala = datosSala.data.detalle_sala;

                // Convierte las horas a minutos en cada fila de la tabla
                for(let i = 0; i < this.detalleSala.length; i++) {
                    // castea el formato a horas y minutos validos 
                    this.detalleSala[i].hora_inicio = this.obtenerHoraMinutos(this.detalleSala[i].hora_inicio);
                    this.detalleSala[i].hora_fin = this.obtenerHoraMinutos(this.detalleSala[i].hora_fin);
                    
                    // obtiene la posicion en la tabla para que se pueda imprimir
                    this.detalleSala[i].hora_inicio = this.calcularPosicion(this.detalleSala[i].hora_inicio);
                    this.detalleSala[i].hora_fin = this.calcularPosicion(this.detalleSala[i].hora_fin);
                }
            } catch (error) {
                alert("Aún no se han asignado proyectos a esta sala")
            }
        },
        
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

            return  horas+":"+minutos
        }
    },
    mounted() {
        console.log(this.sala)
        this.obtenerDatosSala()
    }
}
</script>