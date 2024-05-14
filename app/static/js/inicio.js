function mostrarContenido(id) {
    // Oculta todos los contenidos
    var contenidos = document.querySelectorAll('.contenido');
    contenidos.forEach(function(contenido) {
      contenido.style.display = 'none';
    });
    // Muestra el contenido correspondiente al ID proporcionado
    var contenidoAMostrar = document.getElementById(id);
    if (contenidoAMostrar) {
      contenidoAMostrar.style.display = 'block';
    }
  }
  