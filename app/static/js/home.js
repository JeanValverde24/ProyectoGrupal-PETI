// Agregar event listener para cada botón de acordeón
document.querySelectorAll('.accordion-btn').forEach(button => {
  button.addEventListener('click', function() {
    // Obtener el panel asociado al botón de acordeón
    const panel = this.nextElementSibling;
    
    // Toggle de la clase 'active' para mostrar/ocultar el contenido adicional
    panel.classList.toggle('active');
    
    // Si el panel está activo, cerrar todos los demás paneles
    if (panel.classList.contains('active')) {
      closeOtherPanels(panel);
    }
  });
});

// Función para cerrar todos los demás paneles excepto el panel actual
function closeOtherPanels(currentPanel) {
  document.querySelectorAll('.accordion-panel').forEach(panel => {
    if (panel !== currentPanel && panel.classList.contains('active')) {
      panel.classList.remove('active');
    }
  });
}
