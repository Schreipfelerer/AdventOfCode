def read_input(
    *,
    use_example=False,
) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc) as f:
        return f.read().split("\n")


def parse_input(lines):  # parses the input to the desired typ
    return [list(map(int, line)) for line in lines[:-1]]


def solve_part1(data):  # solves the question
    trailhead_scores = 0
    for y, datarow in enumerate(data):
        for x, datapoint in enumerate(datarow):
            if datapoint == 0:
                trailhead_scores += len(get_trailheads(data, x, y, 0))
    return trailhead_scores


def get_trailheads(data, x, y, h):
    if x < 0 or len(data[0]) <= x:
        return set()
    if y < 0 or len(data) <= y:
        return set()
    if data[y][x] != h:
        return set()
    if h == 9:
        return {(x, y)}
    trailheads = set()
    for x_off, y_off in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        trailheads = trailheads.union(get_trailheads(data, x + x_off, y + y_off, h + 1))

    return trailheads


def solve_part2(data):  # solves the question
    trailhead_scores = 0
    for y, datarow in enumerate(data):
        for x, datapoint in enumerate(datarow):
            if datapoint == 0:
                trailhead_scores += get_trailhead_score(data, x, y, 0)
    return trailhead_scores


def get_trailhead_score(data, x, y, h):
    if x < 0 or len(data[0]) <= x:
        return 0
    if y < 0 or len(data) <= y:
        return 0
    if data[y][x] != h:
        return 0
    if h == 9:
        return 1
    trailheads = 0
    for x_off, y_off in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        trailheads += get_trailhead_score(data, x + x_off, y + y_off, h + 1)

    return trailheads


def main():
    lines = read_input()
    data = parse_input(lines)
    print(f"Part 1: {solve_part1(data)}")
    print()
    print(f"Part 2: {solve_part2(data)}")


if __name__ == "__main__":
    main()
