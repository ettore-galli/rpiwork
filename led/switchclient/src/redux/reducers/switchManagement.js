import { SET_SWITCH_STATUS, TOGGLE_SWITCH_STATUS } from "../actionTypes";

const initialState = {
    switchStatus: []
};


function setSwitch(switches, switchId, switchStatus) {
    return switches.map((el, id) => { if (id === switchId) { return switchStatus; } else { return el; } });
}

function toggleSwitch(switches, switchId) {
    return switches.map((el, id) => { if (id === switchId) { return !el; } else { return el; } });
}

export default function (state = initialState, action) {
    console.log("switch management", action);
    switch (action.type) {
        case SET_SWITCH_STATUS: {
            console.log(SET_SWITCH_STATUS);
            return {
                ...state,
                switchStatus: setSwitch(state.switchStatus, action.payload.switchId, action.payload.switchStatus)
            }
        }
        case TOGGLE_SWITCH_STATUS: {
            console.log(TOGGLE_SWITCH_STATUS);
            return {
                ...state,
                switchStatus: toggleSwitch(state.switchStatus, action.payload.switchIdß)
            }
        }
        default: {
            return state;
        }
    }
}

