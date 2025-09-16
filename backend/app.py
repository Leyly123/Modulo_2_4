from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

DB_NAME = "energy_data.db"

# Endpoint para insertar un nuevo consumo
@app.route("/add_consumo", methods=["POST"])
def add_consumo():
    data = request.json
    fecha = data.get("fecha")
    fuente = data.get("fuente")
    ubicacion = data.get("ubicacion")
    consumo = data.get("consumo")

    if not fecha or not fuente or not ubicacion or not consumo:
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    try:
        if len(fecha) == 10:  
            fecha = fecha + " 00:00:00"

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO consumos (fecha, fuente, ubicacion, consumo_kwh) VALUES (?, ?, ?, ?)",
            (fecha, fuente, ubicacion, consumo),
        )
        conn.commit()
        conn.close()
        return jsonify({"message": "✅ Consumo agregado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint para listar todos los consumos
@app.route("/get_consumos", methods=["GET"])
def get_consumos():
    try:
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM consumos")
        rows = cursor.fetchall()
        conn.close()

        data = [dict(row) for row in rows]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
