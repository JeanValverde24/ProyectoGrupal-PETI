document.querySelectorAll('.accordion-btn').forEach(button => {
  button.addEventListener('click', function() {
    const panel = this.nextElementSibling;
    panel.classList.toggle('active');
    if (panel.classList.contains('active')) {
      closeOtherPanels(panel);
    }
  });
});

function closeOtherPanels(currentPanel) {
  document.querySelectorAll('.accordion-panel').forEach(panel => {
    if (panel !== currentPanel && panel.classList.contains('active')) {
      panel.classList.remove('active');
    }
  });
}
