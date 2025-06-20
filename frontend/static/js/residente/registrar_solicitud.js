// frontend/static/js/residente/registrar_solicitud.js

let listaPrendas = [];

document.getElementById('formAgregarPrenda').addEventListener('submit', function(e) {
    e.preventDefault();

    const tipo = document.getElementById('tipoPrenda').value;
    const cantidad = parseInt(document.getElementById('cantidadPrenda').value);
    const color = document.getElementById('colorPrenda').value;

    const total = listaPrendas.reduce((sum, p) => sum + p.cantidad, 0);
    if (total + cantidad > 12) {
        alert("Solo puedes registrar hasta 12 prendas por solicitud");
        return;
    }

    listaPrendas.push({ tipo_prenda: tipo, cantidad, color_descripcion: color });
    actualizarLista();
    e.target.reset();
});

function actualizarLista() {
    const lista = document.getElementById('listaPrendas');
    lista.innerHTML = '';
    listaPrendas.forEach(p => {
        const li = document.createElement('li');
        li.textContent = `${p.cantidad} ${p.tipo_prenda}(s) - ${p.color_descripcion}`;
        lista.appendChild(li);
    });
}

document.getElementById('btnEnviarSolicitud').addEventListener('click', async () => {
    const usuario = JSON.parse(localStorage.getItem('usuario'));
    if (!usuario || !usuario.id) return alert("Inicia sesión primero.");

    if (listaPrendas.length === 0) {
        alert("Agrega al menos una prenda");
        return;
    }

    try {
        const response = await fetch('/api/solicitudes', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id_usuario: usuario.id,  
                prendas: listaPrendas
            })
        });

        const data = await response.json();
        if (response.ok) {
            alert("✅ Solicitud registrada exitosamente");
            listaPrendas = [];
            actualizarLista();
        } else {
            alert("❌ Error: " + data.error);
        }
    } catch (err) {
        alert("Error de red");
        console.error(err);
    }
});
