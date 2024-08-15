// formularios
let datos_personales = document.getElementById('datos_personales');
let datos_institucionales = document.getElementById('datos_institucionales');
let datos_academicos = document.getElementById('datos_academicos');

// Botones de las opciones para llenar
let btn_datos_personales = document.getElementById('btn_datos_personales');
let btn_datos_institucionales = document.getElementById('btn_datos_institucionales');
let btn_datos_academicos = document.getElementById('btn_datos_academicos');

// Botones generales
let btn_siguiente_datos_personales = document.getElementById('btn_siguiente_datos_personales');
let btn_siguiente_datos_institucionales = document.getElementById('btn_siguiente_datos_institucionales');
let btn_regresar_datos_institucionales = document.getElementById('btn_regresar_datos_institucionales'); 
let btn_regresar_datos_academicos = document.getElementById('btn_regresar_datos_academicos');

// Eventos de los botones
btn_datos_institucionales.addEventListener('click', ()=>{
    activar_datos_institucionales();
});

btn_datos_academicos.addEventListener('click', ()=>{
    activar_datos_academicos();
});

btn_datos_personales.addEventListener('click', ()=>{
    activar_datos_personales();
});

btn_siguiente_datos_personales.addEventListener('click', ()=>{
    activar_datos_institucionales();
});

btn_siguiente_datos_institucionales.addEventListener('click',()=>{
    activar_datos_academicos();
});

btn_regresar_datos_institucionales.addEventListener('click', ()=>{
    activar_datos_personales();
});

btn_regresar_datos_academicos.addEventListener('click',()=>{
    activar_datos_institucionales();
});


function activar_datos_institucionales(){
    datos_personales.style.display = 'none';
    datos_academicos.style.display = 'none';
    datos_institucionales.style.display = 'block';
    btn_datos_institucionales.setAttribute('class', 'btn bg-dark text-white');
    btn_datos_academicos.setAttribute('class', 'btn text-dark');
    btn_datos_personales.setAttribute('class', 'btn text-dark');
}
function activar_datos_personales(){
    datos_personales.style.display = 'block';
    datos_academicos.style.display = 'none';
    datos_institucionales.style.display = 'none';
    btn_datos_institucionales.setAttribute('class', 'btn text-dark');
    btn_datos_academicos.setAttribute('class', 'btn text-dark');
    btn_datos_personales.setAttribute('class', 'btn bg-dark text-white');
}

function activar_datos_academicos(){
    datos_personales.style.display = 'none';
    datos_academicos.style.display = 'block';
    datos_institucionales.style.display = 'none';
    btn_datos_institucionales.setAttribute('class', 'btn text-dark');
    btn_datos_academicos.setAttribute('class', 'btn bg-dark text-white');
    btn_datos_personales.setAttribute('class', 'btn text-dark');
}