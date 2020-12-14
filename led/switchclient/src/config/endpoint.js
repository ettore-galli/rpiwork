const REACT_APP_SWITCH_SERVER_ENDPOINT_PORT=8080;

export const getSwitchPatternURL = () => {
    return window.location.protocol + "//" + window.location.hostname + ":" + REACT_APP_SWITCH_SERVER_ENDPOINT_PORT + "/pattern/";
}