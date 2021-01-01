





const buildWebRepl = (
    inputElementId,
    enterTriggerId,
    resultAreaId
) => {

    const initStateAction = () => {
        return { stack: [] };
    }

    const getInputFromUserAction = () => {
        return document.getElementById(inputElementId).value;
    }

    const calculateStateFromLastResultFunction = (state, lastResult) => {
        return {
            ...state,
            stack: state.stack.concat([lastResult])
        };
    }

    const updateInterfaceFromStateAction = (state) => {
        document.getElementById(resultAreaId).innerText = state.stack;
    }

    const processInputFunction = (input, state) => {
        return input;
    }


    return new Webrepl(
        initStateAction,
        getInputFromUserAction,
        processInputFunction,
        calculateStateFromLastResultFunction,
        updateInterfaceFromStateAction,
        enterTriggerId
    )
}