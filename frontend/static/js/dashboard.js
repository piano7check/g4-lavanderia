// document.addEventListener("DOMContentLoaded", () => {
//     const token = localStorage.getItem('token');
//     const usuario = JSON.parse(localStorage.getItem('usuario'));

//     if (!token || !usuario) {
//         window.location.href = "/login";
//         return;
//     }

//     // Validamos el token accediendo al dashboard con headers
//     fetch("/dashboard", {
//         method: "GET",
//         headers: {
//             "Authorization": "Bearer " + token
//         }
//     }).then(res => {
//         if (res.redirected) {
//             window.location.href = res.url;
//         } else {
//             document.getElementById("nombreUsuario").textContent = usuario.nombre || usuario.correo;
//         }
//     });

//     document.getElementById("cerrarSesion").addEventListener("click", () => {
//         localStorage.removeItem("token");
//         localStorage.removeItem("usuario");
//         window.location.href = "/login";
//     });
// });
document.addEventListener("DOMContentLoaded", () => {
    const usuario = JSON.parse(localStorage.getItem("usuario"));
    if (!usuario) {
        window.location.href = "/login";  // Redirige si no hay usuario
        return;
    }
    document.getElementById("bienvenida").textContent = `Bienvenido/a, ${usuario.nombre}`;
});
