
document.addEventListener("DOMContentLoaded", () => {
    const usuario = JSON.parse(localStorage.getItem("usuario"));
    if (!usuario) {
        window.location.href = "/login";  // Redirige si no hay usuario
        return;
    }
    document.getElementById("bienvenida").textContent = `Bienvenido/a, ${usuario.nombre}`;
});
