import { INIT_SWITCHES, SET_SWITCH_STATUS, TOGGLE_SWITCH_STATUS } from "./actionTypes";

export const initSwitches = () => (
    dispatch => {
        dispatch({
            type: INIT_SWITCHES,
            payload: {}
        })
    }
);

export const setSwitch = (switchId, switchStatus) => (
    dispatch => {
        dispatch({
            type: SET_SWITCH_STATUS,
            payload: { switchId, switchStatus }
        })
    }
);

export const toggleSwitch = (switchId) => (
    dispatch => {
        dispatch({
            type: TOGGLE_SWITCH_STATUS,
            payload: { switchId }
        })
    }
);