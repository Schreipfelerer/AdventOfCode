def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    hail = []
    for line in lines:
        line = line[:-1]
        if not line:
            continue
        line = line.replace(' @ ', ', ')
        hail.append(list(map(int, line.split(", "))))
    return hail


def solve(data):  # solves the question
    test_min = 7
    test_max = 27
    return data


def main():
    lines = readInput(True)
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
