import { SET_SWITCH_STATUS, TOGGLE_SWITCH_STATUS } from "./actionTypes";

export const setSwitch = (switchId, switchStatus) => ({
    type: SET_SWITCH_STATUS,
    payload: { switchId, switchStatus }
});

export const toggleSwitch = (switchId) => ({
    type: TOGGLE_SWITCH_STATUS,
    payload: { switchId }
});