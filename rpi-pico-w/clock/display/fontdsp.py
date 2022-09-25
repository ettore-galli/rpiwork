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


def render_char(matrix_value):
    if matrix_value == 1:
        return "#"
    if matrix_value == 2:
        return "#"
    return " "


def dsp_char_matrix(fontw, fonth, char_matrix, render_char=render_char):
    return [
        [render_char(char_matrix[matrix_h][matrix_w]) for matrix_w in range(fontw)]
        for matrix_h in range(fonth)
    ]


def replace_in_matrix(matrix, r, c, submatrix):
    return [
        [
            submatrix[r_i - r][c_i - c]
            if r <= r_i < r + len(submatrix) and c <= c_i < c + len(submatrix[0])
            else element
            for c_i, element in enumerate(row)
        ]
        for r_i, row in enumerate(matrix)
    ]


def print_render_matrix(matrix):
    for row in matrix:
        rendered = " ".join([str(item) for item in row])
        print(rendered)


def zoom_char(fontw, fonth, char_matrix, scale):

    if scale % 2 != 0:
        raise ValueError("Scale must be an even number")

    fontw_z = fontw * scale
    fonth_z = fonth * scale

    zoom_matrix = [[0 for _ in range(fontw_z)] for _ in range(fonth_z)]

    def render_submatrix(scale):
        return [[1 for _ in range(scale)] for _ in range(scale)]

    def render_half_submatrix(scale):
        return [[2 for _ in range(scale // 2)] for _ in range(scale // 2)]

    def is_corner_filled(char_matrix, up, right, r, c):
        return (
            bool(char_matrix[(r + up)][(c + right)])
            if 1 < r + 1 < len(char_matrix) and 1 < c + 1 < len(char_matrix[0])
            else False
        )

    def is_up_left_corner(char_matrix, r, c):
        return (
            # is_corner_filled(char_matrix, -1, -1, r, c)
            is_corner_filled(char_matrix, -1, 0, r, c)
            and is_corner_filled(char_matrix, 0, -1, r, c)
        )

    def is_up_right_corner(char_matrix, r, c):
        return (
            # is_corner_filled(char_matrix, -1, 1, r, c)
            is_corner_filled(char_matrix, -1, 0, r, c)
            and is_corner_filled(char_matrix, 0, 1, r, c)
        )

    def is_down_left_corner(char_matrix, r, c):
        return (
            # is_corner_filled(char_matrix, 1, -1, r, c)
            is_corner_filled(char_matrix, 0, -1, r, c)
            and is_corner_filled(char_matrix, 1, 0, r, c)
        )

    def is_down_right_corner(char_matrix, r, c):
        return (
            # is_corner_filled(char_matrix, 1, 1, r, c)
            is_corner_filled(char_matrix, 0, 1, r, c)
            and is_corner_filled(char_matrix, 1, 0, r, c)
        )

    submatrix = render_submatrix(scale)
    half_submatrix = render_half_submatrix(scale)

    print_render_matrix(submatrix)
    print_render_matrix(half_submatrix)

    for c in range(fontw):
        for r in range(fonth):

            if char_matrix[r][c] == 1:
                zoom_matrix = replace_in_matrix(
                    zoom_matrix, r * scale, c * scale, submatrix
                )

            else:

                if is_up_left_corner(char_matrix, r, c):
                    zoom_matrix = replace_in_matrix(
                        zoom_matrix,
                        r * scale,  # - scale // 2,
                        c * scale,  # - scale // 2,
                        half_submatrix,
                    )

                if is_up_right_corner(char_matrix, r, c):
                    zoom_matrix = replace_in_matrix(
                        zoom_matrix,
                        r * scale,  #  - scale // 2,
                        c * scale + scale // 2,
                        half_submatrix,
                    )

                if is_down_left_corner(char_matrix, r, c):
                    zoom_matrix = replace_in_matrix(
                        zoom_matrix,
                        r * scale + scale // 2,
                        c * scale,  # - scale // 2,
                        half_submatrix,
                    )

                if is_down_right_corner(char_matrix, r, c):
                    zoom_matrix = replace_in_matrix(
                        zoom_matrix,
                        r * scale + scale // 2,
                        c * scale + scale // 2,
                        half_submatrix,
                    )

    return fontw_z, fonth_z, zoom_matrix


def dsp_char_zoom(fontw, fonth, char_data, scale: int):
    matrix = char_matrix(fontw, fonth, char_data)

    fontw_z, fonth_z, matrix_z = zoom_char(fontw, fonth, matrix, scale)

    return dsp_char_matrix(fontw_z, fonth_z, matrix_z)


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
