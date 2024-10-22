// src/api.js
import apiClient from './axiosConfig';

// Función para obtener los recordatorios
export const obtenerRecordatorios = async () => {
  try {
    const response = await apiClient.get('/recordatorios');
    return response.data;
  } catch (error) {
    console.error('Error al obtener los recordatorios:', error);
    throw error;
  }
};
