import React from 'react';
import { connect } from "react-redux";
import { setSwitch, toggleSwitch } from "../../redux/actions";

class Switch extends React.Component {

    toggleSwitchStatus(event) {
        console.log(event);
        this.toggleSwitch(this.props.switchId); // TODO: Actual switch id
    }

    render() {
        return (
            <div className="Led">
                <label>{this.props.label}</label>
                <input
                    type="checkbox"
                    checked={this.props.switches[this.props.switchId]} //TODO: Actual id
                    onChange={this.changeSwitchStatus}
                />
            </div>
        );
    }
}

const mapStateToProps = (state, ownProps) => {
    console.log("mapStateToProps", { switches: state.switchManagement.switchStatus });
    return { ...ownProps, switches: state.switchManagement.switchStatus };
}



export default connect(
    mapStateToProps,
    { setSwitch, toggleSwitch }
)(Switch);