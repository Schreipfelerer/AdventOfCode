def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    return lines


def solve(data):  # solves the question
    snafu_dec = 0
    for num in data:
        power = 0
        for c in num[::-1]:
            if c == "-":
                c = "-1"
            if c == "=":
                c = "-2"
            snafu_dec += (5 ** power) * int(c)
            power += 1

    digits = []
    while snafu_dec:
        digits.append(int(snafu_dec % 5))
        snafu_dec //= 5

    for i, d in enumerate(digits):
        if d > 2:
            digits[i] = d - 5
            if i + 1 == len(digits):
                digits.append(0)
            digits[i + 1] += 1

    return "".join([str(i) for i in digits[::-1]]).replace("-2", "=").replace("-1", "-")


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
