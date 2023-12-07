def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    data = lines[:-2]
    path = []
    for row in lines[-1].split("R"):
        for a in row.split("L"):
            path.append(int(a))
            path.append("L")
        path[-1] = "R"
    path.pop()

    return data, path


def solve(data):  # solves the question
    data, path = data
    longline = max([len(row) for row in data])
    data = [row.ljust(longline) for row in data]
    rev = [data[i][::-1] for i in range(len(data)-1, -1, -1)]
    rotated = ["".join([data[j][i] for j in range(len(data))]) for i in range(len(data[0]))]
    rotated_rev = [rotated[i][::-1] for i in range(len(rotated)-1, -1, -1)]
    facing = 0
    row = 0
    column = data[0].index(".")
    for ind, op in enumerate(path):
        if type(op) == int:
            print((row + 1, column + 1, facing, ind))
            for _ in range(op):
                row_new = row
                if facing % 2 == 1:
                    row_new -= facing-2
                column_new = column
                if facing % 2 == 0:
                    column_new -= facing-1
                row_new %= len(data)
                column_new %= len(data[0])

                if data[row_new][column_new] == " ":
                    if facing == 0:
                        column_new = min(data[row_new].index("."), data[row_new].index("#"))
                    if facing == 1:
                        row_new = min(rotated[column_new].index("."), rotated[column_new].index("#"))
                    if facing == 2:
                        column_new = len(data[0]) - min(rev[len(data)-row_new].index("."), rev[len(data)-row_new].index("#")) - 1
                    if facing == 3:
                        row_new = len(data) - min(rotated_rev[len(data[0])-column_new].index("."), rotated_rev[len(data[0])-column_new].index("#")) - 1
                if data[row_new][column_new] == "#":
                    break
                if data[row_new][column_new] == ".":
                    row = row_new
                    column = column_new
        else:
            facing += 1 if op == "R" else -1
            facing %= 4

    return 1000 * (row+1) + 4 * (column+1) + facing


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
