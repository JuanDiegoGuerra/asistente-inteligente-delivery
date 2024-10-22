import React, { useEffect, useState } from 'react';

const Recordatorios = () => {
  const [recordatorios, setRecordatorios] = useState([]);

  // Llamada a la API para obtener los recordatorios
  useEffect(() => {
    const fetchRecordatorios = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/recordatorios');
        const data = await response.json();
        setRecordatorios(data);
      } catch (error) {
        console.error('Error al obtener los recordatorios:', error);
      }
    };

    fetchRecordatorios();
  }, []); // El array vacío [] significa que solo se ejecuta al montar el componente

  return (
    <div>
      <h1>Lista de Recordatorios</h1>
      <ul>
        {recordatorios.map((recordatorio) => (
          <li key={recordatorio.id}>
            <h3>{recordatorio.titulo}</h3>
            <p>{recordatorio.descripcion}</p>
            <p>Fecha: {recordatorio.fecha}</p>
            <p>{recordatorio.completado ? 'Completado' : 'Pendiente'}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Recordatorios;
