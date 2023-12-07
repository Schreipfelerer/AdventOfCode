def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for line in lines:
        data.append([line[6:8], int(line.split("=")[1].split(";")[0]),
                     line.split("to valve")[1].lstrip("s").lstrip(" ").split(", ")])
    return data


def solve(data):  # solves the question
    trav_m = [[-1 for i in range(len(data))] for i in range(len(data))]
    for i in range(len(data)):
        trav_m[i][i] = 0

    changed = True
    while changed:
        changed = False
        for i in range(len(data)):
            biggest = max(trav_m[i])
            for j in range(len(data)):
                if trav_m[i][j] == biggest:
                    for k in [k for k in range(len(data)) if data[k][0] in data[j][2]]:
                        if trav_m[i][k] == -1:
                            trav_m[i][k] = trav_m[i][j] + 1
                            changed = True
    return traverse([i for i in range(len(data)) if data[i][0] == "AA"][0], 0, 30, trav_m, [(i, data[i][1]) for i in range(len(data)) if data[i][1]])


def traverse(current_room, potential, minutes_left, trav_m, rooms):
    if minutes_left < 0:
        return -1
    pos = [potential]
    for i, room in enumerate(rooms):
        new_room = room[0]
        new_min = minutes_left-trav_m[current_room][room[0]]-1
        new_pot = potential+room[1]*new_min
        pos.append(traverse(new_room, new_pot, new_min, trav_m, rooms[:i]+rooms[i+1:]))
    return max(pos)


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
