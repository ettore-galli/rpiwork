'use strict';

class AudioPage {

    constructor(
        playButton,
        volumeController,
        pitchController,
        filterFrequency,
        filterQ
    ) {

        const AudioContext = window.AudioContext || window.webkitAudioContext;

        this.audioContext = new AudioContext();
        // get the audio element
        this.audioElement = document.querySelector('audio');

        // pass it into the audio context
        this.track = this.audioContext.createMediaElementSource(this.audioElement);

        this.oscillator = this.audioContext.createOscillator();
        this.oscillator.type = "square";

        this.filter = this.audioContext.createBiquadFilter();
        this.filter.type = 'lowpass';
        this.filter.frequency.value = 500;
        this.filter.Q.value = 4;


        this.gainNode = this.audioContext.createGain();

        this.track
            .connect(this.gainNode)
            .connect(this.audioContext.destination);

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

        this.play = () => {
            this.resumeIfSuspended();
            this.audioElement.play();
        }

        this.pause = () => {
            this.resumeIfSuspended();
            this.audioElement.pause();
        }

        this.setVolume = (value) => {
            this.gainNode.gain.value = value;
        }

        this.setFilterFrequency = (value) => {
            this.filter.frequency.value = value;
        }

        this.setFilterQ = (value) => {
            this.filter.Q.value = value;
        }

        playButton.addEventListener('click', function () {

            // play or pause track depending on state
            if (this.dataset.playing === 'false') {
                thisClassContext.play();
                this.dataset.playing = 'true';
            } else if (this.dataset.playing === 'true') {
                thisClassContext.pause();
                this.dataset.playing = 'false';
            }

        }
            , false);

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
            // check if context is in suspended state (autoplay policy)
            if (thisClassContext.audioContext.state === 'suspended') {
                thisClassContext.audioContext.resume();
            }
            thisClassContext.oscillator.frequency.value = this.value;
        }
        );

        this.audioElement.addEventListener('ended', () => {
            playButton.dataset.playing = 'false';
        }, false);

        console.log("AudioPage init completed.")
    }

}

const buildAudioPage = (
    playButton,
    volumeController,
    pitchController,
    filterFrequency,
    filterQ
) => {
    return new AudioPage(
        playButton,
        volumeController,
        pitchController,
        filterFrequency,
        filterQ
    );
}