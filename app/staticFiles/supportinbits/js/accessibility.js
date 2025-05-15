document.addEventListener('DOMContentLoaded', function() {
    const accBtn = document.getElementById('accessibility-btn');
    const accPanel = document.getElementById('accessibility-panel');
    const increaseFont = document.getElementById('increase-font');
    const decreaseFont = document.getElementById('decrease-font');
    const resetFont = document.getElementById('reset-font');
    const highContrast = document.getElementById('high-contrast');
    const resetContrast = document.getElementById('reset-contrast');
    
    // Toggle del panel
    accBtn.addEventListener('click', function() {
        accPanel.classList.toggle('hidden');
    });
    
    // Aumentar tamaño de fuente
    increaseFont.addEventListener('click', function() {
        changeFontSize(1);
    });
    
    // Disminuir tamaño de fuente
    decreaseFont.addEventListener('click', function() {
        changeFontSize(-1);
    });
    
    // Resetear tamaño de fuente
    resetFont.addEventListener('click', function() {
        document.body.style.fontSize = '';
        localStorage.removeItem('fontSize');
    });
    
    // Alto contraste
    highContrast.addEventListener('click', function() {
        document.body.classList.add('high-contrast');
        localStorage.setItem('highContrast', 'true');
    });
    
    // Contraste normal
    resetContrast.addEventListener('click', function() {
        document.body.classList.remove('high-contrast');
        localStorage.removeItem('highContrast');
    });
    
    // Cargar preferencias guardadas
    function loadPreferences() {
        // Tamaño de fuente
        const savedFontSize = localStorage.getItem('fontSize');
        if (savedFontSize) {
            document.body.style.fontSize = savedFontSize;
        }
        
        // Contraste
        if (localStorage.getItem('highContrast') === 'true') {
            document.body.classList.add('high-contrast');
        }
    }
    
    // Cambiar tamaño de fuente
    function changeFontSize(direction) {
        const currentSize = parseFloat(getComputedStyle(document.body).fontSize);
        const newSize = currentSize + (direction * 2);
        document.body.style.fontSize = `${newSize}px`;
        localStorage.setItem('fontSize', `${newSize}px`);
    }
    
    // Cargar preferencias al iniciar
    loadPreferences();
});