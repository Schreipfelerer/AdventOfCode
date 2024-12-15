#!/usr/bin/env python3
def read_input(
        *,
        use_example=False,
) -> str:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc) as f:
        return f.read()


def parse_input(lines):  # parses the input to the desired typ
    split = lines.split("\n\n")
    return [list(x) for x in split[0].split("\n")], split[1].replace("\n", "")


def move(data, x, y, ins):
    ox, oy = [(1, 0),(0, -1),(-1, 0),(0, 1)][[">", "^", "<", "v"].index(ins)]
    match data[y+oy][x+ox]:
        case "#":
            return x, y
        case ".":
            return x+ox, y+oy
        case "O":
            return 0, 0
    return 0, 0


def solve_part1(data):  # solves the question
    grid, instructions = data
    x, y = 0, 0
    for row in grid:
        if "@" in row:
            x, y = row.index("@"), grid.index(row)
    for ins in instructions:
        x, y = move(data, x, y, ins)

    gps = 0
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == "O":
                gps += x + 100 * y
    return gps


def solve_part2(data):  # solves the question
    return data


def main():
    lines = read_input(use_example=True)
    data = parse_input(lines)
    print(f"Part 1: {solve_part1(data)}")
    print()
    print(f"Part 2: {solve_part2(data)}")


if __name__ == "__main__":
    main()
