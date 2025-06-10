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

document.addEventListener('DOMContentLoaded', () => {
    cargarUsuarios(); // Mostrar usuarios al cargar
    configurarEventos(); // Asignar eventos iniciales
});

let listaUsuarios = []; // Lista global para búsqueda y edición

// Configurar eventos iniciales
function configurarEventos() {
    // Abrir modal al presionar el boton del nuevo
    document.getElementById('btn-nuevo').addEventListener('click', () => {
        document.getElementById('usuarioForm').reset();
        delete document.getElementById('usuarioForm').dataset.editando;
        document.getElementById('modal-registro').classList.remove('hidden');
        document.querySelector('#modal-registro h2').textContent = 'Registrar nuevo usuario';
        document.querySelector('#usuarioForm button[type="submit"]').textContent = 'Guardar';
    });
    // Cancelar modal
    document.getElementById('cancelarModal').addEventListener('click', () => {
        document.getElementById('modal-registro').classList.add('hidden');
    });

    // Búsqueda dinámica
    document.getElementById('buscarInput').addEventListener('input', (e) => {
        const texto = e.target.value.toLowerCase();
        const filtrados = listaUsuarios.filter(u =>
            u.nombre.toLowerCase().includes(texto)
        );
        mostrarUsuarios(filtrados);
    });

    // Manejo de formulario (crear o editar)
    document.getElementById('usuarioForm').addEventListener('submit', async function (e) {
        e.preventDefault();

        const idEditar = this.dataset.editando;
        const nombre = document.getElementById('nombre').value;
        const correo = document.getElementById('correo').value;
        const contrasena = document.getElementById('contrasena').value;
        const tipo_usuario = document.getElementById('tipo_usuario').value;
        const datos = { nombre, correo, contrasena, tipo_usuario };

        try {
            let res;
            if (idEditar) {
                res = await fetch(`/api/usuarios/${idEditar}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(datos)
                });
                alert(res.ok ? "Usuario actualizado correctamente" : "Error al actualizar");
            } else {
                res = await fetch('/api/usuarios', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(datos)
                });
                alert(res.ok ? "Usuario creado correctamente" : "Error al crear");
            }
            this.reset();
            delete this.dataset.editando;
            document.querySelector('#usuarioForm button[type="submit"]').textContent = 'Guardar';
            document.querySelector('#modal-registro h2').textContent = 'Registrar nuevo usuario';
            document.getElementById('modal-registro').classList.add('hidden');
            cargarUsuarios(); // Recargar usuarios actualizados
        } catch (err) {
            console.error('Error al guardar usuario:', err);
            alert('Error del servidor');
        }
    });
}
document.getElementById('btn-admins').addEventListener('click', () => {
    filtrarPorTipo('Administrador');
});

document.getElementById('btn-residentes').addEventListener('click', () => {
    filtrarPorTipo('Residente');
});


// Cargar usuarios desde el backend
async function cargarUsuarios() {
    try {
        const res = await fetch('/api/usuarios');
        const data = await res.json();
        listaUsuarios = data;
        mostrarUsuarios(data);
    } catch (err) {
        console.error("Error al cargar usuarios:", err);
    }
}
function filtrarPorTipo(tipo) {
    const filtrados = listaUsuarios.filter(u => u.tipo_usuario === tipo);
    mostrarUsuarios(filtrados);
}

// Mostrar los usuarios en la tabla
function mostrarUsuarios(usuarios) {
    const tbody = document.getElementById('usuarios-body');
    tbody.innerHTML = '';

    if (usuarios.length === 0) {
        tbody.innerHTML = `<tr><td colspan="3" class="text-center py-4">No hay usuarios.</td></tr>`;
        return;
    }

    usuarios.forEach(usuario => {
        const tr = document.createElement('tr');
        tr.classList.add("hover:bg-gray-100");
        tr.innerHTML = `
            <td class="py-2 px-4 border">${usuario.nombre}</td>
            <td class="py-2 px-4 border">${usuario.tipo_usuario}</td>
            <td class="py-2 px-4 border text-center">
            
                <img src="../../static/img/icon-editar.png" 
                    alt="Editar" class="cursor-pointer inline editar-usuario" data-id="${usuario.id}">
            
                <img src="../../static/img/icon-eliminar.png" 
                    alt="Eliminar" class="cursor-pointer inline eliminar-usuario" data-id="${usuario.id}">
            </td>`;
        tbody.appendChild(tr);
    });

    // Asignar eventos a los botones editar (después de renderizar)
    document.querySelectorAll('.editar-usuario').forEach(boton => {
        boton.addEventListener('click', () => {
            const userId = boton.dataset.id;
            const usuario = listaUsuarios.find(u => u.id == userId);

            if (usuario) {
                document.getElementById('nombre').value = usuario.nombre;
                document.getElementById('correo').value = usuario.correo;
                document.getElementById('contrasena').value = usuario.contrasena; //Con la opcion de tambien editar la contrasena
                document.getElementById('tipo_usuario').value = usuario.tipo_usuario;

                document.getElementById('usuarioForm').dataset.editando = userId;

                document.querySelector('#modal-registro h2').textContent = 'Editar usuario';
                document.querySelector('#usuarioForm button[type="submit"]').textContent = 'Actualizar';
                document.getElementById('modal-registro').classList.remove('hidden');
            }
        });
    });
}

let usuarioAEliminar = null; //guarda temporalmente el ID

// Delegamos el evento para boton de eliminar
document.addEventListener('click', function (e) {
    if (e.target.classList.contains('eliminar-usuario')) {
        usuarioAEliminar = e.target.dataset.id;
        document.getElementById('modal-confirmar-eliminar').classList.remove('hidden');
    }
});

// Botón "No" → cierra el modal
document.getElementById('cancelarEliminar').addEventListener('click', () => {
    usuarioAEliminar = null;
    document.getElementById('modal-confirmar-eliminar').classList.add('hidden');
});

// Botón "Sí" → elimina el usuario
document.getElementById('confirmarEliminar').addEventListener('click', async () => {
    if (!usuarioAEliminar) return;

    try {
        const res = await fetch(`/api/usuarios/${usuarioAEliminar}`, {
            method: 'DELETE'
        });

        if (res.ok) {
            alert('Usuario eliminado correctamente.');
            cargarUsuarios(); //Refresca la lista
        } else {
            alert('Error al eliminar el usuario.');
        }
    } catch (err) {
        console.error('Error al eliminar usuario:', err);
        alert('Ocurrió un error. Inténtelo más tarde.');
    }

    usuarioAEliminar = null;
    document.getElementById('modal-confirmar-eliminar').classList.add('hidden');
});
