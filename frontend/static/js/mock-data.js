// Simula datos del backend
const mockBackendData = {
    current_user: {
        nombre: "Galia Almaraz",
        role: "admin"
    },
    stats: {
        usuarios_registrados: 1248,
        servicios_activos: 87,
        ingresos_hoy: 2450
    }
};

// Renderiza los datos en el HTML
document.addEventListener('DOMContentLoaded', () => {
    // Actualiza el nombre del usuario
    document.querySelector('#user-name').textContent = mockBackendData.current_user.nombre;
    
    // Renderiza las tarjetas de estadísticas
    const contentDiv = document.getElementById('content');
    contentDiv.innerHTML = `
        <div class="bg-white p-6 rounded-lg shadow">
            <h3 class="font-medium text-gray-900">Usuarios registrados</h3>
            <p class="text-3xl font-bold mt-2">${mockBackendData.stats.usuarios_registrados}</p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow">
            <h3 class="font-medium text-gray-900">Servicios activos</h3>
            <p class="text-3xl font-bold mt-2">${mockBackendData.stats.servicios_activos}</p>
        </div>
        <div class="bg-white p-6 rounded-lg shadow">
            <h3 class="font-medium text-gray-900">Ingresos hoy</h3>
            <p class="text-3xl font-bold mt-2">$${mockBackendData.stats.ingresos_hoy}</p>
        </div>
    `;
});