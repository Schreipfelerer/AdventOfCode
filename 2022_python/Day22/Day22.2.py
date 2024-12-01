import math


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
    faces = sum([sum([1 for c in row if c == "." or c == "#"]) for row in data])
    width = int(math.sqrt(faces // 6))
    data = [row.ljust(width * 4) for row in data]
    while len(data) < width * 4:
        data.append(" " * (width * 4))
    faces = [" " * 4 for _ in range(4)]
    faces_aplha = list("ABCDEF")
    for row in range(4):
        for column in range(4):
            c = data[row * width][column * width]
            if c == "." or c == "#":
                faces[row] = faces[row][:column] + faces_aplha.pop(0) + faces[row][column + 1:]

    trans = [[[" ", -1] for _ in range(4)] for _ in range(6)]

    for row in range(4):
        for column in range(4):
            c = faces[row][column]
            if c != " ":
                for face in range(4):
                    row_new = row
                    if face % 2 == 1:
                        row_new -= face - 2
                    column_new = column
                    if face % 2 == 0:
                        column_new -= face - 1
                    row_new %= 4
                    column_new %= 4

                    c2 = faces[row_new][column_new]
                    if c2 != " ":
                        trans[ord(c) - 65][face][0] = c2
                        trans[ord(c) - 65][face][1] = (face + 2) % 4

    for _ in range(4):
        for c in range(6):  # A
            for i in range(4):  # Facing AB for A
                if trans[c][i][1] != -1:
                    for offset in (-1, 1):
                        if trans[c][(i + offset) % 4][1] == -1:
                            index_target = ord(trans[c][i][0]) - 65  # Index of B
                            facing_new = (trans[c][i][1] - offset) % 4  # Facing AB for B
                            if trans[index_target][facing_new][1] != -1:
                                new_c = trans[index_target][facing_new][0]  # C
                                facing = (trans[index_target][facing_new][1] - offset) % 4  # Facing AC for A
                                trans[c][(i + offset) % 4] = [new_c, facing]  # Set AC for A
                                trans[ord(new_c) - 65][facing] = [chr(c + 65), (i + offset) % 4]  # Set AC for C

    facing = 0
    row = 0
    column = data[0].index(".")
    for ind, op in enumerate(path):
        if type(op) == int:
            for _ in range(op):
                row_new = row
                if facing % 2 == 1:
                    row_new -= facing - 2
                column_new = column
                if facing % 2 == 0:
                    column_new -= facing - 1
                row_new %= len(data)
                column_new %= len(data[0])
                facing_new = facing

                if data[row_new][column_new] == " ":
                    a = faces[row // width][column // width]
                    c, c_face = trans[ord(a) - 65][facing]
                    facing_new = (c_face + 2) % 4

                    row_cell = row % width
                    column_cell = column % width

                    if facing % 2 == 0:
                        row_cell = width - 1 - row_cell
                    else:
                        column_cell = width - 1 - column_cell

                    for _ in range((c_face - facing) % 4):
                        row_cell, column_cell = column_cell, (width - 1 - row_cell)

                    c_x = -1
                    c_y = -1
                    for x in range(4):
                        for y in range(4):
                            if faces[x][y] == c:
                                c_x = x
                                c_y = y

                    row_new = width * c_x + row_cell
                    column_new = width * c_y + column_cell
                if data[row_new][column_new] == "#":
                    break
                if data[row_new][column_new] == ".":
                    row = row_new
                    column = column_new
                    facing = facing_new
        else:
            facing += 1 if op == "R" else -1
            facing %= 4

    return 1000 * (row + 1) + 4 * (column + 1) + facing


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
