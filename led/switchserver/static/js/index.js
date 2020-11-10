"use strict"

const page = function (w, r){
    // Global references
    const SWITCH_IDS=["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10"];

    w.getSwitchSetting = function (switchId){
        return document.getElementById(switchId).checked;
    }

        
    w.getSwitchConfiguration = function (){
        let switchConfiguration = {};
        for (const s of SWITCH_IDS){
            switchConfiguration[s] = w.getSwitchSetting(s);
            }
        return switchConfiguration; 
    }


    w.prepareSetSwitchPatternRequestBody = function(){
        return {"pattern" : w.getSwitchConfiguration()};
    }


    w.setSwitchPattern = function(){
        return r.performSetSwitchPatternRequest(
            w.prepareSetSwitchPatternRequestBody()
        );
    }
    
}

page(window, window);
