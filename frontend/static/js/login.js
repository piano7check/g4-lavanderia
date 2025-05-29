document.getElementById("loginForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const res = await fetch("http://localhost:5000/api/auth/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ correo: email, contrasena: password }),
  });

  const data = await res.json();

  if (!response.ok) throw new Error(data.error || 'Error desconocido');

    const { token, user } = data;
    localStorage.setItem('token', token);
    localStorage.setItem('tipo_usuario', user.tipo_usuario);

    // Redirige según el rol
    if (user.tipo_usuario === 'superadministrador') {
        window.location.href = '/admin/superdashboard.html';
    } else if (user.tipo_usuario === 'administrador') {
        window.location.href = '/admin/dashboard.html';
    } else {
        window.location.href = '/student/dashboard.html';
    }

});
