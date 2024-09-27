<template>
    <div class="become">
        <div class="container">
            <div class="row row-eq-height">
                <div class="col-lg-6 order-2 order-lg-1">
                    <div class="become_title">
                        <h1>Bienvenido al portal RREDSI</h1>
                    </div>
                    <p class="become_text">RREDSI es una red reconocida por su impacto en el desarrollo de proyectos de innovación y tecnología. A lo largo de los años, los evaluadores han desempeñado un rol clave en garantizar la calidad y relevancia de los proyectos presentados. Su capacidad para analizar y proporcionar retroalimentación precisa ha contribuido significativamente al éxito de cada convocatoria. Los logros obtenidos demuestran el compromiso y la excelencia en cada evaluación realizada. RREDSI sigue avanzando como un motor de progreso para la ciencia y la innovación en Colombia.</p>
                    
                </div>
                <div class="col-lg-6 order-1 order-lg-2">
                    <div class="become_image">
                        <img src="../assets/img/become.jpg" alt="img">
                    </div>
                </div>
                
            </div>
        </div>
    </div>
</template>

<style scoped> 
    .become
    {
        width: 100%;
        padding-bottom: 60px;
    }
    .become_title h1
    {
        display: block;
        color: #1a1a1a;
        font-weight: 500;
        padding-top: 24px;
    }
    .become_title h1::before
    {
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
        font-size: 16px;
        color: #a5a5a1;
        margin-top: 48px;
        margin-bottom: 0px;
    }
    .become_button
    {
        width: 188px;
        height: 53px;
        background: #ffb606;
        margin-top: 37px;
    }
    .become_button a
    {
        display: block;
        font-size: 16px;
        font-weight: 700;
        color: #FFFFFF;
        line-height: 53px;
    }
    .become_button:hover
    {
        box-shadow: 0px 10px 20px rgba(0,0,0,0.2);
    }
    .become_image
    {
        width: 100%;
        margin-top: 85px;
    }
    .become_image img
    {
        width: 100%;
    }

    .btn-close{

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
