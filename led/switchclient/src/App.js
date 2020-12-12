import React from 'react';
import './App.css';
import Switch from './components/switch/Switch';
import { initSwitches } from "./redux/actions";
import { connect } from "react-redux";

function App(props) {
  props.initSwitches();
  const switches = Object.keys(props.switches).map(
    switchId => {
      return <Switch
        key={switchId}
        label={switchId}
        switchId={switchId}
        >
      </Switch>
    }
  );
  return (
    <div className="App">
      <header className="App-header">
        {switches}
      </header>
    </div>
  );
}

const mapStateToProps = (state, ownProps) => {
  return { ...ownProps, switches: state.switchManagement.switchStatus };
}

export default connect(
  mapStateToProps,
  { initSwitches }
)(App);
