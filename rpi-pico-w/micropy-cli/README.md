# MICROPY-CLI

## Docs

<https://micropy-cli.readthedocs.io/en/latest/>
<https://www.agilepartner.net/en/micropython-esp8266-and-vscode/>

## Steps - setup

pip install --upgrade micropy-cli
pip install micropy-cli[create_stubs]

## Steps - dev

micropy stubs create /dev/cu.usbmodem1101 # Solo prima volta che si usa un dispositivo
micropy init micropy-1
