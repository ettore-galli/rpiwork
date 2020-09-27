import { INIT_SWITCHES, SET_SWITCH_STATUS, TOGGLE_SWITCH_STATUS } from "./actionTypes";

const getArrayIdFromSwitchId = switchId => {
    return parseInt(switchId);
}

export const initSwitches = () => ({
    type: INIT_SWITCHES,
    payload: {}
});

export const setSwitch = (switchId, switchStatus) => ({
    type: SET_SWITCH_STATUS,
    payload: { switchId: getArrayIdFromSwitchId(switchId), switchStatus }
});

export const toggleSwitch = (switchId) => ({
    type: TOGGLE_SWITCH_STATUS,
    payload: { switchId: getArrayIdFromSwitchId(switchId) }
});