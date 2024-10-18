<template>
 
        <div class="row justify-content-center mb-3">
            <div class="col-lg-6 col-8 text-center">
                <h4 class=" mb-5 fs-3 border-2 d-inline-block p-2 title-border-radius">Bienvenid@ al Portal RREDSI</h4>
            </div>
        </div>
        <div class="row g-5 align-items-center mb-5">
            <div class="col-lg-5 wow1 fadeIn" data-wow-delay="0.1s">
                <div class="video border">
                    <button type="button" class="btn btn-play">
                      <a href="https://www.youtube.com/watch?v=Gj68NswekVs" target="_blank"><span></span></a>
                    </button>
                </div>
            </div>
            <div class="col-lg-7 wow2 fadeIn" data-wow-delay="0.3s">
                <h1 class="text-dark mb-4 display-7">Aprende Sobre las Funcionalidades y Servicios Disponibles</h1>
                <p class="text-dark mb-4">En este video se presenta una guía completa sobre las distintas opciones disponibles en el portal RREDSI. Explorarás las tareas que puedes realizar y la ubicación de cada sección para facilitar tu experiencia de uso. Además, podrás obtener información detallada sobre...
                </p>
                <div class="row mb-4">
                    <div class="col-lg-6">
                        <h6 class="mb-3 text-dark"><i class="fas fa-check-circle me-2 icon"></i>Características</h6>
                        <h6 class="mb-3 text-dark"><i class="fas fa-check-circle me-2 icon"></i>Herramientas</h6>
                        <h6 class="mb-3 text-dark"><i class="fas fa-check-circle me-2 icon"></i>Limitaciones</h6>
                    </div>
                    <div class="col-lg-6">
                        <h6 class="mb-3 text-dark"><i class="fas fa-check-circle me-2 icon"></i>Alcance</h6>
                        <h6 class="mb-3 text-dark"><i class="fas fa-check-circle me-2 icon"></i>Requisitos</h6>
                        <h6 class="text-dark"><i class="fas fa-check-circle me-2 icon"></i>Configuraciones Predeterminadas</h6>
                    </div>
                </div>
                <a href="" class="btn px-5 py-3">Más información</a>
            </div>
        </div>
</template>
<style scoped>
.title-border-radius {
    border-radius: 10% 30%;
    color: #ffb606;
    border-bottom: 2px solid #ffb606;
  }
  
  .icon{
    color: #343a40;
    font-size: 15px
  }
  
  .border {
    border: 1px solid #dee2e6 !important;
  }
  
  .btn {
    font-weight: 600;
    transition: .5s;
    background: #ffb606;
  }
  
  .video {
    position: relative;
    height: 100%;
    min-height: 400px;
    background: linear-gradient(rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0.1)), url(../../../assets/img/learning.png);
    background-position: center center;
    background-repeat: no-repeat;
    background-size: cover;
    border-radius: 10px;
  }
  
  .video .btn-play {
    position: absolute;
    z-index: 3;
    top: 50%;
    left: 50%;
    transform: translateX(-50%) translateY(-50%);
    box-sizing: content-box;
    display: block;
    width: 32px;
    height: 44px;
    border-radius: 50%;
    border: none;
    outline: none;
    padding: 18px 20px 18px 28px;
  }
  
  .video .btn-play:before {
    content: "";
    position: absolute;
    z-index: 0;
    left: 50%;
    top: 50%;
    transform: translateX(-50%) translateY(-50%);
    display: block;
    width: 100px;
    height: 100px;
    background: #7083f9;
    border-radius: 50%;
    animation: pulse-border 1500ms ease-out infinite;
  }
  
  .video .btn-play:after {
    content: "";
    position: absolute;
    z-index: 1;
    left: 50%;
    top: 50%;
    transform: translateX(-50%) translateY(-50%);
    display: block;
    width: 100px;
    height: 100px;
    background: #ffb606;
    border-radius: 50%;
    transition: all 200ms;
  }
  
  .video .btn-play img {
    position: relative;
    z-index: 3;
    max-width: 100%;
    width: auto;
    height: auto;
  }
  
  .video .btn-play span {
    display: block;
    position: relative;
    z-index: 3;
    width: 0;
    height: 0;
    border-left: 32px solid white;
    border-top: 22px solid transparent;
    border-bottom: 22px solid transparent;
  }
  
  @keyframes pulse-border {
    0% {
        transform: translateX(-50%) translateY(-50%) translateZ(0) scale(1);
        opacity: 1;
    }
  
    100% {
        transform: translateX(-50%) translateY(-50%) translateZ(0) scale(1.5);
        opacity: 0;
    }
  }
  
  #videoModal {
    z-index: 99999;
  }
  
  #videoModal .modal-dialog {
    position: relative;
    max-width: 800px;
    margin: 60px auto 0 auto;
  }
  
  #videoModal .modal-body {
    position: relative;
    padding: 0px;
  }
  
  #videoModal .close {
    position: absolute;
    width: 30px;
    height: 30px;
    right: 0px;
    top: -30px;
    z-index: 999;
    font-size: 30px;
    font-weight: normal;
    color: #FFFFFF;
    background: #000000;
    opacity: 1;
  }
  
  .video.border {
    border-radius: 50% 20% / 10% 40%;
  }
  
  .about {
    background: linear-gradient(rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)), url(../img/background.jpg);
    background-position: center center;
    background-repeat: no-repeat;
    background-size: cover;
  }
  /*** About End ***/
</style>