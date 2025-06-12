module.exports = {
  content: [
    "../templates/auth/*.html",    // Ruta relativa desde la carpeta tailwind/
    "../templates/**/*.html"       // Escanea todos los HTML en subcarpetas
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}