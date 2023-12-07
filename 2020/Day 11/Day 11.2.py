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
                        if x_off != 0 or y_off != 0:
                            real_x_off = 0
                            real_y_off = 0
                            see = "."
                            while see == ".":
                                real_x_off += x_off
                                real_y_off += y_off
                                if(x + real_x_off >= 0 and y + real_y_off >= 0) and (x + real_x_off < len(c) and y + real_y_off < len(c[x])):
                                    see = c_copy[x + real_x_off][y + real_y_off]
                                else:
                                    see = "L"
                            adjacent += 1 if see == "#" else 0
                if adjacent == 0:
                    c[x][y] = "#"
                if adjacent >= 5:
                    c[x][y] = "L"

print(sum([1 for x in range(len(c)) for y in range(len(c[x])) if c[x][y] == "#"]))
