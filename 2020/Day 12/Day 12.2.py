c = []
with open("input.txt") as file:
    for line in file:
        c.append(line.rstrip("\n"))

pos = [10, 1]
pos_ship = [0, 0]
for instruction in c:
    if instruction[0] == "N":
        pos[1] += int(instruction[1:])
    elif instruction[0] == "S":
        pos[1] -= int(instruction[1:])
    elif instruction[0] == "E":
        pos[0] += int(instruction[1:])
    elif instruction[0] == "W":
        pos[0] -= int(instruction[1:])
    elif instruction[0] == "L":
        for i in range(int(int(instruction[1:]) / 90)):
            pos[0], pos[1] = 0 - pos[1], pos[0]
    elif instruction[0] == "R":
        for i in range(int(int(instruction[1:]) / 90)):
            pos[0], pos[1] = pos[1], 0 - pos[0]
    elif instruction[0] == "F":
        pos_ship[0] += (pos[0] * int(instruction[1:]))
        pos_ship[1] += (pos[1] * int(instruction[1:]))

print(sum([abs(x) for x in pos_ship]))
print(pos_ship)
