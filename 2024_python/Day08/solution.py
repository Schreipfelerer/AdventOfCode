def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    data = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ".":
                if char not in data.keys():
                    data[char] = [(x, y)]
                else :
                    data[char] += [(x, y)]
    return data, len(lines)-1, len(lines[0])


def solvePart1(data):  # solves the question
    data, max_y, max_x = data
    anti_pos = set()
    for value in data.values():
        for a in value:
            for b in value:
                if a == b:
                    continue
                pos = (2*a[0]-b[0], 2*a[1]-b[1])
                if 0 <= pos[0] < max_x and 0 <= pos[1] < max_y:
                    anti_pos.add(pos)
    return len(anti_pos)


def solvePart2(data):  # solves the question
    data, max_y, max_x = data
    anti_pos = set()
    for value in data.values():
        for a in value:
            for b in value:
                if a == b:
                    if len(value) > 1:
                        anti_pos.add(a)
                    continue
                i = 1
                pos = ((i+1) * a[0] - i * b[0], (i+1) * a[1] - i * b[1])
                while 0 <= pos[0] < max_x and 0 <= pos[1] < max_y:
                    anti_pos.add(pos)
                    i += 1
                    pos = ((i+1) * a[0] - i * b[0], (i+1) * a[1] - i * b[1])

    return len(anti_pos)


def main():
    lines = readInput()
    data = parseInput(lines)
    print(f"Part 1: {solvePart1(data)}")
    print("")
    print(f"Part 2: {solvePart2(data)}")


if __name__ == "__main__":
    main()
