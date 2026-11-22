import os
import solara
from negocio_v2 import cargar, ingreso_real, pedidos_validos

# Configuración y secreto: vienen del entorno, nunca del código.
NOMBRE = os.environ.get("NOMBRE_APP", "Mi app")
CLAVE_ADMIN = os.environ.get("CLAVE_ADMIN", "")

ventas = cargar()
sede = solara.reactive("Centro")
clave = solara.reactive("")

@solara.component
def Page():
    solara.Markdown(f"# {NOMBRE}")
    solara.Select(label="Sede", value=sede, values=["Centro", "Norte", "Sur"])
    solara.Markdown(f"Ingreso real de {sede.value}: {ingreso_real(ventas, sede.value)}")
    solara.Markdown(f"Pedidos válidos: {pedidos_validos(ventas, sede.value)}")
    solara.InputText("Clave de administración", value=clave, password=True)
    if CLAVE_ADMIN and clave.value == CLAVE_ADMIN:
        solara.DataFrame(ventas[ventas["sede"] == sede.value])
