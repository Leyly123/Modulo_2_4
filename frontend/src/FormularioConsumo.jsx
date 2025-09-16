import { useState } from "react";

export default function FormularioConsumo() {
  const [formData, setFormData] = useState({
    fecha: "",
    fuente: "",
    ubicacion: "",
    consumo: ""
  });

  const [mensaje, setMensaje] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!formData.fecha || !formData.fuente || !formData.ubicacion || !formData.consumo) {
      setMensaje("⚠️ Todos los campos son obligatorios.");
      return;
    }

    try {
      const response = await fetch("http://localhost:5000/add_consumo", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      const result = await response.json();

      if (response.ok) {
        setMensaje("✅ Consumo registrado en la base.");
        setFormData({ fecha: "", fuente: "", ubicacion: "", consumo: "" });
      } else {
        setMensaje("❌ Error: " + result.error);
      }
    } catch (error) {
      setMensaje("❌ Error de conexión con el backend.");
    }
  };

  return (
    <div>
      <h2>Ingreso de Consumo Energético</h2>
      <form onSubmit={handleSubmit}>
        <input type="date" name="fecha" value={formData.fecha} onChange={handleChange} />
        <select name="fuente" value={formData.fuente} onChange={handleChange}>
          <option value="">Seleccione fuente</option>
          <option value="electricidad">Electricidad</option>
          <option value="gas">Gas</option>
          <option value="solar">Solar</option>
        </select>
        <input type="text" name="ubicacion" placeholder="Ubicación" value={formData.ubicacion} onChange={handleChange} />
        <input type="number" name="consumo" placeholder="Consumo (kWh)" value={formData.consumo} onChange={handleChange} />
        <button type="submit">Guardar</button>
      </form>
      {mensaje && <p>{mensaje}</p>}
    </div>
  );
}
