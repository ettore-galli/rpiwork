'use strict';

class WebSynth {

    constructor(
        window,
        volumeController,
        pitchController,
    ) {
        const AudioContext = window.AudioContext || window.webkitAudioContext;

        this.audioContext = new AudioContext();

        this.oscillator = this.audioContext.createOscillator();
        this.oscillator.type = "square";

        this.gainNode = this.audioContext.createGain();
        this.gainNode.gain.value = 0;

        this.oscillator
            .connect(this.gainNode)
            .connect(this.audioContext.destination);
        this.oscillator.start(0);

        const thisClassContext = this;

        this.resumeIfSuspended = () => {
            if (this.audioContext.state === 'suspended') {
                this.audioContext.resume();
            }
        }

        this.setFrequency = (value) => {
            this.resumeIfSuspended();
            this.oscillator.frequency.value = value;
        }

        this.setVolume = (value) => {
            this.resumeIfSuspended();
            this.gainNode.gain.value = value;
        }

        // OPTION A: Event listeners added inside class - BLOCK START

        // volumeController.addEventListener('input', function () {
        //     thisClassContext.setVolume(this.value);
        // }
        // );

        // pitchController.addEventListener('input', function () {
        //     thisClassContext.setFrequency(this.value);
        // }
        // );

        // OPTION A: Event listeners added inside class - BLOCK END

    }

}

