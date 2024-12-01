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
    trav_m = [[-1 for _ in range(len(data))] for _ in range(len(data))]
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
    return traverse([i for i in range(len(data)) if data[i][0] == "AA"][0],
                    [i for i in range(len(data)) if data[i][0] == "AA"][0],
                    0, 26, trav_m, [(i, data[i][1]) for i in range(len(data)) if data[i][1]], 0, 0)


def traverse(room_me, room_el, pot, minutes, trav_m, rooms, stun_me, stun_el):
    if minutes - max(stun_el, stun_me) < 0:
        return -1
    if stun_me > 0 and stun_el > 0:
        return traverse(room_me, room_el, pot, minutes - 1, trav_m, rooms, stun_me - 1, stun_el - 1)
    if not stun_me:
        pos = [pot]
        for i, room in enumerate(rooms):
            timespent = trav_m[room_me][room[0]] + 1
            new_pot = pot + room[1] * (minutes - timespent)
            pos.append(
                traverse(room[0], room_el, new_pot, minutes, trav_m, rooms[:i] + rooms[i + 1:], timespent, stun_el))
    else:
        pos = [pot]
        for i, room in enumerate(rooms):
            timespent = trav_m[room_el][room[0]] + 1
            new_pot = pot + room[1] * (minutes - timespent)
            pos.append(
                traverse(room_me, room[0], new_pot, minutes, trav_m, rooms[:i] + rooms[i + 1:], stun_me, timespent))
    return max(pos)


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
