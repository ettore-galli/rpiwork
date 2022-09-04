from display.pico_lcd_18 import LCD_1inch8, SPI0_WIRING


def instantiate_display():
    wiring = SPI0_WIRING
    LCD = LCD_1inch8(wiring)
    
    return LCD

def test_display():
    print("Testing display...")
    lcd = instantiate_display()
    lcd.fill(lcd.BLACK)
    lcd.text("Testing display...", 10, 10, lcd.WHITE)
    lcd.show()
    
if __name__ == '__main__':
    test_display()
    
    
    