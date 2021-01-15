'use strict'

function initSynth(){
    const webrepl = new AudioPage(
        document.getElementById('volume'),
        document.getElementById('pitch'),
        document.getElementById('filter-frequency'),
        document.getElementById('filter-q')
    );
    
    // const volumeController = document.getElementById('volume');
    // const filterFrequency = document.getElementById('pitch');
    // const filterQ = document.getElementById('filter-frequency');
    // const pitchController = document.getElementById('filter-q');
    
    // volumeController.addEventListener('input', function () {
    //     webrepl.setVolume(this.value);
    // }
    // );
    
    // filterFrequency.addEventListener('input', function () {
    //     webrepl.setFilterFrequency(this.value);
    // }
    // );
    
    // filterQ.addEventListener('input', function () {
    //     webrepl.setFilterQ(this.value);
    // }
    // );
    
    // pitchController.addEventListener('input', function () {
    //     webrepl.setFrequency(this.value);
    // }
    // );
}
