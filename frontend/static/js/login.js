// frontend/static/js/login.js

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
            // Guarda el token y tipo de usuario si deseas
            localStorage.setItem('token', data.token);
            localStorage.setItem('nombre', data.usuario.nombre);
            localStorage.setItem('tipo_usuario', data.usuario.tipo_usuario);

            // Redirige según tipo de usuario
            if (data.usuario.tipo_usuario === 'Administrador') {
                window.location.href = '/admin/dashboard'; //RUTA del administrador QUE IRA EN VIEW_ROUTES COMO PARAMETRO DE LA FUNCION DEBE SER EXACTAMENTE IGUAL A ESTA 
            } else if (data.usuario.tipo_usuario === 'Residente') {
                window.location.href = '/residente/bienvenida'; //RUTA del residente QUE IRA EN VIEW_ROUTES COMO PARAMETRO DE LA FUNCION DEBE SER EXACTAMENTE IGUAL A ESTA pero para residente en este caso
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



//'http://localhost:5000/api/auth/login'
        
