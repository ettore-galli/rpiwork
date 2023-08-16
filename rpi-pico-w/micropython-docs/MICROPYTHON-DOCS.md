# MICROPYTHON

## General Micropython Docs

### Prompt

<https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html>

```shell
screen  $(ls -d -1 /dev/*  | grep cu.usb)
```

### Mpremote

<https://docs.micropython.org/en/latest/reference/mpremote.html>

```shell
mpremote

mpremote reset 

mpremote soft-reset

mpremote run [path/to/local]/main.py # Esegue su dispositivo 

```

## General Project Setup Workflow

### 1. Create virtualenv

```shell
python3.11 -m venv myvirtualenv
source myvirtualenv/bin/activate
```

### 2. Install micropython-cli

```shell
pip install --upgrade micropy-cli
```

### 3. Search for available stubs, then install.

```shell
micropy stubs search
```