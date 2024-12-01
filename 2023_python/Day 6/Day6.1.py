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
        data.append([int(x) for x in line.rstrip("\n ").lstrip("Time:Distance ").split(" ") if x])
    return data


def solve(data):  # solves the question
    multi = 1
    for race in range(len(data[0])):
        wc = 0
        for mils in range(data[0][race]):
            distance = (data[0][race] - mils) * mils
            if distance > data[1][race]:
                wc += 1
        multi *= wc
    return multi


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
