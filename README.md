# ⚡ Flujo del Proyecto

Este proyecto implementa un **circuito completo de captura, almacenamiento y visualización de datos de consumo energético**, integrando **React, Flask API, SQLite y Power BI**.  

---

## 🔹 1. Frontend (React)
- Formulario en **React** para el ingreso de consumos energéticos.  
- Valida los datos (fecha, fuente, ubicación y consumo en kWh).  
- Envía la información mediante **fetch** a la API del backend.  

---

## 🔹 2. Backend (Flask API + SQLite)
- La **API en Flask** recibe los datos enviados desde el frontend.  
- Los registros se guardan en la base de datos **SQLite (`energy_data.db`)**.  
- Se puede administrar con **DB Browser for SQLite**.  
- Endpoints disponibles:
  - `POST /add_consumo` → Inserta un nuevo consumo.  
  - `GET /get_consumos` → Lista todos los consumos registrados.  

---

## 🔹 3. Procesamiento (Python)
- El script `procesamiento.py` se conecta a la base de datos **`energy_data.db`**.  
- Extrae todos los consumos (incluyendo los nuevos registros).  
- Genera automáticamente un archivo **CSV actualizado** con la información completa.  

---

## 🔹 4. Visualización (Power BI)
- El **CSV generado** es la fuente de datos para un **dashboard en Power BI**.  
- El dashboard se **actualiza automáticamente** cuando se agregan nuevos consumos desde el formulario.  
- Permite visualizar y analizar métricas de consumo energético.  

---

## 🔄 Flujo Resumido

```mermaid
graph LR
A[🖥️ React<br/>Formulario] --> B[🌐 Flask API]
B --> C[🗄️ SQLite<br/>energy_data.db]
C --> D[🐍 procesamiento.py<br/>CSV actualizado]
D --> E[📊 Power BI<br/>Dashboard dinámico]
