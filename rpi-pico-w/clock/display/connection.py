from display.pico_lcd_18 import LCD_1inch8, SPI0_WIRING


def instantiate_display():
    wiring = SPI0_WIRING
    LCD = LCD_1inch8(wiring)

    return LCD
