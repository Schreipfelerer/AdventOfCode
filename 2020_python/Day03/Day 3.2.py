c = []
with open("input.txt") as file:
    for line in file:
        c.append(line)


def start(acc_x, acc_y):
    num = 0
    x = 0
    y = 0
    while True:
        x += acc_x
        y += acc_y
        try:
            if (c[y][x % (len(c[y]) - 1)]) == "#":
                num += 1
        except IndexError:
            return num


print(str(start(1, 1) * start(3, 1) * start(5, 1) * start(7, 1) * start(1, 2)))
