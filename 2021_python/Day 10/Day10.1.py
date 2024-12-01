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
        data.append(line.rstrip("\n"))

    return data


def solve(data):  # solves the question
    score = 0
    for line in data:
        for i in range(0, len(line), 2):
            line = line.replace("()", "")
            line = line.replace("{}", "")
            line = line.replace("[]", "")
            line = line.replace("<>", "")
        if line:
            for char in line:
                if char == ")":
                    score += 3
                    break
                if char == "]":
                    score += 57
                    break
                if char == "}":
                    score += 1197
                    break
                if char == ">":
                    score += 25137
                    break
    return score


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
