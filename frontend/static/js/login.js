document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("loginForm");
    if (!form) return;

    form.addEventListener("submit", async function(e) {
        e.preventDefault();
        
        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value;

        try {
            const response = await fetch("http://127.0.0.1:5000/api/auth/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                credentials: "include",
                body: JSON.stringify({
                    correo: email,
                    contrasena: password
                })
            });

            const data = await response.json();

            if (response.ok) {
                localStorage.setItem('token', data.token);
                window.location.href = "/dashboard";
            } else {
                alert(data.message || "Error al iniciar sesión");
            }
        } catch (error) {
            console.error("Error:", error);
            alert("Error de conexión con el servidor");
        }
    });
});