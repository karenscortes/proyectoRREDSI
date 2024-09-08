<template>
    <div class="container pt-5">
        <div class="row mb-4 mt-2">
            <div class="col">
                <div class="section_title text-center">
                    <h1>Asignar proyectos</h1>
                </div>
            </div>
        </div>
        <div class="accordion accordion-flush border-bottom" id="accordionFlushExample">

            <AcordeonProyecto v-for="(proyecto, index) in proyectos" 
                :key="index" 
                :proyecto="proyecto"
                :index="index" 
            />

        </div>
        <!-- Paginador -->
        <div class="mt-5">
            <div aria-label="Page navigation example mb-5">
                <ul class="pagination justify-content-center">
                    <li class="page-item disabled m-1">
                        <a class="page-link" href="#" tabindex="-1"
                            style="border-radius: 20px; color: black;">Previous</a>
                    </li>
                    <li class="page-item rounded m-1">
                        <a class="page-link rounded-circle" href="#" style="color: black;">1</a>
                    </li>
                    <li class="page-item m-1">
                        <a class="page-link rounded-circle" href="#" style="color: black;">2</a>
                    </li>
                    <li class="page-item m-1">
                        <a class="page-link rounded-circle" href="#" style="color: black;">3</a>
                    </li>
                    <li class="page-item m-1">
                        <a class="page-link" href="#" style="border-radius: 20px; color: black;">Next</a>
                    </li>
                </ul>
            </div>
        </div>

    </div>
</template>

<script>
import AcordeonProyecto from './AcordeonProyecto.vue';

export default {
    data() {
        return {
            proyectos: [
                {
                    titulo: "BigDataIA",
                    institucion: "UTP",
                    modalidad: "Ciencias Sociales",
                    autores: [{ nombre: "Francisco Sanchez" }, { nombre: "Sara Perez" }, { nombre: "Nicolas SinApellido" }, { nombre: "Santiago Alarcón" }],
                    areaConocimiento: "Sistemas",
                    posiblesEvaluadores: [{ nombreEvaluador: "Santa teresita" }, { nombreEvaluador: "Nicolas Uribe" }]
                },
                {
                    titulo: "Machine Learning en Marketing",
                    institucion: "Universidad Nacional",
                    modalidad: "Mercadeo",
                    autores: [{ nombre: "Ana María López" }, { nombre: "Carlos Rodríguez" }],
                    areaConocimiento: "Inteligencia Artificial",
                    posiblesEvaluadores: [{ nombreEvaluador: "Marta Gómez" }, { nombreEvaluador: "Juan Ríos" }]
                },
                {
                    titulo: "Blockchain en la Salud",
                    institucion: "Pontificia Universidad Javeriana",
                    modalidad: "Salud",
                    autores: [{ nombre: "Laura Fernández" }, { nombre: "Pedro García" }],
                    areaConocimiento: "Tecnología",
                    posiblesEvaluadores: [{ nombreEvaluador: "Isabel Morales" }, { nombreEvaluador: "Fernando Álvarez" }]
                },
                {
                    titulo: "Análisis de Datos en la Educación",
                    institucion: "Universidad de Antioquia",
                    modalidad: "Educación",
                    autores: [{ nombre: "Manuel Castro" }, { nombre: "Lucía Martínez" }],
                    areaConocimiento: "Estadística",
                    posiblesEvaluadores: [{ nombreEvaluador: "Jorge Herrera" }, { nombreEvaluador: "Elena Ramírez" }]
                },
                {
                    titulo: "Realidad Aumentada en la Arquitectura",
                    institucion: "Universidad de los Andes",
                    modalidad: "Arquitectura",
                    autores: [{ nombre: "Felipe Ríos" }, { nombre: "Camila Torres" }],
                    areaConocimiento: "Diseño",
                    posiblesEvaluadores: [{ nombreEvaluador: "Andrés Salazar" }, { nombreEvaluador: "Verónica Peña" }]
                },
                {
                    titulo: "Ciberseguridad en las Finanzas",
                    institucion: "Universidad del Rosario",
                    modalidad: "Finanzas",
                    autores: [{ nombre: "Santiago Muñoz" }, { nombre: "Valeria Díaz" }],
                    areaConocimiento: "Seguridad Informática",
                    posiblesEvaluadores: [{ nombreEvaluador: "Ricardo Méndez" }, { nombreEvaluador: "Patricia López" }]
                }


            ]
        }
    },
    components: {
        AcordeonProyecto
    }
}
</script>
<style>
.section_title h1 {
	display: block;
	color: #1a1a1a;
	font-weight: 500;
	padding-top: 24px;
}

.section_title h1::before {
	display: block;
	position: absolute;
	top: 0;
	left: 50%;
	-webkit-transform: translateX(-50%);
	-moz-transform: translateX(-50%);
	-ms-transform: translateX(-50%);
	-o-transform: translateX(-50%);
	transform: translateX(-50%);
	width: 55px;
	height: 4px;
	content: '';
	background: #ffb606;
}
</style>