import React, { useState } from 'react';

const RecordatorioForm = () => {
  const [titulo, setTitulo] = useState('');
  const [descripcion, setDescripcion] = useState('');
  const [fecha, setFecha] = useState('');
  const [completado, setCompletado] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const nuevoRecordatorio = { titulo, descripcion, fecha, completado };
    
    const response = await fetch('http://127.0.0.1:8000/api/recordatorios', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(nuevoRecordatorio),
    });

    const data = await response.json();
    console.log('Recordatorio creado:', data);
  };

  return (
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
  );
};

export default RecordatorioForm;
