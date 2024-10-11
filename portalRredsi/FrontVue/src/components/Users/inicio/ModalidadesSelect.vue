<template>
    <div class="form-group">
        <select class="form-control" id="modalidadesSelect" v-model="selectedModalidad" @change="updateModalidad">
            <option v-for="modalidad in modalidades" :key="modalidad.id_modalidad" :value="modalidad.id_modalidad">
                {{ modalidad.nombre }}
            </option>
        </select>
    </div>
</template>

<script>
import { ref, onMounted, watch } from 'vue';
import { getAllModalidades } from '@/services/modalidades_Service';  // Asegúrate de tener el servicio configurado correctamente

export default {
    props: {
        selectedModalidad: {
            type: Number,
            default: null,
        },
    },
    setup(props, { emit }) {
        const modalidades = ref([]);
        const selectedModalidad = ref(props.selectedModalidad);

        // Obtener modalidades de la API
        const fetchModalidades = async () => {
            try {
                const response = await getAllModalidades(); // Cambia esto según cómo esté configurada tu API
                modalidades.value = response.data;
            } catch (error) {
                console.error('Error al obtener las modalidades:', error);
            }
        };

        // Emitir el evento modalidad-selected cuando cambie selectedModalidad
        const updateModalidad = () => {
            emit('modalidad-selected', selectedModalidad.value);
        };

        // Obtener modalidades cuando el componente se monta
        onMounted(fetchModalidades);

        // Usar watch para observar cambios en props.selectedModalidad
        watch(
            () => props.selectedModalidad,
            (newModalidad) => {
                selectedModalidad.value = newModalidad;
            },
            { immediate: true }
        );

        return {
            modalidades,
            selectedModalidad,
            updateModalidad,
        };
    },
};
</script>

<style scoped>
/* Estilos opcionales */
</style>
