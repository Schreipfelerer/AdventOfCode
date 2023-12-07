def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    data = []
    s = None
    e = None
    for line in lines:
        row = []
        for char in line:
            if char == "S":
                char = "a"
                s = (len(data), len(row))
            elif char == "E":
                char = "z"
                e = (len(data), len(row))
            row.append(ord(char)-97)
        data.append(row)
    return s, e, data


def solve(data):  # solves the question
    _, signal, grid = data
    steps = []
    for _ in range(len(grid)):
        step_row = []
        for _ in range(len(grid[0])):
            step_row.append(1000000)
        steps.append(step_row)

    steps[signal[0]][signal[1]] = 0
    queue = [signal]
    while queue:
        x, y = queue.pop(0)
        elev = grid[x][y]
        step = steps[x][y]
        for change in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x + change[0] < len(grid) and 0 <= y + change[1] < len(grid[0]):
                if elev-1 <= grid[x + change[0]][y + change[1]] and steps[x + change[0]][y + change[1]] == 1000000:
                    steps[x + change[0]][y + change[1]] = step + 1
                    queue.append(((x + change[0]), (y + change[1])))

    steps_to_a = 100000
    for x, row in enumerate(grid):
        for y, char in enumerate(row):
            if char == 0:
                steps_to_a = min(steps_to_a, steps[x][y])
    return steps_to_a


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
