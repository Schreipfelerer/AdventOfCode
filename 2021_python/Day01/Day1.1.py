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
        data.append(int(line))
    return data


def solve(data):  # solves the question
    num_increase = 0
    last_m = None
    for measurement in data:
        if not last_m:
            last_m = measurement
        else:
            if measurement > last_m:
                num_increase += 1
            last_m = measurement
    return num_increase


def main():
    lines = readInput(False)
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
