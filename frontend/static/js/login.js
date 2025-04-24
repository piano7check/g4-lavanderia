document.getElementById("loginForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  const res = await fetch("/api/auth/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ correo: email, contrasena: password }),
  });

  const data = await res.json();

  if (res.ok) {
    // El token ya se guarda en la sesión del servidor
    window.location.href = "/dashboard";  // Redirige al dashboard
  } else {
    document.getElementById("errorMessage").textContent = data.message || "Error al iniciar sesión";
    document.getElementById("errorMessage").classList.remove("hidden");
  }
});
