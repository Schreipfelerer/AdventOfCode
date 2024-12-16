#!/usr/bin/env python3
def read_input(
        *,
        use_example=False,
) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc) as f:
        return f.read().split("\n")


def parse_input(lines):  # parses the input to the desired typ
    return lines[:-1]


def solve_part1(data):  # solves the question
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = [(1, len(data) - 2, 0, 0)]
    cheapest = {}
    while queue:
        x, y, d, c = queue.pop(0)
        if (x, y, d) in cheapest and cheapest[(x, y, d)] < c:
            continue
        cheapest[(x, y, d)] = c
        dx, dy = directions[d]
        if data[y + dy][x + dx] != "#":
            queue.append((x + dx, y + dy, d, c + 1))
        queue += [(x, y, (d + 1) % 4, c + 1000), (x, y, (d - 1) % 4, c + 1000)]
    return min(cheapest[(len(data) - 2, 1, 0)], cheapest[(len(data) - 2, 1, 3)]), cheapest


def solve_part2(data, cost):  # solves the question
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    best_spots = set()
    d = 0 if cost[(len(data) - 2, 1, 0)] < cost[(len(data) - 2, 1, 3)] else 3
    queue = [(len(data) - 2, 1, d)]
    while queue:
        x, y, d = queue.pop(0)
        best_spots.add((x, y))
        for t in [(x, y, (d+1)%4), (x, y, (d-1)%4), (x-directions[d][0], y-directions[d][1], d)]:
            if t in cost and cost[t] < cost[(x, y, d)]:
                queue.append(t)
    return len(best_spots)


def main():
    lines = read_input(use_example=False)
    solve, cheapest = solve_part1(parse_input(lines))
    print(f"Part 1: {solve}")
    print()
    print(f"Part 2: {solve_part2(parse_input(lines), cheapest)}")


if __name__ == "__main__":
    main()
