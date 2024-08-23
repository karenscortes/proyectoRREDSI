// // formularios
// let datos_personales = document.getElementById('datos_personales');
// let datos_institucionales = document.getElementById('datos_institucionales');
// let datos_academicos = document.getElementById('datos_academicos');

// // Botones de las opciones para llenar
// let btn_datos_personales = document.getElementById('btn_datos_personales');
// let btn_datos_institucionales = document.getElementById('btn_datos_institucionales');
// let btn_datos_academicos = document.getElementById('btn_datos_academicos');

// // Botones generales
// let btn_siguiente_datos_personales = document.getElementById('btn_siguiente_datos_personales');
// let btn_siguiente_datos_institucionales = document.getElementById('btn_siguiente_datos_institucionales');
// let btn_regresar_datos_institucionales = document.getElementById('btn_regresar_datos_institucionales'); 
// let btn_regresar_datos_academicos = document.getElementById('btn_regresar_datos_academicos');

// // Eventos de los botones
// btn_datos_institucionales.addEventListener('click', ()=>{
//     activar_datos_institucionales();
// });

// btn_datos_academicos.addEventListener('click', ()=>{
//     activar_datos_academicos();
// });

// btn_datos_personales.addEventListener('click', ()=>{
//     activar_datos_personales();
// });

// btn_siguiente_datos_personales.addEventListener('click', ()=>{
//     activar_datos_institucionales();
// });

// btn_siguiente_datos_institucionales.addEventListener('click',()=>{
//     activar_datos_academicos();
// });

// btn_regresar_datos_institucionales.addEventListener('click', ()=>{
//     activar_datos_personales();
// });

// btn_regresar_datos_academicos.addEventListener('click',()=>{
//     activar_datos_institucionales();
// });


// function activar_datos_institucionales(){
//     datos_personales.style.display = 'none';
//     datos_academicos.style.display = 'none';
//     datos_institucionales.style.display = 'block';
//     btn_datos_institucionales.setAttribute('class', 'btn bg-dark text-white');
//     btn_datos_academicos.setAttribute('class', 'btn text-dark');
//     btn_datos_personales.setAttribute('class', 'btn text-dark');
// }
// function activar_datos_personales(){
//     datos_personales.style.display = 'block';
//     datos_academicos.style.display = 'none';
//     datos_institucionales.style.display = 'none';
//     btn_datos_institucionales.setAttribute('class', 'btn text-dark');
//     btn_datos_academicos.setAttribute('class', 'btn text-dark');
//     btn_datos_personales.setAttribute('class', 'btn bg-dark text-white');
// }

// function activar_datos_academicos(){
//     datos_personales.style.display = 'none';
//     datos_academicos.style.display = 'block';
//     datos_institucionales.style.display = 'none';
//     btn_datos_institucionales.setAttribute('class', 'btn text-dark');
//     btn_datos_academicos.setAttribute('class', 'btn bg-dark text-white');
//     btn_datos_personales.setAttribute('class', 'btn text-dark');
// }


let formulario = document.getElementById('formulario');
let contenido_tabla = document.getElementById('scheduleBody');
let fecha_tabla = document.getElementById('fecha_tabla');

formulario.addEventListener('submit', (e) => {
    e.preventDefault();
    let nombre_proyecto = document.getElementById('id_proyecto').value;
    let nombre_evaluador1 = document.getElementById('id_evaluador_1').value;
    let nombre_evaluador2 = document.getElementById('id_evaluador_2').value;
    let hora_inicio = document.getElementById('horario_inicio').value;
    let hora_fin = document.getElementById('horario_fin').value;
    let fecha = document.getElementById('fecha').value;
    fecha_tabla.textContent = fecha;

    console.log(nombre_proyecto);
    const texto = document.createElement('strong');
    texto.textContent = nombre_proyecto;

    let proyecto = document.createElement('td');
    proyecto.appendChild(texto);

    let evaluador1 = document.createElement('td');
    evaluador1.textContent = nombre_evaluador1;

    let evaluador2 = document.createElement('td');
    evaluador2.textContent = nombre_evaluador2;

    console.log(hora_inicio);
    insertar_proyecto(evaluador1, evaluador2, proyecto, hora_inicio, hora_fin);
});

function insertar_proyecto(evaluador_td_1, evaluador_td_2, proyectoTd, hora_inicio, hora_fin) {
    
    let inicio = calcularPosicion(hora_inicio);
    let fin = calcularPosicion(hora_fin);
    let colspan = (fin - inicio)+1;


    proyectoTd.setAttribute("colspan", colspan);
    proyectoTd.style.backgroundColor = "rgb(255, 182, 6)";
    // proyectoTd.classList.add("text-center", "movible");
    
    // Se tiene que clonar porque no deja agregar dos elementos iguales 
    proyecto_evaluador_2 = proyectoTd.cloneNode(true);

    console.log(proyecto_evaluador_2);

    let fila_evaluador_1 = document.createElement('tr');
    fila_evaluador_1.appendChild(evaluador_td_1);

    let fila_evaluador_2 = document.createElement('tr');
    fila_evaluador_2.appendChild(evaluador_td_2);

    // Insertar celdas vacías antes del horario de inicio
    for (let i = 0; i < inicio; i++) {
        let celdaVacia1 = document.createElement('td');
        let celdaVacia2 = document.createElement('td');

        fila_evaluador_1.appendChild(celdaVacia1);
        fila_evaluador_2.appendChild(celdaVacia2);
    }

    fila_evaluador_1.appendChild(proyectoTd);
    fila_evaluador_2.appendChild(proyecto_evaluador_2);

    // Insertar celdas vacías después del proyecto, si es necesario
    let totalColumnas = 24;
    let celdasRestantes = totalColumnas - (inicio + colspan);
    for (let i = 0; i < celdasRestantes; i++) {
        let celdaVacia1 = document.createElement('td');
        let celdaVacia2 = document.createElement('td');

        fila_evaluador_1.appendChild(celdaVacia1);
        fila_evaluador_2.appendChild(celdaVacia2);
    }

    contenido_tabla.appendChild(fila_evaluador_1);
    contenido_tabla.appendChild(fila_evaluador_2);
}

function calcularPosicion(hora) {
    let [horas, minutos] = hora.split(':').map(Number);
    let posicion = (horas - 6) * 2; // Resta 6 porque la tabla empieza desde las 6:00am
    if (minutos >= 30) {
        posicion += 1;
    }
    return posicion;
}

