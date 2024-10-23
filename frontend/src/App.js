// src/App.js
import React from 'react';
import './App.css';
import Recordatorios from './components/Recordatorios';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Mis Recordatorios</h1>
        <Recordatorios />
      </header>
    </div>
  );
}

export default App;
