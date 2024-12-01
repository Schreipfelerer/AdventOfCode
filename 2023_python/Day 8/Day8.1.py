def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = [lines[0].strip("\n"), dict()]
    for line in lines[2:]:
        data[1][line[0:3]] = (line[7:10], line[12:15])
    return data


def solve(data):  # solves the question
    pos = "AAA"
    steps = 0
    while pos != "ZZZ":
        direction = 0 if data[0][steps % len(data[0])] == "L" else 1
        pos = data[1][pos][direction]
        steps += 1
    return steps


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
