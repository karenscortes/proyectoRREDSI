<template>
    <div class="col my-4">
        <div class="section_title text-center ">
            <h1>Listado de Proyectos</h1>
        </div>
    </div>
    <!-- Select -->
    <div class="container">
        <div class="row justify-content-between">
            <div class="col-7 col-sm-3 mb-3 ">
                <select class="form-select" aria-label="Default select example">
                    <option selected>Etapas</option>
                    <option value="1">Primera Etapa</option>
                    <option value="2">Segunda Etapa</option>
                </select>
            </div>
            <div class=" col-12 col-sm-7 row justify-content-end align-items-center">
                <div class="col-8 col-sm-7">
                    <input type="text" id="busqueda" class="form-control py-2 w-100"
                        style="height: 100%; padding: 0.5rem;" placeholder="Buscar">
                </div>
                <div class="col-4 col-sm-5">
                    <button class="btn w-100 font-weight-bold"
                        style="background-color: #000000; color: #ffffff">Buscar</button>
                </div>
            </div>
        </div>

        <div class="row mb-3 mt-4 justify-content-between align-items-center">
            <div class="col-12">
                <div class="d-flex justify-content-start">
                    <!-- Filtros -->
                    <a href="#" class="mx-1 px-2 border text-white bg-secondary" style="border-radius: 20px;" disabled>
                        Todos
                    </a>
                    <a href="#" class="mx-1 px-2 border text-dark" style="border-radius: 20px;">
                        Calificados
                    </a>
                    <a href="#" class="mx-1 px-2 border text-dark" style="border-radius: 20px;">
                        Pendientes
                    </a>
                </div>
            </div>
        </div>

        <!--Cards-->
        <div class="row">
            <CardProyecto v-for="(proyecto, index) in proyectos" :key="index" :cod_proyecto="proyecto.cod_proyecto"
            :titulo="proyecto.titulo" :institucion="proyecto.institucion" :estado="proyecto.estado"/>
        </div>
    </div>
    <!-- Paginador -->
    <div class="mt-2">
        <div aria-label="Page navigation example mb-5">
            <ul class="pagination justify-content-center">
                <li class="page-item  m-1">
                    <a class="page-link" href="#" tabindex="-1" style="border-radius: 20px; color: black;">Previous</a>
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
</template>

<script>
import CardProyecto from '../CardProyecto.vue';
export default{
    components: {
        CardProyecto,
    },
    data(){
        return{
            proyectos:[
                { 
                    cod_proyecto: "A001",
                    titulo: "BidDataIA",
                    institucion: "UTP",
                    estado:"Calificado"
                },
                { 
                    cod_proyecto: "A034",
                    titulo: "AguaLimpia",
                    institucion: "SENA",
                    estado:"Calificado"
                },
                { 
                    cod_proyecto: "A011",
                    titulo: "CienciaDatos",
                    institucion: "SENA",
                    estado:"Pendiente"
                },
                { 
                    cod_proyecto: "A001",
                    titulo: "BidDataIA",
                    institucion: "UTP",
                    estado:"Calificado"
                },
                { 
                    cod_proyecto: "A001",
                    titulo: "BidDataIA",
                    institucion: "UTP",
                    estado:"Calificado"
                },
                { 
                    cod_proyecto: "A001",
                    titulo: "BidDataIA",
                    institucion: "UTP",
                    estado:"Calificado"
                },
        
            ]
        }
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

/* Estilos para el paginador */
.pagination .page-item .page-link {
    font-size: 18px;
    padding: 10px 20px;
    border-radius: 50px;
}

.pagination .page-item .page-link:hover {
    background-color: rgb(255, 182, 6);
    color: #ffffff;
}

</style>