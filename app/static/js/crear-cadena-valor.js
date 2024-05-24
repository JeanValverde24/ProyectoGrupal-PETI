function toggleCell(cell) {
    var row = cell.parentNode;
    var cells = row.getElementsByClassName('cell');
    for (var i = 0; i < cells.length; i++) {
        cells[i].innerHTML = '';
    }
    cell.innerHTML = 'x';
}

function addFortaleza() {
    var fortalezasDiv = document.getElementById('fortalezas');
    var count = fortalezasDiv.getElementsByClassName('fortaleza').length + 1;
    var newInput = document.createElement('input');
    newInput.type = 'text';
    newInput.name = 'fortaleza' + count;
    newInput.className = 'fortaleza';
    newInput.placeholder = 'F' + count + ':';
    fortalezasDiv.appendChild(newInput);
}

function addDebilidad() {
    var debilidadesDiv = document.getElementById('debilidades');
    var count = debilidadesDiv.getElementsByClassName('debilidad').length + 1;
    var newInput = document.createElement('input');
    newInput.type = 'text';
    newInput.name = 'debilidad' + count;
    newInput.className = 'debilidad';
    newInput.placeholder = 'D' + count + ':';
    debilidadesDiv.appendChild(newInput);
}
