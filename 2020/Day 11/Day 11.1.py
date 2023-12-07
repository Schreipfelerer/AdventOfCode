c = []
with open("input.txt") as file:
    for line in file:
        c.append(list(line.rstrip("\n")))
c_copy = []

while c != c_copy:
    c_copy = [c[x].copy() for x in range(len(c))]
    for x in range(len(c_copy)):
        for y in range(len(c_copy[x])):
            if c_copy[x][y] != ".":
                adjacent = 0
                for x_off in range(-1, 2):
                    for y_off in range(-1, 2):
                        if (x_off != 0 or y_off != 0) and (x + x_off >= 0 and y + y_off >= 0) and (x + x_off < len(c) and y + y_off < len(c[x])):
                            adjacent += 1 if c_copy[x + x_off][y + y_off] == "#" else 0
                if adjacent == 0:
                    c[x][y] = "#"
                if adjacent >= 4:
                    c[x][y] = "L"

print(sum([1 for x in range(len(c)) for y in range(len(c[x])) if c[x][y] == "#"]))
