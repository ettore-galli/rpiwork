'use strict'


function getKeyIdFromNumber(keyNumber) {
    return "area" + String(keyNumber);
}

function getKeyFromNumber(keyNumber) {
    return document.getElementById(getKeyIdFromNumber(keyNumber))
}

function buildPadKeyboard(synth, volumeController, numberOfKeys, keyAreaId){
    for (let i = 0; i < numberOfKeys; i++) {

        const keyNumber = i + 1;
        const key = document.getElementById("key-template").content.cloneNode(true).children[0];

        key.id = getKeyIdFromNumber(keyNumber);
        key.style.width = String(95.0 / numberOfKeys) + "%";
        document.getElementById(keyAreaId).appendChild(key);

        
        key.onmouseover = function (e) {
            console.log(keyNumber, volumeController.value)
            synth.playNoteNumber(keyNumber, volumeController.value);
        }

        key.onmousemove = function (e) {
            var rect = e.target.getBoundingClientRect();
            var x = e.clientX - rect.left; // x position within the element.
            var y = e.clientY - rect.top;  // y position within the element.
            synth.setFilterFrequency((y / rect.height) * 3000.0);
        }

        key.onmouseleave = function (e) {
            synth.releaseNote();
        }

    }
}

function initSynth(window, document) {
    const synth = new WebSynth(window);

    const volumeController = document.getElementById('volume');
    const filterFrequency = document.getElementById('filter-frequency');
    const filterQ = document.getElementById('filter-q');

    synth.setVolume(volumeController.value);
    synth.setFilterFrequency(filterFrequency.value);


    volumeController.addEventListener('input', function () {
        synth.setVolume(this.value);
    }
    );

    filterFrequency.addEventListener('input', function () {
        synth.setFilterFrequency(this.value);
    }
    );

    filterQ.addEventListener('input', function () {
        synth.setFilterQ(this.value);
    }
    );

    const numberOfKeys = synth.noteMap.length;

    buildPadKeyboard(synth, volumeController, numberOfKeys, "key-area-up");
    buildPadKeyboard(synth, volumeController, numberOfKeys, "key-area-down");

     
}
