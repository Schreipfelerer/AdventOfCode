input_data = open("input.txt").readlines()
wire1 = input_data[0].split(",")
wire2 = input_data[1].split(",")

past_postitions1 = []
posX = 0
posY = 0
for instruction in wire1:
    direction = instruction[0]
    parameter = int(instruction[1:])
    if direction == "D":
        for i in range(parameter):
            posY -= 1
            past_postitions1.append((posX, posY))
    if direction == "R":
        for i in range(parameter):
            posX += 1
            past_postitions1.append((posX, posY))
    if direction == "L":
        for i in range(parameter):
            posX -= 1
            past_postitions1.append((posX, posY))
    if direction == "U":
        for i in range(parameter):
            posY += 1
            past_postitions1.append((posX, posY))

past_postitions2 = []
posX = 0
posY = 0
for instruction in wire2:
    direction = instruction[0]
    parameter = int(instruction[1:])
    if direction == "D":
        for i in range(parameter):
            posY -= 1
            past_postitions2.append((posX, posY))
    if direction == "R":
        for i in range(parameter):
            posX += 1
            past_postitions2.append((posX, posY))
    if direction == "L":
        for i in range(parameter):
            posX -= 1
            past_postitions2.append((posX, posY))
    if direction == "U":
        for i in range(parameter):
            posY += 1
            past_postitions2.append((posX, posY))

shortest_D = 999999
for pos1 in past_postitions1:
    if pos1 in past_postitions2:
        distance = abs(pos1[0])+abs(pos1[1])
        if distance < shortest_D:
            shortest_D = distance

print(str(shortest_D))