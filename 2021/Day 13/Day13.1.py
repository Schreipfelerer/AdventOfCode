def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    pos_s = []
    folds = []
    is_done = False
    for line in lines:
        if is_done:
            folds.append(line.rstrip("\n").lstrip("fold along").split("="))
            folds[-1][-1] = int(folds[-1][-1])
        elif line == "\n":
            is_done = True
        else:
            pos_a = []
            for pos in line.rstrip("\n").split(","):
                pos_a.append(int(pos))
            pos_s.append(pos_a)
    return pos_s, folds


def solve(data):  # solves the question
    pos, folds = data

    dots = []
    for i in range(1350):
        row = []
        for j in range(1350):
            if list((i, j)) in pos:
                row.append(1)
            else:
                row.append(0)
        dots.append(row)

    fold = folds[0]
    if fold[0] == "x":
        for i in range(0, fold[1]):
            if 1350 > (fold[1]*2)-i:
                for j in range(1350):
                    if dots[i][j] == 0:
                        dots[i][j] = dots[(fold[1]*2)-i][j]
        for i in range(fold[1], 1350):
            for j in range(1350):
                dots[i][j] = 0
    else:
        for i in range(0, fold[1]):
            if 1350 > (fold[1] * 2) - i:
                for j in range(1350):
                    if dots[j][i] == 0:
                        dots[j][i] = dots[j][(fold[1]*2)-i]
        for i in range(fold[1], 1350):
            for j in range(1350):
                dots[j][i] = 0
    score = 0
    for row in dots:
        score += sum(row)
    return score


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
