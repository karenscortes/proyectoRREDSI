<template>  
    <form action="#" class="row justify-content-center">
        <div class="col-lg-8 col-md-11 col-sm-12 mb-3 table-responsive">
            <table class="table display text-dark border border-dark">
                <thead class="text-center">
                    <tr class="titulo_rubrica">
                        <td class="col-4" style="border-top: 1px solid #000;">Titulo:</td>
                        <td colspan="4" style="border-top: 1px solid #000;">
                            <input type="text" class="form-control fs-6 form-control-sm rounded-5" readonly v-bind:value="tituloProyecto">
                        </td>
                    </tr>
                    <tr class="titulo_rubrica">
                        <td class="col-4">Ponente(s):</td>
                        <td colspan="4">
                            <input type="text" class="form-control fs-6 form-control-sm rounded-5" readonly v-bind:value="ponentesProyecto">
                        </td>
                    </tr>
                    <tr class="titulo_rubrica">
                        <td class="col-4">Universidad:</td>
                        <td colspan="4">
                            <input type="text" class="form-control fs-6 form-control-sm rounded-5" readonly v-bind:value="universidadProyecto">
                        </td>
                    </tr>
                    <tr class="titulo_rubrica">
                        <td scope="col-4">Componentes</td>
                        <td scope="col-2">Max Valor</td>
                        <td scope="col-2">Calificación</td>
                        <td scope="col-4">Observaciones</td>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(componente, index) in componentes" :key="index">
                        <td class="border border-dark">
                            <span class="text-dark font-weight-bold">Titulo:</span> {{ componente.titulo }}
                        </td>
                        <td class="text-center border border-dark">{{ componente.valorMaximo }}</td>
                        <td class="border border-dark">
                            <input type="number" v-model.number="componente.calificacion" class="w-100">
                        </td>
                        <td class="border border-dark">
                            <textarea v-model="componente.observaciones" class="w-100" rows="1"></textarea>
                        </td>
                    </tr>
                </tbody>
                <tfoot>
                    <tr class="titulo_rubrica text-center">
                        <th class="border border-dark" scope="row">Puntaje total:</th>
                        <td class="border border-dark">
                            <input type="number" class="form-control fs-6 form-control-sm rounded-5 w-100" readonly>
                        </td>
                    </tr>
                    <tr class="titulo_rubrica text-center">
                        <th class="border border-dark" scope="row">Nombre del Evaluador:</th>
                        <td class="border border-dark">
                            <input type="text" class="form-control fs-6 form-control-sm rounded-5 w-100" readonly v-bind:value="nombreEvaluador">
                        </td>
                        <th class="border border-dark" scope="row">Cédula:</th>
                        <td class="border border-dark">
                            <input type="text" class="form-control fs-6 form-control-sm rounded-5" readonly v-bind:value="cedulaEvaluador">
                        </td>
                    </tr>
                    <tr class="titulo_rubrica text-center">
                        <th scope="row" class="border border-dark">Universidad:</th>
                        <td class="border border-dark">
                            <input type="text" class="form-control fs-6 form-control-sm rounded-5" readonly v-bind:value="universidadEvaluador">
                        </td>
                    </tr>
                    <tr class="titulo_rubrica text-center">
                        <th scope="row" class="border border-dark">Email:</th>
                        <td class="border border-dark">
                            <input type="text" class="form-control fs-6 form-control-sm rounded-5" readonly v-bind:value="emailEvaluador">
                        </td>
                        <th scope="row" class="border border-dark">Celular:</th>
                        <td class="border border-dark">
                            <input type="text" class="form-control fs-6 form-control-sm rounded-5" readonly v-bind:value="celularEvaluador">
                        </td>
                    </tr>
                </tfoot>
            </table>
        </div>
        <div class="col-8 text-center py-5">
            <button class="btn btn-warning w-25 font-weight-bold text-dark"> Calificar </button>
        </div>
    </form>
</template>

<script>    
export default {
    props: {
        tituloProyecto: String,
        ponentesProyecto: String,
        universidadProyecto: String,
        nombreEvaluador: String,
        cedulaEvaluador: Number,
        universidadEvaluador: String,
        emailEvaluador: String,
        celularEvaluador: Number
    },
}
</script>

<style scoped>

.tr_rubrica{
	border-bottom: 1px solid black;
}

.td_rubrica{
	border-right: 1px solid black;
}

.titulo_rubrica{
	font-size: 18px; font-weight: bold;
}

.form-control{
	height: 35px;
	border: 1px solid black;
}

</style>