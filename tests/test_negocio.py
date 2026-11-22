import csv
from negocio_v2 import cargar, ingreso_real

def test_centro_por_otro_camino():
    with open("ventas.csv", encoding="utf-8") as f:
        pagados = [int(fila["valor"]) for fila in csv.DictReader(f) if fila["sede"] == "Centro" and fila["estado"] == "pagado"]
    assert ingreso_real(cargar(), "Centro") == sum(pagados)

def test_cifra_de_control():
    assert ingreso_real(cargar(), "Centro") == 573500
