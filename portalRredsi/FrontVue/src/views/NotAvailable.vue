<template>

    <div class="contenedor">
        <div class="top ">
            
            <span class="style"></span>
        </div>
        <div class="bottom">
        
        </div>
    </div>

</template>

<style scoped>
    .contenedor::after, .contenedor::before, .bottom::after, .bottom::before, .top::after, .top::before, .style::after, .style::before {
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
     
  
    .top {
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
  
    .top::after {
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

    .contenedor{
      
        font-family: system-ui, Helvetica, Roboto, sans-serif;
        text-align: center;
    }
  
    .contenedor::after {
        content: '';
        line-height: 0;
        height: 0;
        transform: translatex(1rem);
        content: '5 3';
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
    
    .contenedor::before {
        content: 'Servicio No Disponible';
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
  
    .bottom {
        min-height: 600px;
        overflow-x: hidden;
    }
  
    .bottom::after {
        content: 'Ups... Desafortunadamente, parece que algo salió mal. Intenta de nuevo más tarde.';
        font-family: 'Roboto', 'sans-serif';
        color: #222;
        font-size: 1rem;
        position: absolute;
        top: 32rem; 
        transform: translatex(16rem); 
        text-align: center;
    }

    @media screen and (min-width:992px) and (max-width:1199px){
        .bottom::after {
            transform: translatex(10rem); 
        }
    }

    @media screen and (min-width:768px) and (max-width:991px){
        .bottom::after {
            transform: translatex(5rem); 
        }
    }

    @media screen and (max-width:767px){
        .bottom::after {
            transform: translatex(0); 
            margin-right: 6rem;
            margin-left: 4rem;
        }
    }
</style>