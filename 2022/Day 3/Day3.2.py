def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    return lines


def solve(data):  # solves the question
    priority = 0
    for i in range(0, len(data), 3):
        common = "".join(set(data[i]).intersection(data[i+1]).intersection(data[i+2]))
        priority += ord(common)-64+26 if common.isupper() else ord(common)-96
    return priority


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
