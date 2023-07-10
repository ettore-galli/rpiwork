from machine import Pin, SPI, PWM
import framebuf


class LCDWiring:
    """
    SYMBOL  | DESCRIPTION
    --------+---------------------------------------------------------
    VCC     | Power (3.3V/5V input)
    GND     | Ground
    DIN     | SPI data input ("mosi")
    CLK     | SPI clock input
    CS      | Chip selection, low active
    DC      | Data/Command selection (high for data, low for command)
    RST     | Reset, low active
    BL      | Backlight

    """

    def __init__(self, spi, cs, sck, mosi, miso, rst, dc, bl):
        self.spi = spi

        self.cs = cs
        # SCK / SCL
        self.sck = sck
        # SDA
        self.mosi = mosi
        # -
        self.miso = miso
        # RES
        self.rst = rst
        # DC
        self.dc = dc
        # BL
        self.bl = bl


# SPI0_WIRING = LCDWiring(cs=1, sck=2, mosi=3, miso=None, rst=7, dc=0, bl=5)
SPI0_WIRING = LCDWiring(spi=1, cs=9, sck=10, mosi=11, miso=None, rst=12, dc=8, bl=13)


class MosaicTile:
    def __init__(self, pos_x: int, pos_y: int, size_x: int, size_y: int, color: int):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.color = color


class LCD_1inch8(framebuf.FrameBuffer):
    def __init__(self, wiring: LCDWiring):
        self.width = 160
        self.height = 128

        self.cs = Pin(wiring.cs, Pin.OUT)
        self.rst = Pin(wiring.rst, Pin.OUT)

        self.cs(1)
        self.spi = SPI(1)
        self.spi = SPI(1, 1000_000)
        self.spi = SPI(
            wiring.spi,
            10000_000,
            polarity=0,
            phase=0,
            sck=Pin(wiring.sck),
            mosi=Pin(wiring.mosi),
            miso=wiring.miso,
        )
        self.dc = Pin(wiring.dc, Pin.OUT)
        self.dc(1)
        self.buffer = bytearray(self.height * self.width * 2)
        super().__init__(self.buffer, self.width, self.height, framebuf.RGB565)
        self.init_display()

        self.WHITE = 0xFFFF
        self.BLACK = 0x0000
        self.GREEN = 0x001F
        self.BLUE = 0xF800
        self.RED = 0x07E0

        self.start_backlight(wiring=wiring, brightness=32767)

    def rgb565(self, red, green, blue):
        # Reverse engineered is de facto binary bbbbbrrrrrrggggg "brg565"
        return ((blue >> 3) << 11) + ((red >> 2) << 5) + (green >> 3)

    def start_backlight(self, wiring, brightness=32767, frequency=1000):
        pwm = PWM(Pin(wiring.bl))
        pwm.freq(frequency)
        pwm.duty_u16(brightness)  # max 65535

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
            dw = aSize
        else:
            wh = aSize
            dw = aSize[0]

        px, py = aPos

        width = wh[0] * aFont["Width"] + max(1, int(dw))

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

    def pick_char_data(self, aFont, aChar):
        """Pick relevant data for drawing a single character from font map"""
        startchar = aFont["Start"]

        fontw = aFont["Width"]
        fonth = aFont["Height"]

        ch = ord(aChar) if isinstance(aChar, str) else aChar

        ci = (ch - startchar) * fontw

        font_data = aFont["Data"]

        charA = font_data[ci : ci + fontw]

        return fontw, fonth, charA

    def render_rectangle_mosaic(self, mosaic: List[MosaicTile]):
        """Actually render a mosaic made of rectangles"""
        for tile in mosaic:
            self.fill_rect(tile.pos_x, tile.pos_y, tile.size_x, tile.size_y, tile.color)

    def prepare_char_draw_mosaic_data(self, aPos, fonth, charA, aSizes, aColor):
        """Prepare drawing data for a single character, rendered as a mosaic of rectangles"""

        mosaic: List[MosaicTile] = []

        px = aPos[0]

        for c in charA:
            py = aPos[1]

            for _ in range(fonth):
                if c & 0x01:
                    mosaic.append(MosaicTile(px, py, aSizes[0], aSizes[1], aColor))
                py += aSizes[1]
                c >>= 1
            px += aSizes[0]

        return mosaic

    def char(self, aPos, aChar, aColor, aFont, aSizes):
        """Draw a character at the given position using the given font and color.
        aSizes is a tuple with x, y as integer scales indicating the
        # of pixels to draw for each pixel in the character."""

        _, fonth, charA = self.pick_char_data(aFont, aChar)
        mosaic = self.prepare_char_draw_mosaic_data(aPos, fonth, charA, aSizes, aColor)
        self.render_rectangle_mosaic(mosaic)