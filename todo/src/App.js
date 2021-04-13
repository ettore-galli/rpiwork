import React from 'react';
import { Todo } from './features/todo/Todo';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Todo />
      </header>
    </div>
  );
}

export default App;
