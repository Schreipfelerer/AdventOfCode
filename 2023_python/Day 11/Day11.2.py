def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for i, line in enumerate(lines):
        for y, char in enumerate(line.rstrip("\n")):
            if char == "#":
                data.append((i, y))
    return lines, data


def solve(data):  # solves the question
    data, galaxies = data
    empty_row = []
    empty_column = []

    for i in range(len(data)):
        if "#" not in data[i]:
            empty_row.append(i)

    for i in range(len(data[0])):
        if all([x[i] == "." for x in data]):
            empty_column.append(i)

    solution = 0
    for i, galax_a in enumerate(galaxies):
        for galax_b in galaxies[i + 1:]:
            distance = abs(galax_a[0] - galax_b[0]) + abs(galax_a[1] - galax_b[1])
            for y in range(min(galax_a[0], galax_b[0]), max(galax_a[0], galax_b[0])):
                if y in empty_row:
                    distance += 1000000 - 1
            for y in range(min(galax_a[1], galax_b[1]), max(galax_a[1], galax_b[1])):
                if y in empty_column:
                    distance += 1000000 - 1
            solution += distance

    return solution


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
