import random


# ============================
def change_numbers(string):
    numbers = list('123456789')
    random.shuffle(numbers)

    out = ''
    for c in string:
        if '0' == c:
            out += c
        else:
            out += numbers[int(c)-1]

    return out


# ============================
def flip_rows(string):
    rows = [0, 1, 2]
    random.shuffle(rows)

    out = [''] * 81

    for k in range(3):
        for i in range(3):
            for j in range(9):
                c = string[k*3+i + 9*j]
                out[rows[k]*3+i + 9*j] = c

    return ''.join(out)


# ============================
def flip_cols(string):
    rows = [0, 1, 2]
    random.shuffle(rows)

    out = [''] * 81

    for k in range(3):
        for i in range(9):
            for j in range(3):
                c = string[i + 9*(j+k*3)]
                out[i + 9*(j+rows[k]*3)] = c

    return ''.join(out)


# ============================
def rotate(string):
    angle = random.randint(0, 3)

    if 0 == angle:
        out = list(string)
    else:
        out = [''] * 81

        for i in range(9):
            for j in range(9):
                if 1 == angle:
                    out[i*9+(8-j)] = string[i+9*j]
                elif 2 == angle:
                    out[(8-i)+9*(8-j)] = string[i+9*j]
                else:
                    out[j+9*(8-i)] = string[i+9*j]

    return ''.join(out)
