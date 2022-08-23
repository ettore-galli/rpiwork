from sysfont import sysfont


def pick_char_data(font_map, input_char):
    startchar = font_map["Start"]

    fontw = font_map["Width"]
    fonth = font_map["Height"]
    ch = ord(input_char) if isinstance(input_char, str) else input_char

    ci = (ch - startchar) * fontw

    font_data = font_map["Data"]
    char_data = font_data[ci : ci + fontw]

    return fontw, fonth, char_data


def dsp_char(fontw, fonth, char_data):

    rendered = [["" for _ in range(fontw)] for _ in range(fonth)]

    for i, c in enumerate(char_data):

        for r in range(fonth):
            if c >> r & 0x01:
                rendered[r][i] = "*"

    return rendered


if __name__ == "__main__":
    for ichar in range(254):
        fontw, fonth, char_data = pick_char_data(sysfont, ichar)
        print([hex(int(chard)) for chard in char_data])
        print([(int(chard)) for chard in char_data])
        for line in dsp_char(fontw, fonth, char_data):
            print(" ".join(line))
