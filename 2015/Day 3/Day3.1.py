def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    return lines[0]


def solve(data):  # solves the question
    pos = [0, 0]
    delivered = {(0, 0)}
    for c in data:
        if c == ">":
            pos[0] += 1
        elif c == "v":
            pos[1] += 1
        elif c == "<":
            pos[0] -= 1
        elif c == "^":
            pos[1] -= 1
        delivered.add((pos[0], pos[1]))

    return len(delivered)


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
