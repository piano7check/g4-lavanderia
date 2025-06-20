document.addEventListener('DOMContentLoaded', async () => {
    const usuario = JSON.parse(localStorage.getItem('usuario'));
    if (!usuario) {
        alert("Inicia sesión primero");
        window.location.href = "/login";
        return;
    }

    try {
        const response = await fetch(`/api/solicitudes/residente/${usuario.id}`);
        const data = await response.json();

        const tabla = document.getElementById('tablaSolicitudes');
        tabla.innerHTML = '';

        data.forEach(solicitud => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td class="px-4 py-2">${usuario.nombre}</td>
                <td class="px-4 py-2">${solicitud.fecha_solicitud}</td>
                <td class="px-4 py-2">${solicitud.estado}</td>
            `;
            tabla.appendChild(tr);
        });
    } catch (err) {
        console.error('Error al cargar solicitudes', err);
        alert('Error al obtener las solicitudes');
    }
});
