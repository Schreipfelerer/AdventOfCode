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
        line = line.rstrip("\n").split(": ")[1].split(" | ")
        datapoint = [[], []]
        for i in [0, 1]:
            for lit in line[i].split(" "):
                if lit:
                    datapoint[i].append(int(lit))
        data.append(datapoint)
    return data


def solve(data):  # solves the question
    sol = 0
    for datapoint in data:
        length = len(set(datapoint[0]) & set(datapoint[1]))
        if length:
            sol += 2 ** (length - 1)
    return sol


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
