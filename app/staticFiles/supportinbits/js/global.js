const toggleBtn = document.getElementById('toggle-mode');
const body = document.body;

toggleBtn.addEventListener('click', () => {
  body.classList.toggle('dark-mode');

  // Cambiar el texto del botón según el modo actual
  if (body.classList.contains('dark-mode')) {
    toggleBtn.textContent = 'Modo Claro ☀️';
  } else {
    toggleBtn.textContent = 'Modo Oscuro 🌙';
  }
});
console.log("hola");