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
    scenic_score_high = 0
    for x in range(1, len(data) - 1):
        for y in range(1, len(data) - 1):
            scenic_score = 1
            for swap in [False, True]:
                for negate in [False, True]:
                    x_off = -1 if negate else 1
                    y_off = 0
                    if swap:
                        x_off, y_off = y_off, x_off

                    x_pos = x + x_off
                    y_pos = y + y_off
                    see = 0
                    while 0 <= x_pos < len(data) and 0 <= y_pos < len(data):
                        see += 1
                        if data[y][x] <= data[y_pos][x_pos]:
                            break

                        x_pos += x_off
                        y_pos += y_off

                    scenic_score *= see

            scenic_score_high = max(scenic_score_high, scenic_score)
    return scenic_score_high


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
