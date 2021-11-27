'use strict';

(() => {

    let __state = { feedback: false };

    function setState(state) {
        __state = {...__state, ... { state } };
    }

    function getState() {
        return __state;
    }

    function setUI(state) {
        feedback(getState().feedback);
    }

    function feedback(state) {
        document.getElementById('feedback').classList.remove("feedbackOn", "feedbackOff");
        document.getElementById('feedback').classList.add(!!state ? "feedbackOn" : "feedbackOff");
    }

    document.addEventListener('keydown', logKey.bind(this, "dw"));
    document.addEventListener('keyup', logKey.bind(this, "up"));

    function setState(state) {
        __state = {...__state, ...state };
    }

    function logKey(type, e) {
        const message = `${type}-${e.code}`
        setState({ feedback: type === 'dw' })
    }

    setInterval(setUI, 10);

})();