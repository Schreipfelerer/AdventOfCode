def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    data = [[int(line), i] for i, line in enumerate(lines)]
    return data


def solve(data):  # solves the question
    zero = None
    for elem in data[:]:
        if elem[0] == 0:
            zero = elem
        i = data.index(elem)
        data.pop(data.index(elem))
        i += elem[0]
        i %= len(data)
        data.insert(i, elem)
    return sum((data[(1000 + data.index(zero)) % len(data)][0],
                data[(2000 + data.index(zero)) % len(data)][0],
                data[(3000 + data.index(zero)) % len(data)][0]))


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
