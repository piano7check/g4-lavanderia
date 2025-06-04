// usuarios.js
document.getElementById('usuarioForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const nombre = document.getElementById('nombre').value;
    const correo = document.getElementById('correo').value;
    const contrasena = document.getElementById('contrasena').value;
    const tipo_usuario = document.getElementById('tipo_usuario').value;

    const token = localStorage.getItem('token');

    const response = await fetch('/api/usuarios', { //va al user_router es decir la api de usuarios
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        },
        body: JSON.stringify({ nombre, correo, contrasena, tipo_usuario })
    });

    const mensaje = document.getElementById('mensaje');

    if (response.ok) {
        const data = await response.json();
        mensaje.textContent = data.mensaje;
    } else {
        mensaje.textContent = "Error al crear usuario.";
        mensaje.classList.add('text-red-600');
    }
});
