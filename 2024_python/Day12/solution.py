def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example3.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    return lines[:-1]


def growPart(lines, x_start, y_start):
    part = [(x_start, y_start)]
    char = lines[y_start][x_start]
    area = 1
    perimeter = 4
    next_part = {(x_start+1, y_start), (x_start-1, y_start), (x_start, y_start+1), (x_start, y_start-1)}
    while next_part:
        x, y = next_part.pop()
        if x < 0 or y < 0 or x >= len(lines[0]) or y >= len(lines):
            continue
        if lines[y][x] != char:
            continue
        for offset in [(1,0), (0,1), (-1,0), (0,-1)]:
            x_off = x + offset[0]
            y_off = y + offset[1]
            if (x_off, y_off) in part:
                perimeter -= 1
            else:
                next_part.add((x_off, y_off))
                perimeter += 1
        area += 1
        part.append((x, y))
    return part, perimeter, area


def solvePart1(data):  # solves the question
    parts = []
    price = 0
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if all([(x, y) not in p for p in parts]):
                part, perimeter, area = growPart(data, x, y)
                parts.append(part)
                price += perimeter*area
    return price



def solvePart2(data):  # solves the question
    return len(data)



def main():
    lines = readInput(use_example=False)
    data = parseInput(lines)
    print(f"Part 1: {solvePart1(data)}")
    print("")
    print(f"Part 2: {solvePart2(data)}")


if __name__ == "__main__":
    main()
