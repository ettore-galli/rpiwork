package main

import (
	"blinky/imgbuffer"
	"machine"
	"sync"
	"time"

	"tinygo.org/x/drivers/ssd1306"
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
		_ = val
		//println((val))
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

	machine.I2C1.Configure(machine.I2CConfig{Frequency: 400 * machine.KHz})
	display := ssd1306.NewI2C(machine.I2C1)
	display.Configure(ssd1306.Config{Width: 128, Height: 64, Address: ssd1306.Address_128_32, VccState: ssd1306.SWITCHCAPVCC})

	display.ClearBuffer()
	display.ClearDisplay()

	// err := display.SetBuffer(FotoEttore)
	imgBuffer := imgbuffer.ToSSD1306ImageBuffer(BlockBuffer)
	println(imgBuffer)
	err := display.SetBuffer(BlockBuffer)
	if err != nil {
		println(err)
	}

	display.Display()

	go AdcLoop(sensor, samplingDelayMs)
	go LedLoop(led, delayMs)

	mainWg.Wait()

}
