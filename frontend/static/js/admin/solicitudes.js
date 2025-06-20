// solicitudes.js

document.addEventListener('DOMContentLoaded', async () => {
    try {
        const response = await fetch('/api/admin/solicitudes');
        const solicitudes = await response.json();

        const tabla = document.getElementById('tablaSolicitudes');
        tabla.innerHTML = '';

        solicitudes.forEach(s => {
            const tr = document.createElement('tr');

            tr.innerHTML = `
                <td class="p-3 border">${s.id}</td>
                <td class="p-3 border">${s.id_usuario}</td>
                <td class="p-3 border">${s.nombre_usuario}</td>
                <td class="p-3 border">${s.fecha_solicitud}</td>
                <td class="p-3 border">
                    <select data-id="${s.id}" class="estadoSolicitud border rounded p-1">
                        ${generarOpcionesEstado(s.estado)}
                    </select>
                </td>
                <td class="p-3 border">
                    <button class="bg-green-600 text-white px-3 py-1 rounded hover:bg-green-700 notificarBtn" data-id="${s.id}">
                        Notificar
                    </button>
                </td>
            `;
            tabla.appendChild(tr);
        });

        // Evento para cambiar estado (guardamos luego)
        document.querySelectorAll('.estadoSolicitud').forEach(select => {
            select.addEventListener('change', async (e) => {
                const id = e.target.getAttribute('data-id');
                const nuevoEstado = e.target.value;

                await fetch(`/api/admin/solicitudes/${id}/estado`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ estado: nuevoEstado })
                });

                alert(`Estado actualizado a ${nuevoEstado}`);
            });
        });

        // Evento de notificación (solo simulado por ahora)
        document.querySelectorAll('.notificarBtn').forEach(btn => {
            btn.addEventListener('click', () => {
                const id = btn.getAttribute('data-id');
                alert(`Solicitud ${id} notificada al residente.`);
                // Aquí puedes agregar lógica real luego (por ejemplo, correo o notificación interna)
            });
        });

    } catch (error) {
        console.error("Error al cargar solicitudes", error);
    }
});

// Generar opciones del select con estado actual seleccionado
function generarOpcionesEstado(actual) {
    const opciones = ['pendiente', 'aceptado', 'rechazado', 'en proceso', 'listo para recoger', 'entregado'];
    return opciones.map(estado => {
        return `<option value="${estado}" ${estado === actual ? 'selected' : ''}>${estado}</option>`;
    }).join('');
}
