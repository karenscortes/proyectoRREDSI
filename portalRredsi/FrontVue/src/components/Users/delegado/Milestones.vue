<template>
    <!-- Milestones -->
    <div class="row milestones">
        <div class="milestones_background">
        </div>

            <div class="container">
                <div class="row">

                    <!-- Milestone -->
                    <div class="col-lg-3 milestone_col">
                        <div class="milestone text-center">
                            <div class="milestone_icon"><img src="@/assets/img/milestone_1.svg"
                                    alt="https://www.flaticon.com/authors/zlatko-najdenovski"></div>
                            <div class="milestone_counter" data-end-value="750">{{ postulaciones }}</div>
                            <div class="milestone_text">Postulaciones</div>
                        </div>
                    </div>

                    <!-- Milestone -->
                    <div class="col-lg-3 milestone_col">
                        <div class="milestone text-center">
                            <div class="milestone_icon"><img src="@/assets/img/milestone_2.svg"
                                    alt="https://www.flaticon.com/authors/zlatko-najdenovski"></div>
                            <div class="milestone_counter" data-end-value="120">0</div>
                            <div class="milestone_text">Proyectos inscritos</div>
                        </div>
                    </div>

                    <!-- Milestone -->
                    <div class="col-lg-3 milestone_col">
                        <div class="milestone text-center">
                            <div class="milestone_icon"><img src="@/assets/img/milestone_3.svg"
                                    alt="https://www.flaticon.com/authors/zlatko-najdenovski"></div>
                            <div class="milestone_counter" data-end-value="39">{{ proyectosAsignados }}</div>
                            <div class="milestone_text">Proyectos asignados</div>
                        </div>
                    </div>

                    <!-- Milestone -->
                    <div class="col-lg-3 milestone_col">
                        <div class="milestone text-center">
                            <div class="milestone_icon"><img src="@/assets/img/milestone_4.svg"
                                    alt="https://www.flaticon.com/authors/zlatko-najdenovski"></div>
                            <div class="milestone_counter" data-end-value="3500" data-sign-before="+">0</div>
                            <div class="milestone_text">Proyectos evaluados</div>
                        </div>
                    </div>

                </div>
            </div>
    </div>
</template>
<script>
import { ref, onMounted } from 'vue';
import { useAuthStore } from '@/store';
import { obtenerCantidadPostulaciones, obtenerCantidadProyectosAsignados } from '@/services/delegadoService'

export default {
    setup() {
        const authStore = useAuthStore();
        const user = authStore.user;

        const postulaciones = ref(0);
        const proyectosAsignados = ref(0);

        // Función para obtener las postulaciones y proyectos asignados en paralelo
        const obtenerDatos = async () => {
            try {
                const [postulacionesResp, proyectosResp] = await Promise.all([
                    obtenerCantidadPostulaciones(),
                    obtenerCantidadProyectosAsignados()
                ]);

                postulaciones.value = postulacionesResp.data;
                proyectosAsignados.value = proyectosResp.data;
            } catch (error) {
                console.error('Error al obtener datos:', error);
            }
        };

        // Cargar los datos al montar el componente
        onMounted(() => {
            obtenerDatos();
        });

        return {
            user,
            postulaciones,
            proyectosAsignados
        };
    }
};
</script>
<style scoped>
/*********************************
10. Milestones
*********************************/

.milestones {
    width: 100%;
    padding-top: 30px;
    padding-bottom: 30px;
    margin-top: 20px;
    align-items: center;
}

.milestones_background {
    background-image: url('../../../assets/img/milestones_background.jpg');
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-repeat: no-repeat;
    background-size: cover;
    background-position: center center;
	background-attachment: fixed;

}

.milestone {
    width: 100%;
}

.milestone_icon {
    display: inline-block;
    width: 70px;
    height: 70px;
}

.milestone_icon img {
    width: 100%;
}

.milestone_counter {
    font-size: 36px;
    font-weight: 500;
    color: #ffb606;
    line-height: 1;
    margin-top: 41px;
}

.milestone_text {
    font-size: 22px;
    font-weight: 500;
    color: #FFFFFF;
    margin-top: 3px;
}
</style>