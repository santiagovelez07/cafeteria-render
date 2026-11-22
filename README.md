# Cafetería — ingreso real por sede
- URL pública: https://cafeteria-render.onrender.com
- Repositorio: https://github.com/santiagovelez07/cafeteria-render
- Correr: `docker build -t mi-app . && docker run --rm -p 8765:8765 --env-file .env mi-app` y abrir http://localhost:8765
- Datos: ventas de práctica del curso (en su proyecto: nombre de la fuente abierta, enlace y licencia)
- Variables: `NOMBRE_APP`, `CLAVE_ADMIN` (se configuran en Render; copie `.env.example` como `.env` para correrla local)
