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
        col = line.rstrip("\n").split(" | ")
        col[0] = col[0].split(" ")
        col[1] = col[1].split(" ")
        data.append(col)

    return data


def solve(data):  # solves the question
    num = 0
    for line in data:
        for digit in line[1]:
            if len(digit) in [2,3,4,7]:
                num += 1

    return num


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
