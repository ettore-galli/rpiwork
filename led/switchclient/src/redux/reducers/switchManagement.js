import { INIT_SWITCHES, SET_SWITCH_STATUS, TOGGLE_SWITCH_STATUS } from "../actionTypes";

const initialState = {
    switchStatus: []
};

function initSwitches() {
    return [false, false];
}

function setSwitch(switches, switchId, switchStatus) {
    return switches.map((el, id) => { if (id === switchId) { return switchStatus; } else { return el; } });
}

function toggleSwitch(switches, switchId) {
    return switches.map((el, id) => { if (id === switchId) { return !el; } else { return el; } });
}

export default function (state = initialState, action) {
    switch (action.type) {
        case INIT_SWITCHES: {
            const switchStatus = state.switchStatus.length>0?state.switchStatus:initSwitches();
            return {
                ...state,
                switchStatus
            }
        }
        case SET_SWITCH_STATUS: {
            return {
                ...state,
                switchStatus: setSwitch(state.switchStatus, action.payload.switchId, action.payload.switchStatus)
            }
        }
        case TOGGLE_SWITCH_STATUS: {
            return {
                ...state,
                switchStatus: toggleSwitch(state.switchStatus, action.payload.switchId)
            }
        }
        default: {
            return state;
        }
    }
}

