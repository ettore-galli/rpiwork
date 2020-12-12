import { INIT_SWITCHES, SET_SWITCH_STATUS } from "./actionTypes";
import { SWITCH_SERVER_PATTERN_URL } from "../config/endpoint";


export const initSwitches = () => (
    dispatch => {
        fetch(
            SWITCH_SERVER_PATTERN_URL,
            {
                mode: 'cors',
                credentials: 'same-origin'
            }
        )
            .then(response => response.json())
            .then(data => {
                dispatch({
                    type: INIT_SWITCHES,
                    payload: data
                })
            }
            );
    }
);

export const setSwitchStatus = (switchId, statusValue, switches) => (
    dispatch => {

        const toggle_request_body = {
            pattern: {
                ...switches,
                [switchId]: statusValue
            }
        };

        const toggle_request = JSON.stringify(toggle_request_body);
        
        fetch(
            SWITCH_SERVER_PATTERN_URL,
            {
                method: 'POST',
                mode: 'cors',
                credentials: 'same-origin',
                headers: new Headers({
                    'Content-Type': 'application/json'
                }),
                body: toggle_request
            }
        )
            .then(response => response.json())
            .then(
                data => {
                    dispatch({
                        type: SET_SWITCH_STATUS,
                        payload: data
                    })
                }
            )
    }
);


 