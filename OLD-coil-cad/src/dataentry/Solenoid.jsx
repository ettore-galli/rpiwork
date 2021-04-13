import '../App.css';
import React from 'react';
import Button from '../components/Button';
import Field from '../components/Field'
import inductance from '../calc/Solenoid';

class Solenoid extends React.Component {

  constructor(props) {
    super(props);
    // this.handleChange = this.handleChange.bind(this);
    this.state = {
      spire: 100,
      diametro: 5.0,
      lunghezza: 30.0,
      permeabilita: 1.0,
      induttanza: 0
    }
    this.performCalculus = this.performCalculus.bind(this);
  }

  performCalculus() {
    const induttanza = inductance(
      parseFloat(this.state.permeabilita),
      parseFloat(this.state.lunghezza) / 1000.0,
      parseFloat(this.state.diametro) / 1000.0,
      parseFloat(this.state.spire)
    )
    console.log(
      this.state.permeabilita,
      this.state.lunghezza,
      this.state.diametro,
      this.state.spire
    )
    this.setState({
      induttanza: induttanza
    })
    console.log(this.state)
  }

  render() {

    return (
      <div className="App-body">

        <Field label="Permeabilità relativa" value={this.state.permeabilita}
          onChange={e => { this.setState({ permeabilita: e.target.value }) }}
        ></Field>
        <Field label="Diametro (mm)" value={this.state.diametro}
          onChange={e => { this.setState({ diametro: e.target.value }) }}
        ></Field>
        <Field label="Lunghezza (mm)" value={this.state.lunghezza}
          onChange={e => { this.setState({ lunghezza: e.target.value }) }}
        ></Field>
        <Field label="Spire" value={this.state.spire}
          onChange={e => { this.setState({ spire: e.target.value }) }}
        ></Field>

        <Button
          label="Calcola"
          onClick={this.performCalculus}

        ></Button>
        <div className="App-result">{this.state.induttanza}</div>

      </div>
    );
  }
}

export default Solenoid;