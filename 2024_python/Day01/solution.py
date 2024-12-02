def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    data1 = []
    data2 = []
    for line in lines:
        if not line:
            continue
        line = line.split("   ")
        data1.append(int(line[0]))
        data2.append(int(line[1]))
    return data1, data2


def solvePart1(data):  # solves the question
    data1, data2 = data
    data1.sort()
    data2.sort()
    data = zip(data1, data2)
    sum = 0
    for (d1, d2) in data:
        sum += abs(d1 - d2)
    return sum

def solvePart2(data):  # solves the question
    data1, data2 = data
    sum = 0
    for d1 in data1:
        sum += d1*data2.count(d1)
    return sum


def main():
    lines = readInput()
    data = parseInput(lines)
    print(f"Part 1: {solvePart1(data)}")
    print("")
    print(f"Part 2: {solvePart2(data)}")


if __name__ == "__main__":
    main()
