# TINYGO

## Setup tinygo

<https://tinygo.org/getting-started/install/macos/>

Downloaded directly (no homebrew)
<https://github.com/tinygo-org/tinygo/releases/download/v0.29.0/tinygo0.29.0.darwin-amd64.tar.gz>

Tinygo placed under home directory

```bash
~/tinygo
```

Added configuration to ```~/.zshrc```

```shell
#
# Tiny Go Setup
#
TINYGO_PATH=~/tinygo/bin
export PATH=$TINYGO_PATH:$PATH
```

```shell
tinygo target
```

## Video tutorial

<https://youtu.be/B-6GsoEg0Lw?si=KrkhNcieKCxIBY-w>

## Examples

ADC
<https://github.com/soypat/tinygo-arduino-examples/blob/main/lcdscreen_adc/sense.go>

Display
<https://github.com/va1da5/tinygo-pico-ssd1306/blob/main/README.md>

Display Driver
<https://github.com/tinygo-org/drivers/blob/release/ssd1306/ssd1306.go>

```bash
go get tinygo.org/x/drivers    
```

## Flash

```bash
CMD + Shift + P --> Tiny GoTarget --> pico
```
