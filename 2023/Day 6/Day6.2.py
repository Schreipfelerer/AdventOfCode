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
        data.append(int(line.replace(" ", "").rstrip("\n ").lstrip("Time:Distance ")))
    return data


def solve(data):  # solves the question
    wc = 0
    for mils in range(data[0]):
        distance = (data[0]-mils)*mils
        if distance>data[1]:
            wc+= 1
    return wc


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
