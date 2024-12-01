from typing import List, Tuple


def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines: List[str]):  # parses the input to the desired typ
    data = []
    for line in lines:
        data.append((line.split()[0], int(line.split()[1])))
    return data


def solve(data: List[Tuple[str, int]]):  # solves the question
    pos = [0, 0]
    for movement in data:
        if movement[0] == "forward":
            pos[0] += movement[1]
        if movement[0] == "down":
            pos[1] += movement[1]
        if movement[0] == "up":
            pos[1] -= movement[1]
    return pos[0] * pos[1]


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
