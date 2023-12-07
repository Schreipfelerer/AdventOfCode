filelines = open("input.txt").read().split("\n")

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

    x = 0
    y = 0
    for direction in step:
        x += direction[0]
        y += direction[1]

    if [x, y] in steps:
        steps.remove([x, y])
    else:
        steps.append([x, y])

print(len(steps))
