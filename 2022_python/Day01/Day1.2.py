def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = []
    elf = []
    for line in lines:
        line = line.rstrip("\n")
        if line:
            elf.append(int(line))
        else:
            data.append(elf)
            elf = []
    data.append(elf)
    return data


def solve(data):  # solves the question
    max_cal = [0, 0, 0]
    for elf in data:
        if min(max_cal) < sum(elf):
            max_cal[max_cal.index(min(max_cal))] = sum(elf)
    return sum(max_cal)


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
