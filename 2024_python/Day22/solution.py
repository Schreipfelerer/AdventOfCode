#!/usr/bin/env python3
def read_input(
    *,
    use_example=False,
) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example2.txt" if use_example else "input.txt"
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
            number = next_secret(number)  # noqa: PLW2901
        score += number
    return score


def solve_part2(data):  # solves the question
    changes = []
    prizes = []
    for number in data:
        c = []
        p = []
        for _ in range(2000):
            next_number = next_secret(number)
            p.append(next_number%10)
            c.append((next_number%10)-(number%10))
            number = next_number  # noqa: PLW2901
        p = p[3:]
        sliding_window = [(c[i], c[i+1], c[i+2], c[i+3]) for i in range(len(c)-3)]
        changes.append(sliding_window)
        prizes.append(p)

    best_bananas = 0
    d = {xs for x in changes for xs in x}
    for j, combo in enumerate(d):
        print(f"starting ({j}/{len(d)})")
        bananas = 0
        for i in range(len(data)):
            index = next((ind for ind, x in enumerate(changes[i]) if x == combo), -1)
            if index != -1:
                bananas += prizes[i][index]
        best_bananas = max(bananas, best_bananas)
    return best_bananas


def main():
    lines = read_input(use_example=False)
    print(f"Part 1: {solve_part1(parse_input(lines))}")
    print()
    print(f"Part 2: {solve_part2(parse_input(lines))}")


if __name__ == "__main__":
    main()
