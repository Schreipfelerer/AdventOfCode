def readInput(
    *,
    use_example=False,
) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc) as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for line in lines:
        if not line:
            continue
        line = line.split(" ")
        data.append(list(map(int, line)))
    return data


def solvePart1(data):  # solves the question
    safe_num = 0
    for d in data:
        if all(0 < x[0] - x[1] < 4 for x in zip(d[:-1], d[1:])) or all(
            0 < x[1] - x[0] < 4 for x in zip(d[:-1], d[1:])
        ):
            safe_num += 1
    return safe_num


def solvePart2(data):  # solves the question
    safe_num = 0
    for d in data:
        if d[0] < d[-1]:
            d = d[::-1]
        bool_list = [0 < x[0] - x[1] < 4 for x in zip(d[:-1], d[1:])]
        true_count = bool_list.count(True)
        if true_count == len(bool_list):
            safe_num += 1
            continue

        index_false = bool_list.index(False)
        d_1 = d[:index_false] + d[index_false + 1 :]
        d_2 = d[: index_false + 1] + d[index_false + 2 :]

        if all(0 < x[0] - x[1] < 4 for x in zip(d_1[:-1], d_1[1:])) or all(
            0 < x[0] - x[1] < 4 for x in zip(d_2[:-1], d_2[1:])
        ):
            safe_num += 1
    return safe_num


def main():
    lines = readInput()
    data = parseInput(lines)
    print(f"Part 1: {solvePart1(data)}")
    print()
    print(f"Part 2: {solvePart2(data)}")


if __name__ == "__main__":
    main()
