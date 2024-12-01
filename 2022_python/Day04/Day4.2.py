def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for line in lines:
        da = []
        for assignment in line.split(","):
            d = []
            for section in assignment.split("-"):
                d.append(int(section))
            da.append(d)
        data.append(da)
    return data


def solve(data):  # solves the question
    counter = 0
    for line in data:
        task1 = set(range(line[0][0], line[0][1] + 1))
        task2 = set(range(line[1][0], line[1][1] + 1))
        if not task1.isdisjoint(task2):
            counter += 1
    return counter


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
