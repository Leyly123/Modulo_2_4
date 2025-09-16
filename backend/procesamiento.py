import sqlite3
import pandas as pd

conn = sqlite3.connect("energy_data.db")

df = pd.read_sql_query("SELECT * FROM consumos", conn)

print("✅ Datos extraídos de la base de datos:")
print(df) 

df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce", format="mixed")

df["mes"] = df["fecha"].dt.to_period("M")

reporte = df.groupby(["mes", "fuente", "ubicacion"])["consumo_kwh"].sum().reset_index()

print("\n✅ Reporte agregado:")
print(reporte)

reporte.to_csv("reporte_consumo_mensual.csv", index=False, encoding="utf-8-sig")
print("\n✅ Archivo 'reporte_consumo_mensual.csv' generado con éxito.")
