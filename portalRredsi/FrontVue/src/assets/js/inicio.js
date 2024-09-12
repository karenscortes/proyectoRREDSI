document.getElementById('btn_ponente2').addEventListener('click', function () {
    var ponente2 = document.getElementById('ponente2');
    if (ponente2.style.display === 'none') {
        ponente2.style.display = 'block';
        this.textContent = 'Ocultar Ponente Opcional';
    } else {
        ponente2.style.display = 'none';
        this.textContent = 'Agregar Ponente Opcional';
    }
});

function openModal() {
    document.getElementById('authorModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('authorModal').style.display = 'none';
}

function addAuthor() {
    var authorName = document.getElementById('nombreAutor').value;
    var authorsList = document.getElementById('listaAutores');
    var autoresInput = document.getElementById('autores_proyecto');

    if (authorName.trim() !== '') {
        var newAuthor = document.createElement('div');
        newAuthor.textContent = authorName;
        authorsList.appendChild(newAuthor);

        // Agregar el autor al input de autores
        if (autoresInput.value.trim() === '') {
            autoresInput.value = authorName;
        } else {
            autoresInput.value += ', ' + authorName;
        }

        document.getElementById('nombreAutor').value = ''; // Limpiar campo de entrada
    }
}

function scrollToSection(sectionId) {
    var section = document.getElementById(sectionId);
    section.scrollIntoView({ behavior: 'smooth' });
}