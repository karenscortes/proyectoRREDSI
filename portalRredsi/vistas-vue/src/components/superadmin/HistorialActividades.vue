<template>
    <div class="modal fade" id="historialModal" tabindex="-1" aria-labelledby="historialLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content border border-dark border-5 rounded-4 text-dark">
            <div class="modal-header bg-warning">
                <h3 class="modal-title mx-auto" id="historialLabel">HISTORIAL ACCIONES DELEGADO {{ nombre_delegado }} </h3>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body p-4">
                <div class="table-responsive">
                    <table class="table table-bordered">
                        <thead class="bg-warning">
                            <tr>
                                <th>Tipo de Acción</th>
                                <th>Módulo</th>
                                <th>Descripción</th>
                                <th>Fecha</th>
                                <th>Hora</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>{{ tipo_accion }}</td>
                                <td>{{ modulo }}</td>
                                <td>{{ descripcion }}</td>
                                <td>{{ fecha }}</td>
                                <td>{{ hora }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>

</template>

<script>
import { ref } from "vue";
export default {
    setup() {
        const nombre_delegado = ref("nombre_delegado");
        const tipo_accion = ref(tipo_accion);
        const modulo = ref(modulo);
        const descripcion = ref(descripcion);
        const fecha = ref(fecha);
        const hora = ref(hora);

        
        return { nombre_delegado, tipo_accion, modulo, descripcion, fecha, hora };
    },
};
</script>