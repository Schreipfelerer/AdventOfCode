def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for line in lines:
        row = []
        for char in line:
            row.append(int(char))
        data.append(row)
    return data


def solve(data):  # solves the question
    vis_trees = set()
    for start_end in (False, True):
        for swap_xy in (False, True):
            for i in range(len(data)):
                biggest_tree = -1
                for j in range(len(data)):
                    x = len(data) - i - 1 if start_end else i
                    y = len(data) - j - 1 if start_end else j
                    if swap_xy:
                        x, y = y, x
                    if data[y][x] > biggest_tree:
                        biggest_tree = data[y][x]
                        vis_trees.add((x, y))
    xy = list(vis_trees)
    xy.sort()
    return len(vis_trees)


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
