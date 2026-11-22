import os
import solara
from negocio_v2 import cargar, ingreso_real, pedidos_validos

# Configuración y secreto: vienen del entorno (en Render, del panel Environment).
NOMBRE = os.environ.get("NOMBRE_APP", "Mi app")
CLAVE_ADMIN = os.environ.get("CLAVE_ADMIN", "")
# Para quién es, qué resuelve y de dónde salen los datos: se ven en pantalla.
NECESIDAD = "Para quien administra la cafetería: ¿cuánto entró de verdad a la caja en cada sede?"
FUENTE = "Datos: ventas de práctica del curso, generadas para su usuario (no son datos abiertos)."

ventas = cargar()
sede = solara.reactive("Centro")
clave = solara.reactive("")

@solara.component
def Page():
    solara.Markdown(f"# {NOMBRE}\n\n{NECESIDAD}")
    solara.Select(label="Sede", value=sede, values=["Centro", "Norte", "Sur"])
    solara.Markdown(f"Ingreso real de {sede.value}: {ingreso_real(ventas, sede.value)}")
    solara.Markdown(f"Pedidos válidos: {pedidos_validos(ventas, sede.value)}")
    solara.InputText("Clave de administración", value=clave, password=True)
    if CLAVE_ADMIN and clave.value == CLAVE_ADMIN:
        solara.DataFrame(ventas[ventas["sede"] == sede.value])
    solara.Markdown(FUENTE)
