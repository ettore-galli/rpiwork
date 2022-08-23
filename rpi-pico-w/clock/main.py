from machine import Pin, SPI, PWM
import framebuf
import time

from sysfont import sysfont

BL = 5
DC = 0
RST = 7
MOSI = 3
SCK = 2
CS = 1


class LCD_1inch8(framebuf.FrameBuffer):
    def __init__(self):
        self.width = 160
        self.height = 128

        self.cs = Pin(CS, Pin.OUT)
        self.rst = Pin(RST, Pin.OUT)

        self.cs(1)
        self.spi = SPI(1)
        self.spi = SPI(1, 1000_000)
        self.spi = SPI(
            0, 10000_000, polarity=0, phase=0, sck=Pin(SCK), mosi=Pin(MOSI), miso=None
        )
        self.dc = Pin(DC, Pin.OUT)
        self.dc(1)
        self.buffer = bytearray(self.height * self.width * 2)
        super().__init__(self.buffer, self.width, self.height, framebuf.RGB565)
        self.init_display()

        self.WHITE = 0xFFFF
        self.BLACK = 0x0000
        self.GREEN = 0x001F
        self.BLUE = 0xF800
        self.RED = 0x07E0

    def write_cmd(self, cmd):
        self.cs(1)
        self.dc(0)
        self.cs(0)
        self.spi.write(bytearray([cmd]))
        self.cs(1)

    def write_data(self, buf):
        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(bytearray([buf]))
        self.cs(1)

    def init_display(self):
        """Initialize dispaly"""
        self.rst(1)
        self.rst(0)
        self.rst(1)

        self.write_cmd(0x36)
        self.write_data(0x70)

        self.write_cmd(0x3A)
        self.write_data(0x05)

        # ST7735R Frame Rate
        self.write_cmd(0xB1)
        self.write_data(0x01)
        self.write_data(0x2C)
        self.write_data(0x2D)

        self.write_cmd(0xB2)
        self.write_data(0x01)
        self.write_data(0x2C)
        self.write_data(0x2D)

        self.write_cmd(0xB3)
        self.write_data(0x01)
        self.write_data(0x2C)
        self.write_data(0x2D)
        self.write_data(0x01)
        self.write_data(0x2C)
        self.write_data(0x2D)

        self.write_cmd(0xB4)
        # Column inversion
        self.write_data(0x07)

        # ST7735R Power Sequence
        self.write_cmd(0xC0)
        self.write_data(0xA2)
        self.write_data(0x02)
        self.write_data(0x84)
        self.write_cmd(0xC1)
        self.write_data(0xC5)

        self.write_cmd(0xC2)
        self.write_data(0x0A)
        self.write_data(0x00)

        self.write_cmd(0xC3)
        self.write_data(0x8A)
        self.write_data(0x2A)
        self.write_cmd(0xC4)
        self.write_data(0x8A)
        self.write_data(0xEE)

        self.write_cmd(0xC5)
        # VCOM
        self.write_data(0x0E)

        # ST7735R Gamma Sequence
        self.write_cmd(0xE0)
        self.write_data(0x0F)
        self.write_data(0x1A)
        self.write_data(0x0F)
        self.write_data(0x18)
        self.write_data(0x2F)
        self.write_data(0x28)
        self.write_data(0x20)
        self.write_data(0x22)
        self.write_data(0x1F)
        self.write_data(0x1B)
        self.write_data(0x23)
        self.write_data(0x37)
        self.write_data(0x00)
        self.write_data(0x07)
        self.write_data(0x02)
        self.write_data(0x10)

        self.write_cmd(0xE1)
        self.write_data(0x0F)
        self.write_data(0x1B)
        self.write_data(0x0F)
        self.write_data(0x17)
        self.write_data(0x33)
        self.write_data(0x2C)
        self.write_data(0x29)
        self.write_data(0x2E)
        self.write_data(0x30)
        self.write_data(0x30)
        self.write_data(0x39)
        self.write_data(0x3F)
        self.write_data(0x00)
        self.write_data(0x07)
        self.write_data(0x03)
        self.write_data(0x10)

        self.write_cmd(0xF0)
        # Enable test command
        self.write_data(0x01)

        self.write_cmd(0xF6)
        # Disable ram power save mode
        self.write_data(0x00)

        # sleep out
        self.write_cmd(0x11)
        # DEV_Delay_ms(120);

        # Turn on the LCD display
        self.write_cmd(0x29)

    def show(self):
        self.write_cmd(0x2A)
        self.write_data(0x00)
        self.write_data(0x01)
        self.write_data(0x00)
        self.write_data(0xA0)

        self.write_cmd(0x2B)
        self.write_data(0x00)
        self.write_data(0x02)
        self.write_data(0x00)
        self.write_data(0x81)

        self.write_cmd(0x2C)

        self.cs(1)
        self.dc(1)
        self.cs(0)
        self.spi.write(self.buffer)
        self.cs(1)

    def draw_text(self, aPos, aString, aColor, aFont, aSize=1, nowrap=False):
        """Draw a text at the given position.  If the string reaches the end of the
        display it is wrapped to aPos[0] on the next line.  aSize may be an integer
        which will size the font uniformly on w,h or a or any type that may be
        indexed with [0] or [1]."""

        if aFont == None:
            return

        # Make a size either from single value or 2 elements.
        if (type(aSize) == int) or (type(aSize) == float):
            wh = (aSize, aSize)
        else:
            wh = aSize

        px, py = aPos

        width = wh[0] * aFont["Width"] + 1
        for c in aString:
            self.char((px, py), c, aColor, aFont, wh)
            px += width
            # We check > rather than >= to let the right (blank) edge of the
            # character print off the right of the screen.
            if px + width > self.width:
                if nowrap:
                    break
                else:
                    py += aFont["Height"] * wh[1] + 1
                    px = aPos[0]

    def char(self, aPos, aChar, aColor, aFont, aSizes):
        """Draw a character at the given position using the given font and color.
        aSizes is a tuple with x, y as integer scales indicating the
        # of pixels to draw for each pixel in the character."""

        if aFont == None:
            return

        startchar = aFont["Start"]
        endchar = aFont["End"]

        ci = ord(aChar)

        if startchar <= ci <= endchar:
            fontw = aFont["Width"]
            fonth = aFont["Height"]
            ci = (ci - startchar) * fontw

            charA = aFont["Data"][ci : ci + fontw]

            px = aPos[0]

            for c in charA:
                py = aPos[1]
                for r in range(fonth):
                    if c & 0x01:
                        self.fill_rect(px, py, aSizes[0], aSizes[1], aColor)
                    py += aSizes[1]
                    c >>= 1
                px += aSizes[0]


def get_time_hms():
    return time.gmtime()[3:6]


def fmt_time_hms(time_hms):
    return str("%.2d:%.2d:%.2d" % time_hms)


def fmt_time_hm(time_hms):
    return str("%.2d:%.2d" % time_hms[:2])


def display_time(lcd, dsp_time):
    lcd.fill(LCD.BLACK)
    # lcd.text(dsp_time, 10, 10, lcd.WHITE)
    aSize = 4
    height = 128
    pos_h = (height - 8 * aSize) // 2
    lcd.draw_text((10, pos_h), dsp_time, lcd.WHITE, sysfont, aSize=aSize)
    lcd.show()


def render_time(lcd, curtime):
    dsp_time = fmt_time_hm(curtime)
    display_time(lcd=lcd, dsp_time=dsp_time)


def clock(lcd):

    curtime = ()

    while True:

        now = get_time_hms()

        if now != curtime:
            curtime = now
            render_time(lcd=lcd, curtime=curtime)

        time.sleep_ms(10)


if __name__ == "__main__":
    pwm = PWM(Pin(BL))
    pwm.freq(1000)
    pwm.duty_u16(32768)  # max 65535

    LCD = LCD_1inch8()

    LCD.fill(LCD.WHITE)
    # time.sleep(1)

    clock(lcd=LCD)
    # color BRG

    LCD.fill(LCD.WHITE)

    LCD.show()

    LCD.fill_rect(0, 0, 160, 20, LCD.RED)
    LCD.rect(0, 0, 160, 20, LCD.RED)
    LCD.text("Raspberry Pi Pico", 2, 8, LCD.WHITE)

    LCD.fill_rect(0, 20, 160, 20, LCD.BLUE)
    LCD.rect(0, 20, 160, 20, LCD.BLUE)
    LCD.text("PicoGo", 2, 28, LCD.WHITE)

    LCD.fill_rect(0, 40, 160, 20, LCD.GREEN)
    LCD.rect(0, 40, 160, 20, LCD.GREEN)
    LCD.text("Pico-LCD-1.8", 2, 48, LCD.WHITE)

    LCD.fill_rect(0, 60, 160, 10, 0x07FF)
    LCD.rect(0, 60, 160, 10, 0x07FF)
    LCD.fill_rect(0, 70, 160, 10, 0xF81F)
    LCD.rect(0, 70, 160, 10, 0xF81F)
    LCD.fill_rect(0, 80, 160, 10, 0x7FFF)
    LCD.rect(0, 80, 160, 10, 0x7FFF)
    LCD.fill_rect(0, 90, 160, 10, 0xFFE0)
    LCD.rect(0, 90, 160, 10, 0xFFE0)
    LCD.fill_rect(0, 100, 160, 10, 0xBC40)
    LCD.rect(0, 100, 160, 10, 0xBC40)
    LCD.fill_rect(0, 110, 160, 10, 0xFC07)
    LCD.rect(0, 110, 160, 10, 0xFC07)
    LCD.fill_rect(0, 120, 160, 10, 0x8430)
    LCD.rect(0, 120, 160, 10, 0x8430)

    LCD.show()
    time.sleep(1)
    LCD.fill(0xFFFF)
