def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for line in lines:
        transition = []
        for cords_i in line.rstrip("\n").split(" -> "):
            cords = []
            for cord in cords_i.split(","):
                cords.append(int(cord))
            transition.append(tuple(cords))
        data.append(tuple(transition))
    return data


def solve(data):  # solves the question
    vents = []
    for i in range(1000):
        line = []
        for j in range(1000):
            line.append(0)
        vents.append(line)

    for transition in data:
        xy1, xy2 = transition
        x1, y1 = xy1
        x2, y2 = xy2
        if x1 == x2 or y1 == y2:
            if x2 < x1:
                x1, x2 = x2, x1
            if y2 < y1:
                y1, y2 = y2, y1
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    vents[x][y] += 1

    counter = 0
    for line in vents:
        for point in line:
            if point >= 2:
                counter += 1

    return counter


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
