#!/usr/bin/env python3
from itertools import batched


def read_input(
    *,
    use_example=False,
) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc) as f:
        return f.read().split("\n")


def parse_input(lines):  # parses the input to the desired typ
    return [
        [
            [int(x[2:]) for x in batch[0][10:].split(", ")],
            [int(x[2:]) for x in batch[1][10:].split(", ")],
            [int(x[2:]) for x in batch[2][7:].split(", ")],
        ]
        for batch in batched(lines[:-1], 4)
    ]


def solve_part1(data):  # solves the question
    tokens = 0
    for d in data:
        a, b, goal = d
        b_presses = 0
        for a_presses in range(goal[0] // a[0], -1, -1):
            while goal[0] > a[0] * a_presses + b[0] * b_presses:
                b_presses += 1
            if (
                goal[0] == a[0] * a_presses + b[0] * b_presses
                and goal[1] == a[1] * a_presses + b[1] * b_presses
            ):
                tokens += a_presses * 3 + b_presses

    return tokens


def solve_part2(data):  # solves the question
    tokens = 0
    for d in data:
        a, b, goal = d
        goal = [10000000000000 + g for g in goal] # 10000000000000
        dif = a[0]*b[1]-a[1]*b[0]

        a_p = int((goal[0] * b[1] - b[0] * goal[1]) / dif)
        b_p = int((a[0] * goal[1] - goal[0] * a[1]) / dif)
        if a_p * a[0] + b_p * b[0] == goal[0] and a_p * a[1] + b_p * b[1] == goal[1]:
            tokens += 3 * a_p + b_p
    return tokens


def main():
    lines = read_input(use_example=False)
    data = parse_input(lines)
    print(f"Part 1: {solve_part1(data)}")
    print()
    print(f"Part 2: {solve_part2(data)}")


if __name__ == "__main__":
    main()
