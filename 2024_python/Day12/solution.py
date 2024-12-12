def read_input(
    *,
    use_example=False,
) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc) as f:
        return f.read().split("\n")


def parse_input(lines):  # parses the input to the desired typ
    return lines[:-1]


def grow_part(lines, x_start, y_start):
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


def solve_part1(data):  # solves the question
    parts = []
    price = 0
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if all([(x, y) not in p for p in parts]):
                part, perimeter, area = grow_part(data, x, y)
                parts.append(part)
                price += perimeter*area
    return price



def solve_part2(data):  # solves the question
    return len(data)



def main():
    lines = read_input(use_example=True)
    data = parse_input(lines)
    print(f"Part 1: {solve_part1(data)}")
    print()
    print(f"Part 2: {solve_part2(data)}")


if __name__ == "__main__":
    main()
