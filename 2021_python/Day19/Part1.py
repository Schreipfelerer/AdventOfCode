def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = []
    scanner = []
    for line in lines:
        if not line.rstrip("\n"):
            data.append(scanner)
            scanner = []
        elif not line.rstrip("\n").startswith("---"):
            pos = []
            for num in line.rstrip("\n").split(","):
                pos.append(int(num))
            scanner.append(pos)
    data.append(scanner)
    return data


def solve(data):  # solves the question
    return None


def main():
    lines = readInput(True)
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
