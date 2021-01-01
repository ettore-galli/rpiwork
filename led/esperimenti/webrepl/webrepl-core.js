class Webrepl {

    constructor(
        initStateAction,
        getInputFromUserAction,
        processInputFunction,
        calculateStateFromLastResultFunction,
        updateInterfaceFromStateAction,
        enterTriggerId
    ) {

        this.applicationState = initStateAction();

        const getApplicationState = () => {
            return { ...this.applicationState };
        }

        const setApplicationState = (state) => {
            this.applicationState = { ...state };
        }

        const processInputAction = (inputReader, interfaceWriter) => {
            const user_input = inputReader();
            const lastResult = processInputFunction(user_input, getApplicationState());
            setApplicationState(
                calculateStateFromLastResultFunction(getApplicationState(), lastResult)
            )
            interfaceWriter(getApplicationState())
        }

        document.getElementById(enterTriggerId).onclick = () => {
            processInputAction(getInputFromUserAction, updateInterfaceFromStateAction)
        }

        console.log("webrepl init completed.")
    }

}