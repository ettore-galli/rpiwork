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
            else:
                rendered[r][i] = " "
    return rendered


def dsp_char_n(fontw, fonth, char_data, n_half: int):

    n = 2 * n_half

    rendered = [["" for _ in range(fontw * n)] for _ in range(fonth * n)]

    for i, c in enumerate(char_data):
        di = n * i
        for h in range(n):
            for r in range(fonth):
                dr = n * r
                if c >> r & 0x01:
                    rendered[dr + h][di] = "*" * n
                else:
                    fillmatrix = [[" " for _ in range(n)] for _ in range(n)]
                    if r > 0:
                        if c >> (r - 1) & 0x01:
                            for fr in range(n_half):
                                for fc in range(n):
                                    fillmatrix[fr][fc] = "*"
                    if r < fontw:
                        if c >> (r + 1) & 0x01:
                            for fr in range(n_half, n):
                                for fc in range(n):
                                    fillmatrix[fr][fc] = "*"

                    dw = r < fonth - 1 and c >> (r + 1) & 0x01
                    up = r > 0 and c >> (r - 1) & 0x01
                    le = i > 0 and char_data[i - 1] >> r & 0x01
                    ri = i < fontw - 1 and char_data[i + 1] >> r & 0x01

                    if False:
                        rendered[dr + h][di] = " " * n

                    else:
                        for q in range(n):
                            for w in range(n):
                                rendered[dr + q][di + w] = fillmatrix[q][w]
    return rendered


if __name__ == "__main__":
    for ichar in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ":"]:
        
        fontw, fonth, char_data = pick_char_data(sysfont, ichar)
        
        print([hex(int(chard)) for chard in char_data])
        print([(int(chard)) for chard in char_data])
        print("\n")
        for line in dsp_char(fontw, fonth, char_data):
            print("".join(line))
        for line in dsp_char_n(fontw, fonth, char_data, 2):
            print("".join(line))
