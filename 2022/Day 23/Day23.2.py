def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    return lines


def solve(data):  # solves the question
    turn = 0
    proposed_moves = [1]
    while proposed_moves:
        if "#" in data[0]:
            data.insert(0, "." * len(data[0]))
        if "#" in data[-1]:
            data.append("." * len(data[-1]))

        e_l = False
        for row in data:
            if "#" == row[0]:
                e_l = True
        if e_l:
            for x, row in enumerate(data):
                data[x] = "." + row

        e_r = False
        for row in data:
            if "#" == row[-1]:
                e_r = True
        if e_r:
            for x, row in enumerate(data):
                data[x] = row + "."

        proposed_moves = []
        for x, row in enumerate(data):
            for y, c in enumerate(row):
                if c == "#":
                    next_n = 0
                    for x_c in (-1, 0, 1):
                        for y_c in (-1, 0, 1):
                            if not (x_c == 0 == y_c) and data[x + x_c][y + y_c] == "#":
                                next_n += 1

                    if next_n:
                        consider = "NSWENSWE"
                        to_consider = consider[turn % 4: turn % 4 + 4]
                        for con in to_consider:
                            if con == "N":
                                next_n = 0
                                for y_c in (-1, 0, 1):
                                    if data[x - 1][y + y_c] == "#":
                                        next_n += 1
                                if not next_n:
                                    proposed_moves.append([[x, y], [x - 1, y]])
                                    break
                            if con == "S":
                                next_n = 0
                                for y_c in (-1, 0, 1):
                                    if data[x + 1][y + y_c] == "#":
                                        next_n += 1
                                if not next_n:
                                    proposed_moves.append([[x, y], [x + 1, y]])
                                    break
                            if con == "W":
                                next_n = 0
                                for x_c in (-1, 0, 1):
                                    if data[x + x_c][y - 1] == "#":
                                        next_n += 1
                                if not next_n:
                                    proposed_moves.append([[x, y], [x, y - 1]])
                                    break
                            if con == "E":
                                next_n = 0
                                for x_c in (-1, 0, 1):
                                    if data[x + x_c][y + 1] == "#":
                                        next_n += 1
                                if not next_n:
                                    proposed_moves.append([[x, y], [x, y + 1]])
                                    break

        do_moves = []
        for move in proposed_moves:
            collides = False
            for move2 in proposed_moves:
                if move != move2:
                    if move[1] == move2[1]:
                        collides = True
            if not collides:
                do_moves.append(move)

        for move in do_moves:
            data[move[0][0]] = data[move[0][0]][:move[0][1]] + "." + data[move[0][0]][move[0][1] + 1:]
            data[move[1][0]] = data[move[1][0]][:move[1][1]] + "#" + data[move[1][0]][move[1][1] + 1:]

        turn += 1

    return turn+1


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
