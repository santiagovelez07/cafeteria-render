import pandas as pd

def cargar():
    return pd.read_csv("ventas.csv")

def ingreso_real(df, sede):
    return int(df[(df["sede"] == sede) & (df["estado"] == "pagado")]["valor"].sum())

def pedidos_validos(df, sede):
    return int(((df["sede"] == sede) & (df["estado"] == "pagado")).sum())
