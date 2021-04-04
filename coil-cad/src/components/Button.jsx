import React from 'react';


class Button extends React.Component {

    render() {
        return (
            <div>
                <input
                    type="Button"
                    value={this.props.label}
                    onClick={this.props.onClick}
                    onChange={e=>{console.log(e.target.value)}}
                ></input>
            </div>
        );
    }
}

export default Button;