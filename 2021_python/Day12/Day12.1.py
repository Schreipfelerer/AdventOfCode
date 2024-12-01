def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for line in lines:
        data.append(line.rstrip("\n").split("-"))
    return data


def solve(data):  # solves the question
    paths = findPaths("start", [], data)
    return paths


def findPaths(point: str, visited, cons):
    if point == "end":
        return 1
    if point in visited:
        return 0

    neighbours = []
    for path in cons:
        if point in path:
            if point == path[0]:
                neighbours.append(path[1])
            else:
                neighbours.append(path[0])

    if point.lower() == point:
        visited.append(point)

    paths = []
    for neighbour in neighbours:
        kek = findPaths(neighbour, visited[:], cons)
        if kek:
            paths.append(kek)
    return sum(paths)


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
