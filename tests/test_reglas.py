from negocio_v2 import cargar, pedidos_validos

def test_pedidos_validos_no_superan_los_pedidos_de_la_sede():
    ventas = cargar()
    for sede in ["Centro", "Norte", "Sur"]:
        assert pedidos_validos(ventas, sede) <= int((ventas["sede"] == sede).sum())
