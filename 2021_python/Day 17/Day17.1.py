def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for kekw in lines[0].rstrip("\n").lstrip("target area: ").split(", "):
        row = []
        for dat in kekw.split("=")[1].split(".."):
            row.append(int(dat))
        data.append(row)

    return data


def solve(data):  # solves the question
    return int((data[1][0] + 1) * data[1][0] / 2)


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
