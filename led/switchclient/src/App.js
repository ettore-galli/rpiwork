import React from 'react';
import './App.css';
import Switch from './components/switch/Switch';
import { initSwitches } from "./redux/actions";
import { connect } from "react-redux";

function App(props) {
  props.initSwitches();
   

  return (
    <div className="App">
      <header className="App-header">
        <Switch label="s1" switchId="0"></Switch>
        <Switch label="s1" switchId="1"></Switch>
      </header>
    </div>
  );
}

export default connect(
  null,
  { initSwitches }
)(App);