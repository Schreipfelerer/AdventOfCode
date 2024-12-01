def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for line in lines:
        data.append([int(elem) for elem in line.split(",")])
    return data


def solve(data):  # solves the question
    scan = []
    for x in range(22):
        plane = []
        for y in range(22):
            row = []
            for z in range(22):
                row.append(False)
            plane.append(row)
        scan.append(plane)

    for point in data:
        scan[point[0]][point[1]][point[2]] = True

    opensides = 0
    for point in data:
        for offset in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            x = point[0] + offset[0]
            y = point[1] + offset[1]
            z = point[2] + offset[2]
            if 0 <= x <= 21 and 0 <= y <= 21 and 0 <= z <= 21:
                opensides += 0 if scan[x][y][z] else 1
            else:
                opensides += 1
    return opensides


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
