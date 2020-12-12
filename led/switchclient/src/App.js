import React from 'react';
import './App.css';
import Switch from './components/switch/Switch';
import { initSwitches } from "./redux/actions";
import { connect } from "react-redux";

function getSortedSwitchKeys(keys) {
  return keys.sort(
    (a, b) => parseInt(a.replace("s", "")) - parseInt(b.replace("s", ""))
  );
}

function App(props) {

  props.initSwitches();

  const switchesKeysInProperOrder = getSortedSwitchKeys(Object.keys(props.switches));

  const switches = switchesKeysInProperOrder.map(
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
