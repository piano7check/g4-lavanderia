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

let listaUsuarios = [];  // Se guarda aquí para poder buscar dinamicamente

// Cargar usuarios desde el backend
async function cargarUsuarios() {
    try {
        const res = await fetch('/api/usuarios');
        const data = await res.json();
        listaUsuarios = data;  //guardamos la lista completa
        mostrarUsuarios(data); // Mostramos todos al inicio en usuarios.html
    } catch (err) {
        console.error("Error al cargar usuarios:", err);
    }
}

// Mostrar los usuarios en la tabla HTML
function mostrarUsuarios(usuarios) {
    const tbody = document.getElementById('usuarios-body');
    tbody.innerHTML = '';  //limpia tabla

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
                <button class="text-blue-500 hover:text-blue-700"><i class="fas fa-edit"></i></button>
                <button class="text-red-500 hover:text-red-700 ml-2"><i class="fas fa-trash-alt"></i></button>
            </td>
        `;

        tbody.appendChild(tr);
    });
}
// Evento para buscar mientras escribe
document.getElementById('buscarInput').addEventListener('input', (e) => {
    const texto = e.target.value.toLowerCase();

    const filtrados = listaUsuarios.filter(u =>
        u.nombre.toLowerCase().includes(texto)
    );

    mostrarUsuarios(filtrados);
});
document.addEventListener('DOMContentLoaded', () => {
    cargarUsuarios();  //Trae los usuarios desde el backend
});
//Muestra los usuarios al entrar a la pagina
document.addEventListener('DOMContentLoaded', () => {
    cargarUsuarios();  //Trae los usuarios desde el backend
});

