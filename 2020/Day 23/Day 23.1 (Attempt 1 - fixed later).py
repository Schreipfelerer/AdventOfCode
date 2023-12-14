fileline = open("example.txt").read().split("\n")


def printNice():
    result = ""  # Print as required by Task
    for cup in cups[cups.index(1):]:
        result = result + str(cup)

    for cup in cups[:cups.index(1)]:
        result = result + str(cup)

    result = result.lstrip("1")
    print(result)


def printCups(coll, cur_cup, msg=""):
    string_list = []
    for el in coll:
        if el == cur_cup:
            string_list.append("(" + str(el) + ")")
        else:
            string_list.append(" " + str(el) + " ")
    # print(msg + " ".join(string_list))


cups = []
for cup in fileline[0]:  # Parse Input
    cups.append(int(cup))

current_cup = cups[0]

for x in range(100):
    # print("--move: " + str(x+1) + " --")
    index = cups.index(current_cup)

    # printCups(cups, current_cup, "Before Pick Up:")

    pickCups = []
    p_index = (index + 1) % len(cups)
    for i in range(3):  # Pick up Cups Clockwise to Starting
        if p_index == len(cups):
            p_index = 0
        pickCups.append(cups[p_index])
        cups.remove(cups[p_index])

    # printCups(cups, current_cup, "After Pick Up: ")
    # print("")

    destination_cup = current_cup - 1
    while destination_cup not in cups:  # Get Destination Cup
        destination_cup -= 1
        if destination_cup <= 0:
            destination_cup = max(cups)

    destination_index = cups.index(destination_cup)

    # printCups(cups, destination_cup, "Before Insertion Up:")
    offset = 0
    original_len = len(cups)
    for pCup in pickCups:  # Place Picked Ups Cup
        offset += 1
        index = (cups.index(destination_cup) + offset) % len(cups)
        cups.insert(index, pCup)

    # printCups(cups, destination_cup, "After Insertion Up: ")
    # print("")
    # print("")

    current_cup = cups[(cups.index(current_cup) + 1) % len(cups)]
    # printNice()
    pass
