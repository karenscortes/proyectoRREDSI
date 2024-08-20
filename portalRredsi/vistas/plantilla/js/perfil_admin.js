// obtener la logitud en px hasta estos elementos.
let personal_info = $('#datos_personales').offset().top,
    place_info = $('#datos_institucionales').offset().top,
    studies_info = $('#datos_academicos').offset().top;

// Se redimensiona las posiciones verticalmente cada vez que la ventana cambia de tamaño.
window.addEventListener('resize', function(){
    let equipo = $('#datos_personales').offset().top,
    servicio = $('#datos_institucionales').offset().top,
    trabajo = $('#datos_academicos').offset().top;
});

$('#btn_datos_personales').on('click',function(e){
    e.preventDefault();
    $('html, body').animate({
        scrollTop: personal_info-100
    },600);
});

$('#btn_datos_institucionales').on('click',function(e){
    e.preventDefault();
    $('html, body').animate({
        scrollTop: place_info-100
    },600);
});

$('#btn_datos_academicos').on('click',function(e){
    e.preventDefault();
    $('html, body').animate({
        scrollTop: studies_info-100
    },600);
});
