def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for line in lines:
        data.append([int(num) for num in line.split("x")])
    return data


def solve(data):  # solves the question
    paper = 0
    for present in data:
        paper += 2*(present[0]*present[1]+present[0]*present[2]+present[1]*present[2])
        paper += min(present[0]*present[1], present[0]*present[2], present[1]*present[2])
    return paper


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
