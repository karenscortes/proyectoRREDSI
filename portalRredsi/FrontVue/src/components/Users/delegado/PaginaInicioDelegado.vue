<template>
    <div>
        <div class="become">
            <div class="container">
                <div class="row row-eq-height">

                    <div class="col-lg-6 order-2 order-lg-1">
                        <div class="become_title">
                            <h1>Bienvenido {{ user?.nombres }}</h1>
                        </div>
                        <p class="become_text">La Red Regional de Semilleros de Investigación – RREDSI ha sido clave en el desarrollo académico y científico de la región. Nuestros delegados, con su dedicación y habilidades organizativas, han asegurado el éxito de cada evento, creando espacios de crecimiento para jóvenes investigadores. Su esfuerzo ha consolidado a RREDSI como un referente en la promoción de la ciencia y la innovación en Colombia.</p>
                        <div class="become_button text-center trans_200">
                            <a href="#">Explorar</a>
                        </div>
                    </div>

                    <div class="col-lg-6 order-1 order-lg-2">
                        <div class="become_image">
                            <img src="@/assets/img/become.jpg" alt="">
                        </div>
                    </div>

                </div>
            </div>
        </div>


        <!-- Milestones -->
        <div class="milestones">
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
                                <div class="milestone_text">Presentaciones</div>
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

.become {
    width: 100%;
    padding-top: 20px;
    padding-bottom: 60px;
}

.become_title h1 {
    display: block;
    color: #1a1a1a;
    font-weight: 500;
    padding-top: 24px;
}

.become_title h1::before {
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    width: 55px;
    height: 4px;
    content: '';
    background: #ffb606;
}

.become_text
    {
        font-weight: 500;
        font-size: 14px;
        color: #a5a5a1;
        margin-top: 48px;
        margin-bottom: 0px;
    }

.become_button {
    width: 188px;
    height: 53px;
    background: #ffb606;
    margin-top: 37px;
}

.become_button a {
    display: block;
    font-size: 16px;
    font-weight: 700;
    color: #FFFFFF;
    line-height: 53px;
}

.become_button:hover {
    box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.2);
}

.become_image {
    width: 100%;
    margin-top: 85px;
}

.become_image img {
    width: 100%;
}

.btn-close {

    width: 8px;
    height: 8px;
}

/* Media query para pantallas pequeñas */
@media (max-width: 990px) {
    .become_image {
        margin-top: 1px;
    }

    .become_text {
        margin-top: 30px;
    }

    .become_title {
        margin-top: 40px;
    }
}
</style>