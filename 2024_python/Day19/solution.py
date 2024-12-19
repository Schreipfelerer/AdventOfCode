#!/usr/bin/env python3
def read_input(
    *,
    use_example=False,
) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc) as f:
        return f.read().split("\n")


def parse_input(lines):  # parses the input to the desired typ
    parts = "\n".join(lines[:-2]).split("\n\n")
    return parts[0].split(", "), parts[1].split("\n")


def solve_part1(data):  # solves the question
    towles, patterns = data
    possible = 0
    for p in patterns:
        if get_possible_towles(p, towles) > 0:
            possible += 1
    return possible



def solve_part2(data):  # solves the question
    towles, patterns = data
    possible = 0
    for p in patterns:
        possible += get_possible_towles(p, towles)
    return possible


rem = {}
def get_possible_towles(p, towles):
    if not p:
        return 1
    if p in rem:
        return rem[p]
    possible = 0
    for t in towles:
        if p.startswith(t):
            possible += get_possible_towles(p[len(t):], towles)
    rem[p] = possible
    return possible



def main():
    lines = read_input(use_example=False)
    print(f"Part 1: {solve_part1(parse_input(lines))}")
    print()
    print(f"Part 2: {solve_part2(parse_input(lines))}")


if __name__ == "__main__":
    main()
