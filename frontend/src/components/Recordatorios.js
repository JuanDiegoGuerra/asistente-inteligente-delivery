import React, { useState, useEffect } from 'react';

// Componente principal que maneja el formulario y la visualización de recordatorios
const Recordatorios = () => {
  const [recordatorios, setRecordatorios] = useState([]);
  const [titulo, setTitulo] = useState('');
  const [descripcion, setDescripcion] = useState('');
  const [fecha, setFecha] = useState('');
  const [completado, setCompletado] = useState(false);

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

  // Función para manejar la creación de nuevos recordatorios
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Convierte la fecha en un formato compatible con FastAPI (ISO 8601)
    const fechaFormateada = new Date(fecha).toISOString();
    
    const nuevoRecordatorio = { 
        titulo, 
        descripcion, 
        fecha: fechaFormateada, // Usamos la fecha formateada
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
            console.log('Recordatorio creado:', data);
        } else {
            console.error('Error al crear el recordatorio:', response.status);
        }
    } catch (error) {
        console.error('Error en la solicitud:', error);
    }
};

  return (
    <div>
      <h1>Recordatorios</h1>
      
      {/* Formulario para crear un nuevo recordatorio */}
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          placeholder="Título" 
          value={titulo} 
          onChange={(e) => setTitulo(e.target.value)} 
          required 
        />
        <textarea 
          placeholder="Descripción" 
          value={descripcion} 
          onChange={(e) => setDescripcion(e.target.value)} 
          required 
        />
        <input 
          type="datetime-local" 
          value={fecha} 
          onChange={(e) => setFecha(e.target.value)} 
          required 
        />
        <label>
          Completado:
          <input 
            type="checkbox" 
            checked={completado} 
            onChange={() => setCompletado(!completado)} 
          />
        </label>
        <button type="submit">Crear Recordatorio</button>
      </form>

      {/* Lista de recordatorios existentes */}
      <h2>Lista de Recordatorios</h2>
      <ul>
        {recordatorios.map((recordatorio) => (
          <li key={recordatorio.id}>
            {recordatorio.titulo} - {new Date(recordatorio.fecha).toLocaleString()} 
            - {recordatorio.completado ? 'Completado' : 'Pendiente'}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Recordatorios;
