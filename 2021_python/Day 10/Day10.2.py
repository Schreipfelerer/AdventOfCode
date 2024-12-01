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
    scores = []
    for line in data:
        for i in range(0, len(line), 2):
            line = line.replace("()", "")
            line = line.replace("{}", "")
            line = line.replace("[]", "")
            line = line.replace("<>", "")
        if line:
            points = 0
            stop = False
            for char in ">]})":
                if char in line:
                    stop = True
            if not stop:
                for char in line[::-1]:
                    points *= 5
                    if char == "(":
                        points += 1
                    if char == "[":
                        points += 2
                    if char == "{":
                        points += 3
                    if char == "<":
                        points += 4
                scores.append(points)
    scores.sort()
    return scores[int((len(scores) - 1) / 2)]


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
