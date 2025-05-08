document.getElementById('loginForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const correo = document.getElementById('correo').value;
  const contrasena = document.getElementById('contrasena').value;

  try {
      const response = await fetch('http://localhost:5000/auth/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ correo, contrasena })
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.error || 'Error desconocido');

      // Guardar token en localStorage y redirigir
      localStorage.setItem('token', data.token);
      window.location.href = '/dashboard.html';
  } catch (error) {
      document.getElementById('mensajeError').textContent = error.message;
      document.getElementById('mensajeError').classList.remove('hidden');
  }
});


