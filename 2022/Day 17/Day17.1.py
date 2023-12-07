def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    return lines[0]


def solve(data):  # solves the question
    pieces = [["####"], [".#.", "###", ".#."], ["..#", "..#", "###"], ["#", "#", "#", "#"], ["##", "##"]]
    grid = []
    gas_index = 0
    for i in range(2022):
        piece = pieces[i % len(pieces)]
        highest = len(grid)
        for row in reversed(grid):
            if row == "       ":
                highest -= 1
            else:
                break

        x = 2
        y = len(piece)+2+highest

        while len(grid) <= y:
            grid.append("       ")

        is_falling = True
        do_push = True
        while is_falling:

            check_points = []
            gas_right = data[gas_index] == ">"
            if do_push:
                gas_index += 1
                gas_index %= len(data)

                for j, row in enumerate(piece):
                    if gas_right:
                        check_points.append([x + len(row.rstrip(".")), y - j])
                    else:
                        check_points.append([x - 1 + len(row) - len(row.lstrip(".")), y - j])
            else:
                if i % len(pieces) == 1:
                    check_points = [[x, y-2], [x+1, y-3], [x+2, y-2]]
                else:
                    for j in range(len(piece[-1])):
                        check_points.append([x+j, y-len(piece)])

            is_clear = True
            for p in check_points:
                if not (0 <= p[0] < 7) or p[1] == -1:
                    is_clear = False
                else:
                    if grid[p[1]][p[0]] == "#":
                        is_clear = False

            if is_clear:
                if do_push:
                    x += 1 if gas_right else -1
                else:
                    y -= 1

            elif not do_push:
                is_falling = False
                for y_off, row in enumerate(piece):
                    for x_off, p in enumerate(row):
                        if p == "#":
                            grid[y-y_off] = grid[y-y_off][:x+x_off] + "#" + grid[y-y_off][x+x_off+1:]

            do_push = not do_push

    hight = len(grid)
    for i in reversed(grid):
        if i == "       ":
            hight -= 1
        else:
            break
    return hight


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
