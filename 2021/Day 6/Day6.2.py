def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for num in lines[0].rstrip("\n").split(","):
        data[int(num)] += 1
    return data


def solve(data):  # solves the question
    for i in range(256):
        data[9] = data[0]
        data[7] += data[0]
        data = data[1:] + [0]

    return sum(data)


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
