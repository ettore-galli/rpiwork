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
                console.log("Executing then after fetch GET")
                console.log(data)
                dispatch({
                    type: INIT_SWITCHES,
                    payload: data
                })
            }
            );
    }
);

export const toggleSwitch = (switchId, switches) => (
    dispatch => {

        const toggle_request_body = {
            pattern: {
                ...switches,
                [switchId]: !switches[switchId]
            }
        };
        const toggle_request = JSON.stringify(toggle_request_body);
        console.log(toggle_request)
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
                    console.log("Executing then after fetch POST")
                    console.log(data)
                    dispatch({
                        type: SET_SWITCH_STATUS,
                        payload: data
                    })
                }
            )
    }
);