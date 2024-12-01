def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = []

    for line in lines:
        col = line.rstrip("\n").split(" | ")
        col[0] = col[0].split(" ")
        col[1] = col[1].split(" ")
        data.append(col)

    return data


def subset(s1, s2):
    for s in s1:
        if s in s2:
            continue
        return False

    return True


def sub(s1, s2):
    for s in s2:
        s1 = s1.replace(s, "")
    return s1


def solve(data):  # solves the question
    num = 0
    for line in data:
        in_order = [None, None, None, None, None, None, None, None, None, None]
        for digit in line[0]:
            if len(digit) == 2:
                in_order[1] = "".join(sorted(digit))
            if len(digit) == 4:
                in_order[4] = "".join(sorted(digit))
        for digit in line[0]:
            if len(digit) == 3:
                in_order[7] = "".join(sorted(digit))
            if len(digit) == 7:
                in_order[8] = "".join(sorted(digit))
            if len(digit) == 6:
                if subset(in_order[1], digit):
                    if subset(in_order[4], digit):
                        in_order[9] = "".join(sorted(digit))
                    else:
                        in_order[0] = "".join(sorted(digit))
                else:
                    in_order[6] = "".join(sorted(digit))
            if len(digit) == 5:
                if subset(in_order[1], digit):
                    in_order[3] = "".join(sorted(digit))
                else:
                    if subset(sub(in_order[4], in_order[1]), digit):
                        in_order[5] = "".join(sorted(digit))
                    else:
                        in_order[2] = "".join(sorted(digit))
        out = 0
        for digit in line[1]:
            out *= 10
            out += in_order.index("".join(sorted(digit)))
        num += out

    return num


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
