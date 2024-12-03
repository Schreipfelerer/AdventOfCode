def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = []
    s = None
    for y, line in enumerate(lines):
        line = line[:-1]
        if not line:
            continue
        dataline = []
        for x, char in enumerate(line):
            dataline.append(char == '#')
            if char == 'S':
                s = (x, y)
        data.append(dataline)
    return data, s


def solve(data):  # solves the question
    steps_needed = 64
    data, s = data
    possible_locations = {s}
    next_locations = set()

    for _ in range(steps_needed):
        for p in possible_locations:
            for offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if not (0 <= p[0] + offset[0] < len(data[0])):
                    continue
                if not (0 <= p[1] + offset[1] < len(data)):
                    continue
                if data[p[0] + offset[0]][p[1] + offset[1]]:
                    continue
                next_locations.add((p[0] + offset[0], p[1] + offset[1]))
        possible_locations = next_locations
        next_locations = set()
    return len(possible_locations)


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
