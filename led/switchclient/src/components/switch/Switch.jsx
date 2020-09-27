import React from 'react';
import { connect } from "react-redux";
import { setSwitch, toggleSwitch } from "../../redux/actions";

class Switch extends React.Component {

    render() {
        return (
            <div className="Led">
                <label>{this.props.switches[this.props.switchId]}</label>
                <input
                    type="checkbox"
                    checked={this.props.switches[this.props.switchId]}
                    onChange={() => {this.props.toggleSwitch(this.props.switchId);}}
                />
            </div>
        );
    }
}

const mapStateToProps = (state, ownProps) => {
    return { ...ownProps, switches: state.switchManagement.switchStatus };
}



export default connect(
    mapStateToProps,
    { setSwitch, toggleSwitch }
)(Switch);