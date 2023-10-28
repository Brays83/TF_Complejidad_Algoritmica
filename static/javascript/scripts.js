    const raitingRange = document.getElementById('raitingRange');
    const raitingValue = document.getElementById('raitingValue');

    raitingRange.addEventListener('input', function() {
        raitingValue.textContent = raitingRange.value;
    });s
