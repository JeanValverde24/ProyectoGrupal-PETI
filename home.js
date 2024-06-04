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
$('.editar-button').on('click', function(event) {
  event.preventDefault();
  var planId = $(this).data('id');
  editPlan(planId);
});

function editPlan(planId) {
  console.log('Editando plan con ID:', planId);
  window.location.href = '/editar-plan/' + planId;
}