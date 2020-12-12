import { INIT_SWITCHES, SET_SWITCH_STATUS, TOGGLE_SWITCH_STATUS } from "./actionTypes";
import { SWITCH_SERVER_PATTERN_URL } from "../config/endpoint";

export const initSwitches = () => (
    dispatch => {
        fetch(SWITCH_SERVER_PATTERN_URL, { mode: 'cors' })
            .then(response => response.json())
            .then(data => {
                console.log("then did run")
                console.log(data)
                dispatch({
                    type: INIT_SWITCHES,
                    payload: data
                })
            }
            );
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