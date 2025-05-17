const toggleBtn = document.getElementById('toggle-mode');
const body = document.body;

toggleBtn.addEventListener('click', () => {
  body.classList.toggle('dark-mode');

  // Cambiar el texto del botón según el modo actual
  if (body.classList.contains('dark-mode')) {
    toggleBtn.innerHTML = '<i class="bi bi-sun-fill p-2"></i>';
  } else {
    toggleBtn.innerHTML = '<i class="bi bi-moon-fill p-2"></i>';
  }
});

