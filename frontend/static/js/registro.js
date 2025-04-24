document.getElementById('registroForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const nombre = document.getElementById('nombre').value;
    const correo = document.getElementById('correo').value;
    const contrasena = document.getElementById('contrasena').value;
    const tipo_usuario = document.getElementById('tipo_usuario').value;

    const datosUsuario = {
        nombre,
        correo,
        contrasena,
        tipo_usuario
    };

    try {
        const response = await fetch('/api/auth/usuarios', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(datosUsuario)
        });

        const data = await response.json();

        if (response.status === 201) {
            alert('Usuario registrado exitosamente');
        } else {
            alert('Error: ' + data.mensaje);
        }
    } catch (error) {
        console.error('Error al registrar el usuario:', error);
        alert('Ocurrió un error al procesar la solicitud.');
    }
});
