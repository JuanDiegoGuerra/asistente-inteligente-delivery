import React, { useState, useEffect } from 'react';
import '../styles/styles.css';

// Componente principal que maneja el formulario y la visualización de recordatorios
const Recordatorios = () => {
  const [recordatorios, setRecordatorios] = useState([]);
  const [titulo, setTitulo] = useState('');
  const [descripcion, setDescripcion] = useState('');
  const [fecha, setFecha] = useState('');
  const [completado, setCompletado] = useState(false);
  const [mostrarAlerta, setMostrarAlerta] = useState(false);

  // Función para obtener los recordatorios existentes
  const obtenerRecordatorios = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/recordatorios');
      const data = await response.json();
      setRecordatorios(data);
    } catch (error) {
      console.error('Error al obtener los recordatorios:', error);
    }
  };

  // Cargar los recordatorios al cargar el componente
  useEffect(() => {
    obtenerRecordatorios();
  }, []);

  useEffect(() => {
    const verificarRecordatoriosProximos = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/recordatorios/proximos');
        const data = await response.json();
        if (data.length > 0) {
          setMostrarAlerta(true);
          setTimeout(() => setMostrarAlerta(false), 5000); // Oculta la alerta después de 5 segundos
        }
      } catch (error) {
        console.error('Error al verificar recordatorios próximos:', error);
      }
    };

    const interval = setInterval(verificarRecordatoriosProximos, 60000); // Cada minuto
    return () => clearInterval(interval); // Limpia el intervalo cuando el componente se desmonta
  }, []);

  // Función para manejar la creación de nuevos recordatorios
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!fecha || isNaN(new Date(fecha).getTime())) {
      alert("Por favor ingresa una fecha válida.");
      return;
    }

    const nuevoRecordatorio = { 
      titulo, 
      descripcion, 
      fecha_vencimiento: new Date(fecha).toISOString(),
      completado 
    };

    try {
      const response = await fetch('http://127.0.0.1:8000/api/recordatorios', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(nuevoRecordatorio),
      });

      if (response.ok) {
        const data = await response.json();
        setRecordatorios((prevRecordatorios) => [...prevRecordatorios, data]);
        setTitulo('');
        setDescripcion('');
        setFecha('');
        setCompletado(false);
      } else {
        console.error('Error al crear el recordatorio:', response.status);
      }
    } catch (error) {
      console.error('Error al enviar la solicitud:', error);
    }
  };

  return (
    <div>
      <h1 className="titulo-principal">Recordatorios</h1>

      {/* Alerta de recordatorio próximo */}
      {mostrarAlerta && (
        <div className="alerta-recordatorio">
          ¡Tienes recordatorios próximos a vencer!
        </div>
      )}

      {/* Formulario para crear un nuevo recordatorio */}
      <form onSubmit={handleSubmit} className="formulario-recordatorio">
        <input 
          type="text" 
          placeholder="Título" 
          value={titulo} 
          onChange={(e) => setTitulo(e.target.value)} 
          required 
          className="input-titulo"
        />
        <textarea 
          placeholder="Descripción" 
          value={descripcion} 
          onChange={(e) => setDescripcion(e.target.value)} 
          required 
          className="input-descripcion"
        />
        <input 
          type="datetime-local" 
          value={fecha} 
          onChange={(e) => setFecha(e.target.value)} 
          required 
          className="input-fecha"
        />
        <label className="label-completado">
          Completado:
          <input 
            type="checkbox" 
            checked={completado} 
            onChange={() => setCompletado(!completado)} 
            className="input-completado"
          />
        </label>
        <button type="submit" className="boton-crear-recordatorio">Crear Recordatorio</button>
      </form>

      {/* Lista de recordatorios existentes */}
      <h2 className="titulo-lista">Lista de Recordatorios</h2>
      <ul className="lista-recordatorios">
        {recordatorios.map((recordatorio) => (
          <li key={recordatorio.id} className="item-recordatorio">
            <h4 className="recordatorio-titulo">{recordatorio.titulo}</h4>
            <p className="recordatorio-fecha">{new Date(recordatorio.fecha_vencimiento).toLocaleString()}</p>
            <p className="recordatorio-estado">{recordatorio.completado ? "Completado" : "Pendiente"}</p>
            <p className="recordatorio-descripcion">{recordatorio.descripcion}</p> 
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Recordatorios;
