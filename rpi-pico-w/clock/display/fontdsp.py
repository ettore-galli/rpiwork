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


def char_matrix(fontw, fonth, char_data):

    rendered = [[0 for _ in range(fontw)] for _ in range(fonth)]

    for i, c in enumerate(char_data):

        for r in range(fonth):
            if c >> r & 0x01:
                rendered[r][i] = 1

    return rendered


def dsp_char_matrix(fontw, fonth, char_matrix, render_char="#"):
    return [
        [
            render_char if char_matrix[matrix_h][matrix_w] == 1 else " "
            for matrix_w in range(fontw)
        ]
        for matrix_h in range(fonth)
    ]


def zoom_char(fontw, fonth, char_matrix, scale):
    fontw_z = fontw * scale
    fonth_z = fonth * scale

    zoom_matrix = [[0 for _ in range(fontw_z)] for _ in range(fonth_z)]

    for c in range(fontw):
        for r in range(fonth):

            if char_matrix[r][c] == 1:
                for x in range(scale):
                    for y in range(scale):
                        zoom_matrix[r * scale + x][c * scale + y] = 1

    return fontw_z, fonth_z, zoom_matrix


def dsp_char_zoom(fontw, fonth, char_data, scale: int):
    matrix = char_matrix(fontw, fonth, char_data)

    fontw_z, fonth_z, matrix_z = zoom_char(fontw, fonth, matrix, scale)

    return dsp_char_matrix(fontw_z, fonth_z, matrix_z)


# def dsp_char_n(fontw, fonth, char_data, n_half: int):

#     n = 2 * n_half

#     rendered = [["" for _ in range(fontw * n)] for _ in range(fonth * n)]

#     for i, c in enumerate(char_data):

#         di = n * i

#         for h in range(n):

#             for r in range(fonth):

#                 dr = n * r

#                 if c >> r & 0x01:
#                     rendered[dr + h][di] = "*" * n
#                 else:

#                     fillmatrix = [[" " for _ in range(n)] for _ in range(n)]

#                     if r > 0:
#                         if c >> (r - 1) & 0x01:
#                             for fr in range(n_half):
#                                 for fc in range(n):
#                                     fillmatrix[fr][fc] = "*"
#                     if r < fontw:
#                         if c >> (r + 1) & 0x01:
#                             for fr in range(n_half, n):
#                                 for fc in range(n):
#                                     fillmatrix[fr][fc] = "*"

#                     dw = r < fonth - 1 and c >> (r + 1) & 0x01
#                     up = r > 0 and c >> (r - 1) & 0x01
#                     le = i > 0 and char_data[i - 1] >> r & 0x01
#                     ri = i < fontw - 1 and char_data[i + 1] >> r & 0x01

#                     if False:
#                         rendered[dr + h][di] = " " * n

#                     else:
#                         for q in range(n):
#                             for w in range(n):
#                                 rendered[dr + q][di + w] = fillmatrix[q][w]
#     return rendered


if __name__ == "__main__":
    for ichar in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ":"]:

        fontw, fonth, char_data = pick_char_data(sysfont, ichar)

        print([hex(int(chard)) for chard in char_data])
        print([(int(chard)) for chard in char_data])
        print("\n")
        for line in dsp_char(fontw, fonth, char_data):
            print("".join(line))
        for line in dsp_char_zoom(fontw, fonth, char_data, 4):
            print("".join(line))
