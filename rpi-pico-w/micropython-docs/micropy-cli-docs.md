# Micropy-cli

## Micropython: micropy-cli docs

### Official Micropython Documentation

<https://micropy-cli.readthedocs.io/en/latest/>

### Other useful docs

<https://www.agilepartner.net/en/micropython-esp8266-and-vscode/>
<https://medium.com/all-geek-to-me/developing-for-the-raspberry-pi-pico-in-vs-code-getting-started-6dbb3da5ba97>

### Steps - setup

pip install --upgrade micropy-cli

### Steps - setup stubs

```shell
# Ricerca e aggiunta stub esistenti
micropy stubs search pico # --> e.g. micropython-rp2-pico_w-stubs
micropy stubs add micropython-rp2-pico_w-stubs
```

```shell
# Generazione automatica.
# Attenzione: NON FUNZIONA
micropy stubs create /dev/cu.usbmodem1101 # Solo prima volta che si usa un dispositivo
micropy stubs create $(ls -d -1 /dev/*  | grep cu.usb)
```

### Steps - dev

<https://micropy-cli.readthedocs.io/en/latest/base.html#creating-a-project>

micropy init micropy-1
