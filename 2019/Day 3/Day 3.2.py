input_data = open("input.txt").readlines()
wire1 = input_data[0].split(",")
wire2 = input_data[1].split(",")

past_postitions1 = []
posX = 0
posY = 0
i = 0
for instruction in wire1:
    direction = instruction[0]
    parameter = int(instruction[1:])
    if direction == "D":
        for i in range(parameter):
            i += 1
            posY -= 1
            past_postitions1.append((posX, posY, i))
    if direction == "R":
        for i in range(parameter):
            i += 1
            posX += 1
            past_postitions1.append((posX, posY, i))
    if direction == "L":
        for i in range(parameter):
            i += 1
            posX -= 1
            past_postitions1.append((posX, posY, i))
    if direction == "U":
        for i in range(parameter):
            i += 1
            posY += 1
            past_postitions1.append((posX, posY, i))

past_postitions2 = []
posX = 0
posY = 0
i = 0
for instruction in wire2:
    direction = instruction[0]
    parameter = int(instruction[1:])
    if direction == "D":
        for i in range(parameter):
            i += 1
            posY -= 1
            past_postitions2.append((posX, posY, i))
    if direction == "R":
        for i in range(parameter):
            i += 1
            posX += 1
            past_postitions2.append((posX, posY, i))
    if direction == "L":
        for i in range(parameter):
            i += 1
            posX -= 1
            past_postitions2.append((posX, posY, i))
    if direction == "U":
        for i in range(parameter):
            i += 1
            posY += 1
            past_postitions2.append((posX, posY, i))

shortest_D = 999999
for pos1 in past_postitions1:
    for pos2 in past_postitions2:
        if pos1[0] == pos2[0]:
            if pos1[1] == pos2[1]:
                distance = pos1[2] + pos2[2]
                if distance < shortest_D:
                    shortest_D = distance

print(str(shortest_D))
