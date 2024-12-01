c = []
with open("input.txt") as file:
    for line in file:
        c.append(line.rstrip("\n"))

direction = 1
pos = [0, 0]
for instruction in c:
    if instruction[0] == "N":
        pos[1] += int(instruction[1:])
    elif instruction[0] == "S":  # IST FALSCH ABER TROTZDEM FALSCH
        pos[0] += int(instruction[1:])
    elif instruction[0] == "E":
        pos[1] -= int(instruction[1:])
    elif instruction[0] == "W":
        pos[0] -= int(instruction[1:])
    elif instruction[0] == "L":
        direction -= int(instruction[1:]) / 90
    elif instruction[0] == "R":
        direction += int(instruction[1:]) / 90
    elif instruction[0] == "F":
        if direction % 4 == 0:
            pos[1] += int(instruction[1:])
        if direction % 4 == 1:
            pos[0] += int(instruction[1:])
        if direction % 4 == 2:
            pos[1] -= int(instruction[1:])
        if direction % 4 == 3:
            pos[0] -= int(instruction[1:])

print(sum([abs(x) for x in pos]))
