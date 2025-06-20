// // frontend/static/js/login.js
document.getElementById('loginForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const correo = document.getElementById('correo').value;
    const contrasena = document.getElementById('contrasena').value;

    try {
        const response = await fetch('http://localhost:5000/api/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ correo, contrasena })
        });

        const data = await response.json();

        if (response.ok) {
            // GUARDAR USUARIO COMO OBJETO
            const usuario = {
                id: data.usuario.id,
                nombre: data.usuario.nombre,
                tipo_usuario: data.usuario.tipo_usuario
            };
            localStorage.setItem('usuario', JSON.stringify(usuario));

            // Redirección
            if (usuario.tipo_usuario === 'Administrador') {
                window.location.href = '/admin/dashboard';
            } else if (usuario.tipo_usuario === 'Residente') {
                window.location.href = '/residente/bienvenida';
            } else {
                alert('Tipo de usuario no reconocido');
            }
        } else {
            alert(data.error || 'Error al iniciar sesión');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error de red');
    }
});
