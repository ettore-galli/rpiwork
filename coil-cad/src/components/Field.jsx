import React from 'react';


class Field extends React.Component {

    render() {
        return (
            <div>
                <label>{this.props.label}</label>
                <input
                    type="text"
                    onChange={this.props.onChange}
                    value={this.props.value}
                />
            </div>
        );
    }
}

export default Field;