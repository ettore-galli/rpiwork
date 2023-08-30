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

## Video tutorial

<https://youtu.be/B-6GsoEg0Lw?si=KrkhNcieKCxIBY-w>

## Flash

```bash
tinygo flash -target=pico main.go
```
