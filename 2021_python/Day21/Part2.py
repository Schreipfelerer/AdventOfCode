def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    p1 = int(lines[0].split(": ")[1].rstrip("\n"))
    p2 = int(lines[1].split(": ")[1].rstrip("\n"))
    return p1, p2


def solve(data):  # solves the question
    p1, p2 = data
    s1, s2 = 0, 0
    last_roll = 0
    turn_p1 = True
    while s1 < 1000 and s2 < 1000:
        roll = last_roll * 3 + 6 % 10
        last_roll += 3
        if turn_p1:
            p1 = ((p1 + roll - 1) % 10) + 1
            s1 += p1
        else:
            p2 = ((p2 + roll - 1) % 10) + 1
            s2 += p2
        turn_p1 = not turn_p1
    return min(s1, s2) * last_roll


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
