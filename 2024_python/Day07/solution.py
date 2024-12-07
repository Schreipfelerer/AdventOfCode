def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for line in lines:
        if not line:
            continue
        line = line.split(": ")
        evaluatiuon = int(line[0])
        numbers = list(map(int, line[1].split(" ")))
        data.append((evaluatiuon, numbers))
    return data


def solvePart1(data):  # solves the question
    solution = 0
    for test, numbers in data:
        p = possibleValues(numbers)
        if test in p:
            solution += test
    return solution


def solvePart2(data):  # solves the question
    solution = 0
    for test, numbers in data:
        p = possibleValues2(numbers)
        if test in p:
            solution += test
    return solution


def possibleValues(values: [int]):
    if len(values) < 2:
        return set(values)
    possibles = possibleValues(values[:-1])
    possibles_added = set(map(lambda x: x + values[-1], possibles))
    possibles_mul = set(map(lambda x: x * values[-1], possibles))
    return possibles_added.union(possibles_mul)


def possibleValues2(values: [int]):
    if len(values) < 2:
        return set(values)
    possibles = possibleValues2(values[:-1])
    possibles_added = set(map(lambda x: x + values[-1], possibles))
    possibles_mul = set(map(lambda x: x * values[-1], possibles))
    possibles_con = set(map(lambda x: int(str(x)+str(values[-1])), possibles))
    return possibles_added.union(possibles_mul).union(possibles_con)


def main():
    lines = readInput()
    data = parseInput(lines)
    print(f"Part 1: {solvePart1(data)}")
    print("")
    print(f"Part 2: {solvePart2(data)}")


if __name__ == "__main__":
    main()
