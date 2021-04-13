import React from 'react';
import logo from './logo.svg';
import { Meteo } from './features/meteo/Meteo';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <Meteo />
      </header>
    </div>
  );
}

export default App;
