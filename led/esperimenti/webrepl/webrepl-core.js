class Webrepl {

    constructor(
        initStateAction,
        linkMainWorkflowToTriggerAction,
        getInputFromUserAction,
        processInputFunction,
        calculateStateFromLastResultFunction,
        updateInterfaceFromStateAction
    ) {

        this.applicationState = initStateAction();

        const getApplicationState = () => {
            return { ...this.applicationState };
        }

        const setApplicationState = (state) => {
            this.applicationState = { ...state };
        }

        const mainProcessInputWorkflowAction = (inputReader, interfaceWriter) => {
            const user_input = inputReader();
            const lastResult = processInputFunction(user_input, getApplicationState());
            setApplicationState(
                calculateStateFromLastResultFunction(getApplicationState(), lastResult)
            )
            interfaceWriter(getApplicationState())
        }

        linkMainWorkflowToTriggerAction(
            () => {
                mainProcessInputWorkflowAction(getInputFromUserAction, updateInterfaceFromStateAction)
            }
        )

        console.log("webrepl init completed.")
    }

}