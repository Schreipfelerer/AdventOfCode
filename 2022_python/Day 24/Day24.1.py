def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    width = len(lines[0])
    hight = len(lines)
    up = [[x, y] for x in range(len(lines)) for y in range(len(lines[x])) if lines[x][y] == "^"]
    down = [[x, y] for x in range(len(lines)) for y in range(len(lines[x])) if lines[x][y] == "v"]
    right = [[x, y] for x in range(len(lines)) for y in range(len(lines[x])) if lines[x][y] == ">"]
    left = [[x, y] for x in range(len(lines)) for y in range(len(lines[x])) if lines[x][y] == "<"]
    return width, hight, up, down, right, left


def solve(data):  # solves the question
    width, hight, up, down, right, left = data
    posi = {(0, 1)}
    minute = 0
    while (hight - 1, width - 2) not in posi:
        minute += 1
        for p in up:
            p[0] -= 1
            if p[0] == 0:
                p[0] = hight - 2
        for p in down:
            p[0] += 1
            if p[0] == hight - 1:
                p[0] = 1
        for p in right:
            p[1] += 1
            if p[1] == width - 1:
                p[1] = 1
        for p in left:
            p[1] -= 1
            if p[1] == 0:
                p[1] = width - 2

        bliz = up + down + right + left
        new_pos = set()
        for p in posi:
            for offset in ((1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)):
                x = p[0] + offset[0]
                y = p[1] + offset[1]
                if (0 < x < hight - 1 and 0 < y < width - 1) or (x == 0 and y == 1) or (
                        x == hight - 1 and y == width - 2):
                    if [x, y] not in bliz:
                        new_pos.add((x, y))

        posi = new_pos

    return minute


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
