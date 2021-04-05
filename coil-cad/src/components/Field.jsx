import '../App.css';
import React from 'react';


class Field extends React.Component {

    render() {
        return (
            <div className="App-field" >
                <div className="App-field-label">
                    <label>{this.props.label}</label>
                </div>
                <div className="App-field-input">
                    <input
                        type="text"
                        onChange={this.props.onChange}
                        value={this.props.value}
                    />
                </div>
            </div>
        );
    }
}

export default Field;