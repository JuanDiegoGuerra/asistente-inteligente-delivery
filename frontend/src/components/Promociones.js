// src/components/Promociones.js
import React, { useEffect, useState } from 'react';
import { obtenerPromociones } from '../api';

const Promociones = () => {
  const [promociones, setPromociones] = useState([]);

  useEffect(() => {
    const fetchPromociones = async () => {
      try {
        const data = await obtenerPromociones();
        setPromociones(data);
      } catch (error) {
        console.error('Error al obtener las promociones:', error);
      }
    };

    fetchPromociones();
  }, []);

  return (
    <div>
      <h1>Promociones</h1>
      <ul>
        {promociones.map((promocion) => (
          <li key={promocion.id}>{promocion.tipo_comida} - {promocion.horario}</li>
        ))}
      </ul>
    </div>
  );
};

export default Promociones;
