'use strict';

class AudioPage {

    constructor(
        volumeController,
        pitchController,
        filterFrequency,
        filterQ
    ) {

        const AudioContext = window.AudioContext || window.webkitAudioContext;

        this.audioContext = new AudioContext();

        this.oscillator = this.audioContext.createOscillator();
        this.oscillator.type = "square";

        this.filter = this.audioContext.createBiquadFilter();
        this.filter.type = 'lowpass';
        this.filter.frequency.value = 500;
        this.filter.Q.value = 4;

        this.gainNode = this.audioContext.createGain();
        this.gainNode.gain.value = 0;

        this.oscillator
            .connect(this.filter)
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

        this.setFilterFrequency = (value) => {
            this.resumeIfSuspended();
            this.filter.frequency.value = value;
        }

        this.setFilterQ = (value) => {
            this.resumeIfSuspended();
            this.filter.Q.value = value;
        }

        volumeController.addEventListener('input', function () {
            thisClassContext.setVolume(this.value);
        }
        );

        filterFrequency.addEventListener('input', function () {
            thisClassContext.setFilterFrequency(this.value);
        }
        );

        filterQ.addEventListener('input', function () {
            thisClassContext.setFilterQ(this.value);
        }
        );

        pitchController.addEventListener('input', function () {
            thisClassContext.setFrequency(this.value);
        }
        );

        console.log("AudioPage init completed.")
    }

}

