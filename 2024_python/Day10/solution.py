def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for line in lines[:-1]:
        data.append(list(map(int, line)))
    return data


def solvePart1(data):  # solves the question
    trailhead_scores = 0
    for y, datarow in enumerate(data):
        for x, datapoint in enumerate(datarow):
            if datapoint == 0:
                trailhead_scores += len(getTrailheads(data, x, y, 0))
    return trailhead_scores

def getTrailheads(data, x, y, h):
    if 0 > x or len(data[0]) <= x:
        return set()
    if 0 > y or len(data) <= y:
        return set()
    if data[y][x] != h:
        return set()
    if h == 9:
        return {(x, y)}
    trailheads = set()
    for (x_off, y_off) in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        trailheads = trailheads.union(getTrailheads(data, x + x_off, y + y_off, h+1))

    return trailheads


def solvePart2(data):  # solves the question
    trailhead_scores = 0
    for y, datarow in enumerate(data):
        for x, datapoint in enumerate(datarow):
            if datapoint == 0:
                trailhead_scores += getTrailheadsScore(data, x, y, 0)
    return trailhead_scores


def getTrailheadsScore(data, x, y, h):
    if 0 > x or len(data[0]) <= x:
        return 0
    if 0 > y or len(data) <= y:
        return 0
    if data[y][x] != h:
        return 0
    if h == 9:
        return 1
    trailheads = 0
    for (x_off, y_off) in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        trailheads += getTrailheadsScore(data, x + x_off, y + y_off, h+1)

    return trailheads


def main():
    lines = readInput()
    data = parseInput(lines)
    print(f"Part 1: {solvePart1(data)}")
    print("")
    print(f"Part 2: {solvePart2(data)}")


if __name__ == "__main__":
    main()
