#!/usr/bin/env python3
def read_input(
    *,
    use_example=False,
) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc) as f:
        return f.read().split("\n\n")


def parse_input(lines):  # parses the input to the desired typ
    keys, locks = [], []
    lines = [line.split("\n") for line in lines]
    for image in lines[:-1]:
        pins = [[row[i] for row in image].count("#") - 1 for i in range(5)]
        if image[0] == "#####":
            locks.append(pins)
        else:
            keys.append(pins)
    return keys, locks


def solve_part1(data):  # solves the question
    keys, locks = data
    number = 0
    for key in keys:
        for lock in locks:
            fit = True
            for i in range(5):
                if key[i]+lock[i] > 5:
                    fit = False
            if fit:
                number += 1
    return number


def main():
    lines = read_input(use_example=False)
    print(f"Part 1: {solve_part1(parse_input(lines))}")


if __name__ == "__main__":
    main()
