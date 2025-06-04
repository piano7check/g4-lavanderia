// usuarios.js
document.getElementById('usuarioForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const nombre = document.getElementById('nombre').value;
    const correo = document.getElementById('correo').value;
    const contrasena = document.getElementById('contrasena').value;
    const tipo_usuario = document.getElementById('tipo_usuario').value;

    try {
        const response = await fetch('/api/usuarios', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ nombre, correo, contrasena, tipo_usuario })
        });

        const data = await response.json();

        if (response.ok) {
            alert(data.mensaje);
            document.getElementById('usuarioForm').reset();
            document.getElementById('modal-registro').classList.add('hidden');
        } else {
            alert(data.error);
        }

    } catch (error) {
        console.error('Error al registrar usuario:', error);
        alert('Error del servidor. Intente más tarde.');
    }
});

// Mostrar el modal al hacer clic en "+ Nuevo"
document.getElementById('btn-nuevo').addEventListener('click', () => {
    document.getElementById('modal-registro').classList.remove('hidden');
});

// Ocultar modal al hacer clic en "Cancelar"
document.getElementById('cancelarModal').addEventListener('click', () => {
    document.getElementById('modal-registro').classList.add('hidden');
});
