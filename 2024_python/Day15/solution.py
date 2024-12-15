#!/usr/bin/env python3
def read_input(
    *,
    use_example=False,
) -> str:  # Reads the Input cas be set to read from example.txt
    file_loc = "example2.txt" if use_example else "input.txt"
    with open(file_loc) as f:
        return f.read()


def parse_input(lines):  # parses the input to the desired typ
    split = lines.split("\n\n")
    return [list(x) for x in split[0].split("\n")], split[1].replace("\n", "")


def move(data, x, y, ins):
    ox, oy = [(1, 0), (0, -1), (-1, 0), (0, 1)][[">", "^", "<", "v"].index(ins)]
    ox, oy = x+oy, y+oy
    match data[oy][ox]:
        case "#":
            return x, y
        case "O":
            if (ox, oy) == move(data, ox, oy, ins):
                return x, y

    data[oy][ox] = data[y][x]
    data[y][x] = "."
    return ox, oy


def solve_part1(data):  # solves the question
    grid, instructions = data
    x, y = 0, 0
    for row in grid:
        if "@" in row:
            x, y = row.index("@"), grid.index(row)
    for ins in instructions:
        x, y = move(grid, x, y, ins)

    return calculate_gps_score(grid)


def calculate_gps_score(grid):
    gps = 0
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "O" or char == "[":
                gps += x + 100 * y
    return gps


def solve_part2(data):  # solves the question
    grid, instruction = data
    for y, row in enumerate(grid):
        grid[y] = list(
            "".join(row)
            .replace("#", "##")
            .replace(".", "..")
            .replace("O", "[]")
            .replace("@", "@.")  # noqa: COM812
        )
    x, y = 0, 0
    for row in grid:
        if "@" in row:
            x, y = row.index("@"), grid.index(row)

    for ins in instruction:
        x, y = move2(grid, ins, x, y)

    return calculate_gps_score(grid)


def move2(grid, ins, x, y):
    ox, oy = [(1, 0), (0, -1), (-1, 0), (0, 1)][[">", "^", "<", "v"].index(ins)]
    to_move, to_check = [], [(x, y)]
    while to_check:
        px, py = to_check.pop(0)
        if (px, py) in to_move:
            continue
        if (c := grid[py + oy][px + ox]) == "#":
            break
        to_move.append((px, py))
        if c == ".":
            continue
        if oy:
            to_check.append((px + (1 if grid[py + oy][px + ox] == "[" else -1), py + oy))
        to_check.append((px + ox, py + oy))
    else:
        x, y = x+ox, y+oy
        while to_move:
            px, py = to_move.pop()
            grid[py + oy][px + ox] = grid[py][px]
            grid[py][px] = "."

    return x, y


def main():
    lines = read_input(use_example=False)
    print(f"Part 1: {solve_part1(parse_input(lines))}")
    print()
    print(f"Part 2: {solve_part2(parse_input(lines))}")


if __name__ == "__main__":
    main()
