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
            elif char != ".":
                parts.append((i, y))
    return parts, partnums


def solve(data):  # solves the question#
    parts, partnums = data
    sol = 0
    for partnum in partnums:
        is_neighbour = False
        for y in range(partnum[1]-1, partnum[1]+2):
            for x in range(partnum[2]-1, partnum[2]+1+len(partnum[0])):
                if (y, x) in parts:
                    is_neighbour = True
        if is_neighbour:
            sol += int(partnum[0])
    return sol


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
