def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for num in lines[0].rstrip("\n").split(","):
        data.append(int(num))
    return data


def solve(data):  # solves the question
    for i in range(80):
        for j, fish in enumerate(data):
            if fish == 0:
                data[j] = 7
                data.append(9)
            data[j] -= 1
        print(f"Done with day{i}")
    return len(data)


def main():
    lines = readInput(False)
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
