c = []
with open("input.txt") as file:
    for line in file:
        c.append(line)

num = 0
x = 0
y = 0
while True:
    x += 3
    y += 1
    try:
        if (c[y][x % (len(c[y]) - 1)]) == "#":
            num += 1
    except IndexError:
        print(num)
        break
