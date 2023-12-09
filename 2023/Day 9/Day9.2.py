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
        data.append([int(x) for x in line.rstrip("\n").split( )])
    return data


def solve(data):  # solves the question
    solution = 0
    for history in data:
        history = [history]
        while any(history[-1]):
            history.append([history[-1][i+1]-history[-1][i] for i in range(0, len(history[-1])-1)])
        for i in range(len(history)-2, -1, -1):
            history[i].insert(0, history[i][0]-history[i+1][0])
        solution += history[0][0]
    return solution


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
