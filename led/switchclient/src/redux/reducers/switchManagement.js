import { INIT_SWITCHES, SET_SWITCH_STATUS, TOGGLE_SWITCH_STATUS } from "../actionTypes";

const initialState = {
    switchStatus: {}
};

function initSwitches() {
    return { s0: false, s1: false };
}

function setSwitch(switches, switchId, switchStatus) {
    return { ...switches, [switchId]: switchStatus }
}

function toggleSwitch(switches, switchId) {
    return { ...switches, [switchId]: !switches[switchId] }
}

export default function (state = initialState, action) {
    switch (action.type) {
        case INIT_SWITCHES: {
            const switchStatus = Object.keys(state.switchStatus).length > 0 ? state.switchStatus : initSwitches();
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

