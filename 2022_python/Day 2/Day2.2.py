def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for line in lines:
        data.append(line.split(" "))
        data[-1][0] = ord(data[-1][0]) - 64
        data[-1][1] = ord(data[-1][1].replace("X", "A").replace("Y", "B").replace("Z", "C")) - 64
    return data


def solve(data):  # solves the question
    score = 0
    for game in data:
        score += (game[1] - 1) * 3
        score += ((game[0] - 3 + game[1]) % 3) + 1
    return score


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
