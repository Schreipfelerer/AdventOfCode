def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = [[9] * (len(lines[0]))]
    for line in lines:
        row = [9]
        for hight in line.rstrip("\n"):
            row.append(int(hight))
        row.append(9)
        data.append(row)
    data.append([9] * (len(lines[0])))
    return data


def solve(data):  # solves the question
    lowpoints = []
    for i, row in enumerate(data):
        if i != 0 and i != len(data)-1:
            for j, digit in enumerate(row):
                if j != 0 and j != len(row) - 1:
                    if digit < row[j-1] and digit < row[j+1] and digit < data[i-1][j] and digit < data[i+1][j]:
                        lowpoints.append((i, j))

    basins = []
    for lowpoint in lowpoints:
        basins.append(grow(data, [], lowpoint))

    basin_sizes = []
    for basin in basins:
        basin_sizes.append(len(basin))

    basin_sizes.sort()
    return basin_sizes[-1]*basin_sizes[-2]*basin_sizes[-3]


def grow(data, basin, pos):
    x, y = pos
    if pos in basin:
        return basin
    if data[x][y] == 9:
        return basin
    basin.append(pos)
    basin = grow(data, basin, (x, y + 1))
    basin = grow(data, basin, (x, y - 1))
    basin = grow(data, basin, (x + 1, y))
    basin = grow(data, basin, (x - 1, y))
    return basin


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
