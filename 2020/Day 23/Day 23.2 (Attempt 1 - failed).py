import time

fileline = open("input.txt").read().split("\n")

cups1 = []
for cup in fileline[0]:  # Parse Input
    cups1.append(int(cup))

cups = cups1 + list(range(len(cups1), 1000000))
current_cup = cups[0]
index = 0

old_t = time.time()
for x in range(10000000):
    if ((x + 1) % 1000) == 0:
        dt = time.time() - old_t
        old_t = time.time()
        print(" Time Taken: " + str(dt) + "s for 10Mio: " + str(int(dt * 10000 / 60 / 60)) + "h " + str(
            int((dt * 10000 / 60) % 60)) + "min")
        print("-- Round" + str(x + 1) + " --", end="")

    pickCups = []
    p_index = (index + 1) % 1000000
    for i in range(3):  # Pick up Cups Clockwise to Starting
        if p_index < index:
            index -= 1
        if p_index == 1000001 - i:
            p_index = 0
        pickCups.append(cups[p_index])
        cups.remove(cups[p_index])

    #  cups[p_index:p_index+3] = []

    destination_cup = current_cup - 1
    while destination_cup not in cups:  # Get Destination Cup
        destination_cup -= 1
        if destination_cup <= 0:
            destination_cup = 1000000

    destination_index = cups.index(destination_cup)

    #  cups[destination_index:destination_index] = pickCups
    offset = 0
    for pCup in pickCups:  # Place Picked Ups Cup
        offset += 1
        p_index = (destination_index + offset) % len(cups)
        cups.insert(p_index, pCup)
        if p_index < destination_index:
            destination_index += 1

    index += 1
    current_cup = cups[index % 10000000]

cups.index(1)
