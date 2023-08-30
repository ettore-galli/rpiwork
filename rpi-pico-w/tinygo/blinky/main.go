package main

import (
	"machine"
	"time"
)

func main() {
	var delayMs float64 = 100
	led := machine.LED
	led.Configure(machine.PinConfig{Mode: machine.PinOutput})
	for {
		led.Low()
		time.Sleep(time.Millisecond * time.Duration(delayMs))

		led.High()
		time.Sleep(time.Millisecond * time.Duration(delayMs))
	}
}
