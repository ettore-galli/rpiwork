package main

import (
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

func AdcLoop(sensor machine.ADC, samplingDelayMs float64, valueCallback func(uint16)) {
	var val uint16
	for {
		val = sensor.Get()
		valueCallback(val)
		time.Sleep(time.Millisecond * time.Duration(samplingDelayMs))
	}
}

func createImageBufferFromValue(value uint16) []byte {
	const BufferLength int = 1024
	buffer := make([]byte, BufferLength)
	for i := 0; i < BufferLength; i++ {
		buffer[i] = byte(value >> 8)
	}
	return buffer
}

func writeBufferOnDisplay(display ssd1306.Device, imgBuffer []byte) {

	err := display.SetBuffer(imgBuffer)
	if err != nil {
		println(err)
	}

	display.Display()
}

func writeValueOnDisplay(display ssd1306.Device, value uint16) {
	imgBuffer := createImageBufferFromValue(value)

	writeBufferOnDisplay(display, imgBuffer)
}

func main() {
	var mainWg sync.WaitGroup
	mainWg.Add(1)

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

	// // err := display.SetBuffer(FotoEttore)
	// imgBuffer := imgbuffer.ToSSD1306ImageBuffer(BlockBuffer)
	// println(imgBuffer)
	// err := display.SetBuffer(BlockBuffer)
	// if err != nil {
	// 	println(err)
	// }

	// display.Display()

	valueCallback := func(value uint16) {
		writeValueOnDisplay(display, value)
	}

	go AdcLoop(sensor, samplingDelayMs, valueCallback)

	// var delayMs float64 = 300
	// go LedLoop(led, delayMs)

	mainWg.Wait()

}
