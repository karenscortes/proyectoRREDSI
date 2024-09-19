<template> 
    <dic class="container">
        <div class="head ">
            
            <span class="style"></span>
        </div>
        <div class="body">

        </div>
    </dic>

</template>
<style scoped>
    .container::after, .container::before, .body::after, .body::before, .head::after, .head::before, .style::after, .style::before {
        content: '';
        box-sizing: border-box;
        margin: 0;
        padding: 0;
        display: block;
        height: 0;
        
    }
    .style {
        overflow: hidden;
        color: transparent;
        line-height: 0;
        width: 5.1rem;
        height: 1rem;
        margin-top: .2rem;
        position: absolute;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        margin-top:1.3rem;
        margin-left: .1rem;
    }
  
    .style::before {
        width: .3rem; height: .3rem;
        background: #222;
        margin-top: .5rem;
        margin-left: 1.6rem;
        border-radius: 50%;
        box-shadow:
            0 0 0 .3rem white,
            1.4rem -.2rem 0 #222,
            1.5rem 0 0 .3rem white
        ;
    }
     
  
    .head {
        width: 5.1rem;
        height: 5.1rem;
        background: #ffb606;
        border-radius: 50%;
        z-index: -1;
        box-shadow:
        0 0 0 2rem hsla(50, 97%, 49%, 0.1),
        0 0 0 4rem hsla(50, 94%, 33%, 0.05),
        0 0 0 6rem hsla(50, 97%, 61%, .025)
        ;
        position: absolute;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        margin: auto;
    }
  
    .head::after {
        background: #222;
        border-radius: 4rem 4rem .5rem .5rem;
        width: 1.1rem;
        height: .5rem;
        background: #ED6B5F;
        margin-bottom: 1.2rem;
        box-shadow: 0 -.3rem 0 .3rem #222;
        position: absolute;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        margin-top:3.5rem;
        margin-left: 2rem;
        
    }

    .container{
      
        font-family: system-ui, Helvetica, Roboto, sans-serif;
        text-align: center;
    }
  
    .container::after {
        content: '';
        line-height: 0;
        height: 0;
        transform: translatex(1rem);
        content: '4 4';
        font-size: 7rem;
        color: #ffb606;
        letter-spacing: 2rem;
        font-weight: bold;
        position: absolute;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        margin: auto;
    }
    
    .container::before {
        content: 'Página No Encontrada';
        font-family: 'Roboto', sans-serif;
        color: #222;
        font-weight: bolder;
        line-height: 0;
        height: 0;
        position: absolute;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        margin: auto;
        transform: translatey(11rem);
        font-size: 1.5rem;
    }
  
    .body {
        width: 100vw;
        height: 100vh;
        overflow-x: hidden;
    }
  
    .body::after {
        content: 'La Página a la que esta tratando de acceder no existe.';
        font-family: 'Roboto', sans-serif;
        color: #222;
        font-size: 1rem;
        line-height: 0;
        height: 0;
        transform: translatey(14rem);
        position: absolute;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        margin: auto;
    }

</style>