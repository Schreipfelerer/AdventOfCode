import re


def readInput(
    *,
    use_example=False,
) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc) as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    return lines[0]


def solvePart1(data):  # solves the question
    x = re.findall(r"mul\((\d+),(\d+)\)", data)
    sum = 0
    for e in x:
        sum += int(e[0]) * int(e[1])
    return sum


def solvePart2(data):  # solves the question
    no_disabled = re.sub(r"don\'t\(\).*?do\(\)", "", data)
    no_disabled = re.sub(r"don\'t\(\).*$", "", no_disabled)
    multiplications = re.findall(r"mul\((\d+),(\d+)\)", no_disabled)
    sum = 0
    for e in multiplications:
        sum += int(e[0]) * int(e[1])
    return sum


def main():
    lines = readInput()
    data = parseInput(lines)
    print(f"Part 1: {solvePart1(data)}")
    print()
    print(f"Part 2: {solvePart2(data)}")


if __name__ == "__main__":
    main()
