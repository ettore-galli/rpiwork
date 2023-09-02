package main

import (
	"machine"
	"sync"
	"time"
)

func LedLoop(led machine.Pin, delayMs float64) {
	for {
		led.Low()
		time.Sleep(time.Millisecond * time.Duration(delayMs))
		led.High()
		time.Sleep(time.Millisecond * time.Duration(delayMs))
	}
}

func AdcLoop(sensor machine.ADC, samplingDelayMs float64) {
	var val uint16
	for {
		val = sensor.Get()
		println((val))
		time.Sleep(time.Millisecond * time.Duration(samplingDelayMs))
	}
}

func main() {
	var mainWg sync.WaitGroup
	mainWg.Add(1)
	var delayMs float64 = 300
	var samplingDelayMs float64 = 1
	led := machine.Pin(0)
	led.Configure(machine.PinConfig{Mode: machine.PinOutput})

	var sensor = machine.ADC{
		Pin: machine.ADC0,
	}

	machine.InitADC()
	adcCfg := machine.ADCConfig{}
	sensor.Configure(adcCfg)

	go AdcLoop(sensor, samplingDelayMs)
	go LedLoop(led, delayMs)

	mainWg.Wait()

}
