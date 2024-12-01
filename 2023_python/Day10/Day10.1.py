def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    return [line.rstrip("\n") for line in lines]


def solve(data):  # solves the question
    char_dict = {"J": [(0, -1), (-1, 0)],
                 "L": [(0, 1), (-1, 0)],
                 "7": [(0, -1), (1, 0)],
                 "F": [(0, 1), (1, 0)],
                 "-": [(0, 1), (0, -1)],
                 "|": [(1, 0), (-1, 0)],
                 ".": [],
                 "S": [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]}
    index = (0, 0)
    for i, line in enumerate(data):
        if "S" in line:
            index = (i, line.index("S"))

    offsets = (0, 1), (1, 0), (0, -1), (-1, 0)
    direction = None
    for offset in offsets:
        y = index[0] + offset[0]
        x = index[1] + offset[1]

        if 0 <= y < len(data):
            if 0 <= x < len(data[y]):
                char = data[y][x]
                neg_offset = (-offset[0], -offset[1])
                if neg_offset in char_dict[char]:
                    direction = offset

    steps = 0
    while data[index[0]][index[1]] != "S" or steps == 0:
        index = (index[0] + direction[0], index[1] + direction[1])
        directionlist = char_dict[data[index[0]][index[1]]][:]
        directionlist.remove((-direction[0], -direction[1]))
        direction = directionlist[0]
        steps += 1

    return steps // 2


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
