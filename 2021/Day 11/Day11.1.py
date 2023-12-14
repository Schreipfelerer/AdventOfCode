def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for line in lines:
        row = []
        for char in line.rstrip("\n"):
            row.append(int(char))
        data.append(row)
    return data


def solve(data):  # solves the question
    flashes = 0
    for i in range(100):
        for row in data:
            for i, octo in enumerate(row):
                row[i] += 1

        flashed = True
        while flashed:
            flashed = False
            for i, row in enumerate(data):
                for j, octo in enumerate(row):
                    if octo >= 10:
                        flashes += 1
                        flashed = True
                        if i != 0 and j != 0:
                            data[i - 1][j - 1] += 1
                        if i != 0:
                            data[i - 1][j] += 1
                        if i != 0 and j != 9:
                            data[i - 1][j + 1] += 1
                        if j != 9:
                            data[i][j + 1] += 1
                        if i != 9 and j != 9:
                            data[i + 1][j + 1] += 1
                        if i != 9:
                            data[i + 1][j] += 1
                        if i != 9 and j != 0:
                            data[i + 1][j - 1] += 1
                        if j != 0:
                            data[i][j - 1] += 1
                        data[i][j] = -10

        for i, row in enumerate(data):
            for j, octo in enumerate(row):
                if octo < 0:
                    row[j] = 0

    return flashes


def main():
    lines = readInput(False)
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
