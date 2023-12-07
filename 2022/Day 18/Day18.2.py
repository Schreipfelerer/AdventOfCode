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
    air_trap = []
    for x in range(22):
        plane = []
        plane2 = []
        for y in range(22):
            row = []
            row2 = []
            for z in range(22):
                row.append(False)
                row2.append(True)
            plane.append(row)
            plane2.append(row2)
        scan.append(plane)
        air_trap.append(plane2)

    for point in data:
        scan[point[0]][point[1]][point[2]] = True

    # Scan for Air in 2D
    q = [(0, 0, 0)]
    visited = set(q)
    while q:
        p = q.pop(0)
        for offset in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            p_new = (p[0] + offset[0], p[1] + offset[1], p[2] + offset[2])
            if 0 <= p_new[0] <= 21 and 0 <= p_new[1] <= 21 and 0 <= p_new[2] <= 21:
                if p_new not in visited and not scan[p_new[0]][p_new[1]][p_new[2]]:
                    visited.add(p_new)
                    q.append(p_new)

    for p in visited:
        air_trap[p[0]][p[1]][p[2]] = False

    opensides = 0
    for point in data:
        for offset in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            x = point[0] + offset[0]
            y = point[1] + offset[1]
            z = point[2] + offset[2]
            if 0 <= x <= 21 and 0 <= y <= 21 and 0 <= z <= 21:
                opensides += 0 if air_trap[x][y][z] else 1
            else:
                opensides += 1
    return opensides


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
