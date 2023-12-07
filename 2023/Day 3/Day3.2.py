def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    parts = []
    partnums = []
    for i, line in enumerate(lines):
        for y, char in enumerate(line.rstrip("\n")):
            if char in "0123456789":
                if y == 0 or line[y-1] not in "0123456789":
                    number = ""
                    while line[y] in "0123456789":
                        number += line[y]
                        y += 1
                    partnums.append((number, i, y-len(number)))
            elif char == "*":
                parts.append((i, y))
    return parts, partnums


def solve(data):  # solves the question#
    parts, partnums = data
    sol = 0
    for part in parts:
        neighbours = []
        for partnum in partnums:
            if part[0]-1 <= partnum[1] <= part[0]+1:
                if part[1]-1 <= partnum[2]+len(partnum[0])-1 and partnum[2] <= part[1]+1:
                    neighbours.append(partnum[0])
        if len(neighbours) == 2:
            sol += int(neighbours[0])* int(neighbours[1])
    return sol


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
