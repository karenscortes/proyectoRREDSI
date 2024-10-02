<template>
    <div class="form-group">
        <label for="areasConocimientoSelect">Seleccione un Área de Conocimiento</label>
        <select class="form-control" id="areasConocimientoSelect" v-model="selectedAreaConocimiento" @change="updateAreaConocimiento">
            <option v-for="area in areasConocimiento" :key="area.id_area_conocimiento" :value="area.id_area_conocimiento">
                {{ area.nombre }}
            </option>
        </select>
    </div>
</template>

<script>
import { ref, onMounted, watch } from 'vue';
import { getAllAreasConocimiento } from '@/services/areasConocimientoService';  // Ruta del servicio

export default {
    props: {
        selectedAreaConocimiento: {
            type: Number,
            default: null,
        },
    },
    setup(props, { emit }) {
        const areasConocimiento = ref([]);
        const selectedAreaConocimiento = ref(props.selectedAreaConocimiento);

        // Obtener áreas de conocimiento de la API
        const fetchAreasConocimiento = async () => {
            try {
                const response = await getAllAreasConocimiento();
                areasConocimiento.value = response.data;
            } catch (error) {
                console.error('Error al obtener las áreas de conocimiento:', error);
            }
        };

        // Emitir el evento area-conocimiento-selected cuando cambie selectedAreaConocimiento
        const updateAreaConocimiento = () => {
            emit('area-conocimiento-selected', selectedAreaConocimiento.value);
        };

        // Obtener áreas de conocimiento cuando el componente se monta
        onMounted(fetchAreasConocimiento);

        // Usar watch para observar cambios en props.selectedAreaConocimiento
        watch(
            () => props.selectedAreaConocimiento,
            (newAreaConocimiento) => {
                selectedAreaConocimiento.value = newAreaConocimiento;
            },
            { immediate: true }
        );

        return {
            areasConocimiento,
            selectedAreaConocimiento,
            updateAreaConocimiento,
        };
    },
};
</script>

<style scoped>
/* Estilos opcionales */
</style>
