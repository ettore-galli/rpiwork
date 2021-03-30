'use strict'

function initSynth(window, document){
    const synth = new WebSynth(
        window,
        document.getElementById('volume'),
        document.getElementById('pitch')
    );

    // OPTION B: Event listeners outside class - BLOCK START
    const volumeController = document.getElementById('volume');
    const pitchController = document.getElementById('pitch');
    
    volumeController.addEventListener('input', function () {
        synth.setVolume(this.value);
    }
    );
    
    pitchController.addEventListener('input', function () {
        synth.setFrequency(this.value);
    }
    );
    // OPTION B: Event listeners outside class - BLOCK END
}
