document.addEventListener('DOMContentLoaded', function() {
    const btnAtras = document.getElementById('btn-atras');
    if (btnAtras) {
      btnAtras.addEventListener('click', function() {
        window.location.href = '/crear-plan';
      });
    }
  });
  