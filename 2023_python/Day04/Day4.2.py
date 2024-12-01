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
        number = int(line.lstrip("Card ").split(":")[0])
        line = line.rstrip("\n").split(": ")[1].split(" | ")
        datapoint = [[], [], number, 1]
        for i in [0, 1]:
            for lit in line[i].split(" "):
                if lit:
                    datapoint[i].append(int(lit))
        data.append(datapoint)
    return data


def solve(data):  # solves the question
    for datapoint in data:
        winners = len(set(datapoint[0]) & set(datapoint[1]))
        if winners:
            for i in range(datapoint[2], datapoint[2] + winners):
                data[i][3] += datapoint[3]
    return sum(map(lambda datapointy: datapointy[3], data))


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
