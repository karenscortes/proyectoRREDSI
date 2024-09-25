<template>
    <form action="#" class="row justify-content-center ">
        <div class="col-11 mb-3 table-responsive">
            <table class="table display text-dark border border-dark w-100">
                <thead class="text-center">
                    <tr class="titulo_rubrica">
                        <td class="col-4" style="border-top: 1px solid #000;">Titulo:</td>
                        <td colspan="4" style="border-top: 1px solid #000;">
                            <input type="text" class="form-control fs-6 form-control-sm" readonly
                                v-bind:value="tituloProyecto">
                        </td>
                    </tr>
                    <tr class="titulo_rubrica">
                        <td class="col-4">Ponente(s):</td>
                        <td colspan="4">
                            <input type="text" class="form-control fs-6 form-control-sm " readonly
                                v-bind:value="ponentesProyecto">
                        </td>
                    </tr>
                    <tr class="titulo_rubrica">
                        <td class="col-4">Universidad:</td>
                        <td colspan="4">
                            <input type="text" class="form-control fs-6 form-control-sm" readonly
                                v-bind:value="universidadProyecto">
                        </td>
                    </tr>
                    <tr class="titulo_rubrica">
                        <td scope="col-4">Componentes</td>
                        <td scope="col-2">Max Valor</td>
                        <td scope="col-2">Calificación</td>
                        <td scope="col-4">Observaciones</td>
                    </tr>
                </thead>
                    <!-- Component body -->
                    <BodyRubrica :rubricaItems="rubricaItems"></BodyRubrica>
                <tfoot>
                    <tr class="titulo_rubrica text-center">
                        <th class="border border-dark" scope="row">Puntaje total:</th>
                        <td class="border border-dark">
                            <input type="number" class="form-control fs-6 form-control-sm  w-100" readonly 
                                v-bind:value="puntajeTotal">
                        </td>
                    </tr>
                    <tr class="titulo_rubrica text-center">
                        <th class="border border-dark" scope="row">Nombre del Evaluador:</th>
                        <td class="border border-dark">
                            <input type="text" class="form-control fs-6 form-control-sm  w-100" readonly
                                v-bind:value="nombreEvaluador">
                        </td>
                        <th class="border border-dark" scope="row">Cédula:</th>
                        <td class="border border-dark">
                            <input type="text" class="form-control fs-6 form-control-sm " readonly
                                v-bind:value="cedulaEvaluador">
                        </td>
                    </tr>
                    <tr class="titulo_rubrica text-center">
                        <th scope="row" class="border border-dark">Universidad:</th>
                        <td class="border border-dark">
                            <input type="text" class="form-control fs-6 form-control-sm " readonly
                                v-bind:value="universidadEvaluador">
                        </td>
                    </tr>
                    <tr class="titulo_rubrica text-center">
                        <th scope="row" class="border border-dark">Email:</th>
                        <td class="border border-dark">
                            <input type="text" class="form-control fs-6 form-control-sm" readonly
                                v-bind:value="emailEvaluador">
                        </td>
                        <th scope="row" class="border border-dark">Celular:</th>
                        <td class="border border-dark">
                            <input type="text" class="form-control fs-6 form-control-sm" readonly
                                v-bind:value="celularEvaluador">
                        </td>
                    </tr>
                </tfoot>
            </table>
        </div>
    </form>
</template>

<script>
import BodyRubrica from './BodyRubrica.vue';

export default {
    name: 'RubricaCom',
    components: {
        BodyRubrica
    },
    props: {
        tituloProyecto: String,
        ponentesProyecto: String,
        universidadProyecto: String,
        puntajeTotal:Number,
        nombreEvaluador: String,
        cedulaEvaluador: Number,
        universidadEvaluador: String,
        emailEvaluador: String,
        celularEvaluador: Number
    },
    data() {
        return {
            rubricaItems: [
                { componente: 'Originalidad del Proyecto', maxValor: 30, calificacion: 10, observaciones: '' },
                { componente: 'Calidad de la Presentación', maxValor: 25, calificacion: 20, observaciones: '' },
                { componente: 'Relevancia del Contenido', maxValor: 20, calificacion: 10, observaciones: '' },
                { componente: 'Capacidad de Respuesta', maxValor: 15, calificacion: 5, observaciones: '' },
                { componente: 'Impacto Potencial', maxValor: 10, calificacion: 5, observaciones: '' }
            ]
        };
    }
}
</script>

<style scoped>
.tr_rubrica {
    border-bottom: 1px solid black;
}

.td_rubrica {
    border-right: 1px solid black;
}

.titulo_rubrica {
    font-size: 18px;
    font-weight: bold;
}

.form-control {
    height: 35px;
    border: 1px solid black;
}
</style>