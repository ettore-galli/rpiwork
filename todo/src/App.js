import React from 'react';
import { Todo } from './features/todo/Todo';
import {  useDispatch } from 'react-redux';
import './App.css';

import {
  loadEntries,
} from './features/todo/todoSlice';

function App() {
  const dispatch = useDispatch();

  dispatch(loadEntries([
    {id: 1, text:"Test entry 1"},
    {id: 2, text:"Test entry 1+1"},
    {id: 3, text:"Test entry III"},
    {id: 4, text:"Test entry iv"},
    {id: 5, text:"Test entry 5"}
  ]))

  return (
    <div className="App">
      <header className="App-header">
        <Todo />
      </header>
    </div>
  );
}

export default App;
