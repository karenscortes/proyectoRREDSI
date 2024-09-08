<template>
    <div class="container mt-5">
        <!-- Título de la sección -->
        <div class="row mb-3 mt-2">
            <div class="col">
                <div class="section_title text-center">
                    <h1>Postulaciones</h1>
                </div>
            </div>
        </div>

        <!-- Información evaluadores -->
        <div class="container mt-5">
            <div class="row justify-content-center mb-4">
                <div class="col-3 col-sm-3">
                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                        fill="#12d336">
                        <path
                            d="M720-120H280v-520l280-280 50 50q7 7 11.5 19t4.5 23v14l-44 174h258q32 0 56 24t24 56v80q0 7-2 15t-4 15L794-168q-9 20-30 34t-44 14Zm-360-80h360l120-280v-80H480l54-220-174 174v406Zm0-406v406-406Zm-80-34v80H160v360h120v80H80v-520h200Z" />
                    </svg>
                    <span class="text-dark">Evaluador Aceptado</span>
                </div>
                <div class="col-3 col-sm-3">
                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                        fill="#f50c0c">
                        <path
                            d="M240-840h440v520L400-40l-50-50q-7-7-11.5-19t-4.5-23v-14l44-174H120q-32 0-56-24t-24-56v-80q0-7 2-15t4-15l120-282q9-20 30-34t44-14Zm360 80H240L120-480v80h360l-54 220 174-174v-406Zm0 406v-406 406Zm80 34v-80h120v-360H680v-80h200v520H680Z" />
                    </svg>
                    <span class="text-dark">Evaluador Rechazado</span>
                </div>
                <div class="col-3 col-sm-3">
                    <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px"
                        fill="#00000">
                        <path
                            d="M720-120H280v-520l280-280 50 50q7 7 11.5 19t4.5 23v14l-44 174h258q32 0 56 24t24 56v80q0 7-2 15t-4 15L794-168q-9 20-30 34t-44 14Zm-360-80h360l120-280v-80H480l54-220-174 174v406Zm0-406v406-406Zm-80-34v80H160v360h120v80H80v-520h200Z" />
                    </svg>
                    <span class="text-dark">Evaluador Pendiente</span>
                </div>
            </div>
            <div class="accordion accordion-flush" id="accordionFlushExample">
                <AcordeonPostulaciones v-for="(evaluador, index) in evaluadores" :key="index" :evaluador="evaluador"
                    :index="index" />
            </div>
        </div>
    </div>
</template>

<script>
import AcordeonPostulaciones from "./AcordeonPostulaciones.vue";

export default {
    components: {
        AcordeonPostulaciones,
    },
    data() {
        return {
            evaluadores: [
                {
                    nombreEvaluador: "Sebastian Usma",
                    institucion: "UTP",
                    areaConocimiento: "Ciencias Sociales",
                    areaConocimientoSecundaria: "Educación",
                    telefono: "123456789",
                    correo: "usma@mail.com",
                    estado: "Aceptado",
                    urlArchivo: "ruta/al/archivo.pdf",
                    etapa_virtual: true,
                    etapa_presencial: true,
                    jornada_manana: true,
                    jornada_tarde: false
                },
                {
                    nombreEvaluador: "Maribel Obando",
                    institucion: "SENA",
                    areaConocimiento: "Sistemas",
                    areaConocimientoSecundaria: "Tecnología",
                    telefono: "987654321",
                    correo: "obando@mail.com",
                    estado: "Pendiente",
                    urlArchivo: "ruta/al/archivo2.pdf",
                    etapa_virtual: true,
                    etapa_presencial: false,
                    jornada_manana: false,
                    jornada_tarde: false
                },
                {
                    nombreEvaluador: "María Pérez",
                    institucion: "Universidad Nacional",
                    areaConocimiento: "Ingeniería",
                    areaConocimientoSecundaria: "Matemáticas",
                    telefono: "987654321",
                    correo: "mperez@unacional.edu.co",
                    estado: "Pendiente",
                    urlArchivo: "documentos/cv_maria_perez.pdf",
                    etapa_virtual: false,
                    etapa_presencial: true,
                    jornada_manana: false,
                    jornada_tarde: true
                },
                {
                    nombreEvaluador: "Juan Rodríguez",
                    institucion: "Universidad de Antioquia",
                    areaConocimiento: "Medicina",
                    areaConocimientoSecundaria: "Biología",
                    telefono: "1122334455",
                    correo: "jrodriguez@udea.edu.co",
                    estado: "Aceptado",
                    urlArchivo: "documentos/juan_rodriguez.pdf",
                    etapa_virtual: false,
                    etapa_presencial: true,
                    jornada_manana: true,
                    jornada_tarde: true
                },
                {
                    nombreEvaluador: "Laura Gómez",
                    institucion: "Pontificia Universidad Javeriana",
                    areaConocimiento: "Artes",
                    areaConocimientoSecundaria: "Diseño Gráfico",
                    telefono: "5566778899",
                    correo: "laura.gomez@javeriana.edu.co",
                    estado: "Rechazado",
                    urlArchivo: "documentos/laura_gomez_cv.pdf",
                    etapa_virtual: true,
                    etapa_presencial: false,
                    jornada_manana: false,
                    jornada_tarde: false
                }



            ],
        };
    },
};
</script>
