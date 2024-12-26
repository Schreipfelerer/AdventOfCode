#!/usr/bin/env python3
def read_input(
    *,
    use_example=False,
) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc) as f:
        return f.read().split("\n")


def parse_input(lines):  # parses the input to the desired typ
    return [list(line) for line in lines[:-2]]


def dijkstra_from_char(grid, char):
    end = None
    steps = [[2**31 for _ in row] for row in grid]
    end = index_char(grid, char)
    steps[end[1]][end[0]] = 0
    queue = {end}
    while queue:
        x, y = queue.pop()
        for nx, ny in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            if (
                0 <= nx < len(grid[0])
                and 0 <= ny < len(grid)
                and grid[ny][nx] != "#"
                and steps[y][x] < steps[ny][nx] - 1
            ):
                steps[ny][nx] = steps[y][x] + 1
                queue.add((nx, ny))
    return steps


def index_char(grid, char):
    index = None
    for y, row in enumerate(grid):
        if char in row:
            for x, c in enumerate(row):
                if c == char:
                    index = x, y
    return index


def solve_part1(data):  # solves the question
    cheating_threshold = 100
    end_steps = dijkstra_from_char(data, "E")
    start_steps = dijkstra_from_char(data, "S")
    start_loc = index_char(data, "S")
    normal_steps = end_steps[start_loc[1]][start_loc[0]]
    cheats = 0
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c != "#":
                for nx, ny in [
                    (x + 2, y),
                    (x + 1, y + 1),
                    (x, y + 2),
                    (x - 1, y + 1),
                    (x - 2, y),
                    (x - 1, y - 1),
                    (x, y - 2),
                    (x + 1, y - 1),
                ]:
                    if (
                        0 <= nx < len(data[0])
                        and 0 <= ny < len(data)
                        and normal_steps - (start_steps[y][x] + end_steps[ny][nx] + 2)
                        >= cheating_threshold
                    ):
                        cheats += 1

    return cheats


def solve_part2(data):  # solves the question
    cheating_threshold = 100
    end_steps = dijkstra_from_char(data, "E")
    start_steps = dijkstra_from_char(data, "S")
    start_loc = index_char(data, "S")
    normal_steps = end_steps[start_loc[1]][start_loc[0]]
    cheats = 0
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c != "#":
                for ox in range(-20, 21):
                    d = 20 - abs(ox)
                    for oy in range(-d, d + 1):
                        nx = x + ox
                        ny = y + oy
                        if (
                            0 <= nx < len(data[0])
                            and 0 <= ny < len(data)
                            and normal_steps
                            - (
                                start_steps[y][x]
                                + end_steps[ny][nx]
                                + abs(ox)
                                + abs(oy)
                            )
                            >= cheating_threshold
                        ):
                            cheats += 1

    return cheats


def main():
    lines = read_input(use_example=False)
    print(f"Part 1: {solve_part1(parse_input(lines))}")
    print()
    print(f"Part 2: {solve_part2(parse_input(lines))}")


if __name__ == "__main__":
    main()
