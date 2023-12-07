import copy

filelines = open("input.txt").read().split("\n")


hexgrid = []
for x in range(400):
    line = []
    for y in range(400):
        line.append(False)  # True is Black
    hexgrid.append(line)

steps = []
for line in filelines:
    step = []
    while line != "":
        if line.startswith("e"):
            line = line[1:]
            step.append([2, 0])
        if line.startswith("se"):
            line = line[2:]
            step.append([1, -1])
        if line.startswith("sw"):
            line = line[2:]
            step.append([-1, -1])
        if line.startswith("w"):
            line = line[1:]
            step.append([-2, 0])
        if line.startswith("nw"):
            line = line[2:]
            step.append([-1, 1])
        if line.startswith("ne"):
            line = line[2:]
            step.append([1, 1])

    x = 200
    y = 200
    for direction in step:
        x += direction[0]
        y += direction[1]

    hexgrid[x][y] = not hexgrid[x][y]

offsets = [[2, 0], [1, 1], [1, -1], [-2, 0], [-1, 1], [-1, -1]]
for i in range(100):
    old_grid = copy.deepcopy(hexgrid)
    for x in range(0, 400):
        for y in range(x % 2, 400):
            num = 0
            for offset in offsets:
                if 0 <= x+offset[0] < 400:
                    if 0 <= y + offset[1] < 400:
                        if old_grid[x + offset[0]][y + offset[1]]:
                            num += 1
            if old_grid[x][y] and num != 1 and num != 2:
                hexgrid[x][y] = False
            elif (not old_grid[x][y]) and num == 2:
                hexgrid[x][y] = True

    result = 0
    for x in range(0, 400):
        for y in range(x % 2, 400):
            if hexgrid[x][y]:
                result += 1
    print("Round:", i + 1, "Res:", result)
