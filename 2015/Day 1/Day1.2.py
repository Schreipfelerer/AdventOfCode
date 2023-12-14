def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    return lines[0]


def solve(data):  # solves the question
    level = 0
    for i, c in enumerate(data):
        if c == "(":
            level += 1
        if c == ")":
            level -= 1
            if level == -1:
                return i + 1


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
