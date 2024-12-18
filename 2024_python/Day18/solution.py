#!/usr/bin/env python3
def read_input(
    *,
    use_example=False,
) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc) as f:
        return f.read().split("\n")


def parse_input(lines):  # parses the input to the desired typ
    return [[int(x) for x in line.split(",")] for line in lines[:-2]]


def solve_part1(data):  # solves the question
    dim = 70  # 6
    byte_falls = 1024  # 12
    grid = [[False for _ in range(dim + 1)] for _ in range(dim + 1)]
    for d in data[:byte_falls]:
        x, y = d
        if 0 <= x <= dim and 0 <= y <= dim:
            grid[y][x] = True

    reach = [[dim**3 for _ in range(dim + 1)] for _ in range(dim + 1)]
    start = (0, 0)
    queue = {start}
    reach[0][0] = 0
    while queue:
        x, y = queue.pop()
        for n in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            nx, ny = n
            if (
                0 <= nx <= dim
                and 0 <= ny <= dim
                and not grid[ny][nx]
                and reach[y][x] + 1 < reach[ny][nx]
            ):
                reach[ny][nx] = reach[y][x] + 1
                queue.add((nx, ny))
    return reach[dim][dim]


def solve_part2(data):  # solves the question
    dim = 70  # 6
    grid = [[False for _ in range(dim + 1)] for _ in range(dim + 1)]
    for d in data:
        x, y = d
        if 0 <= x <= dim and 0 <= y <= dim:
            grid[y][x] = True

        reach = [[dim**3 for _ in range(dim + 1)] for _ in range(dim + 1)]
        start = (0, 0)
        queue = {start}
        reach[0][0] = 0
        while queue:
            x, y = queue.pop()
            for n in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                nx, ny = n
                if (
                    0 <= nx <= dim
                    and 0 <= ny <= dim
                    and not grid[ny][nx]
                    and reach[y][x] + 1 < reach[ny][nx]
                ):
                    reach[ny][nx] = reach[y][x] + 1
                    queue.add((nx, ny))

        if reach[dim][dim] == dim**3:
            x, y = d
            return f"{x},{y}"

    return "Nothing"


def main():
    lines = read_input(use_example=False)
    print(f"Part 1: {solve_part1(parse_input(lines))}")
    print()
    print(f"Part 2: {solve_part2(parse_input(lines))}")


if __name__ == "__main__":
    main()
