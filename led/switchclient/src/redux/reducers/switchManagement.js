import { INIT_SWITCHES, SET_SWITCH_STATUS } from "../actionTypes";

const initialState = {
    switchStatus: {}
};

function initSwitches(switches) {
    return switches;
}

function setSwitchStatus(switchStatus) {
    return { ...switchStatus}
}

export default function (state = initialState, action) {
    switch (action.type) {
        case INIT_SWITCHES: {
            const switchStatus = Object.keys(state.switchStatus).length > 0 ? state.switchStatus : initSwitches(action.payload);
            return {
                ...state,
                switchStatus
            }
        }
        case SET_SWITCH_STATUS: {
            console.log("SET_SWITCH_STATUS")
            console.log(state.switchStatus, action.payload, action.payload.switchStatus)
            return {
                ...state,
                switchStatus: setSwitchStatus(action.payload)
            }
        }
        default: {
            return state;
        }
    }
}

