#!/usr/bin/env python3
def read_input(
    *,
    use_example=False,
) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc) as f:
        return f.read().split("\n")


def parse_input(lines):  # parses the input to the desired typ
    return [int(x) for x in lines[:-2]]


def next_secret(secret):
    secret = (secret * 64) ^ secret
    secret %= 16777216
    secret = (secret // 32) ^ secret
    secret %= 16777216
    secret = (secret * 2048) ^ secret
    secret %= 16777216
    return secret



def solve_part1(data):  # solves the question
    score = 0
    for number in data:
        for _ in range(2000):
            number = next_secret(number)
        score += number
    return score


def solve_part2(data):  # solves the question
    return data


def main():
    lines = read_input(use_example=False)
    print(f"Part 1: {solve_part1(parse_input(lines))}")
    print()
    print(f"Part 2: {solve_part2(parse_input(lines))}")


if __name__ == "__main__":
    main()
