<template>
    <div class="become">
        <div class="container">
            <div class="row row-eq-height">
                <div class="col-lg-6 order-2 order-lg-1">
                    <div class="become_title">
                        <h1>Bienvenido al portal RREDSI</h1>
                    </div>
                    <p class="become_text">In aliquam, augue a gravida rutrum, ante nisl fermentum nulla, vitae tempor nisl ligula vel nunc. Proin quis mi malesuada, finibus tortor fermentum. Etiam eu purus nec eros varius luctus. Praesent finibus risus facilisis ultricies venenatis. Suspendisse fermentum sodales lacus, lacinia gravida elit dapibus sed. Cras in lectus elit. Maecenas tempus nunc vitae mi egestas venenatis. Aliquam rhoncus, purus in vehicula porttitor, lacus ante consequat purus, id elementum enim purus nec enim. In sed odio rhoncus, tristique ipsum id, pharetra neque.</p>
                    <div class="become_button text-center trans_200">
                        <a href="#">Explorar</a>
                    </div>
                </div>
                <div class="col-lg-6 order-1 order-lg-2">
                    <div class="become_image">
                        <img src="../plantilla/images/become.jpg" alt="img">
                    </div>
                </div>
                
            </div>
        </div>
    </div>
</template>

<script>    

</script>

<style scoped> 
    .become
    {
        width: 100%;
        padding-top: 60px;
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
</style>