def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = []
    pattern = []
    for line in lines:
        line = line.rstrip("\n")
        if line:
            pattern.append(line)
        else:
            data.append(pattern)
            pattern = []
    data.append(pattern)
    return data


def solve(data):  # solves the question
    solution = 0
    for pattern in data:
        for i, row in enumerate(pattern[:-1]):
            string1 = pattern[i]
            string2 = pattern[i + 1]
            difference = 0
            for y in range(len(string1)):
                difference += 1 if string1[y] != string2[y] else 0
            offset = 1
            while i - offset >= 0 and i + offset + 1 < len(pattern) and difference < 2:
                for y in range(len(string1)):
                    difference += 1 if pattern[i - offset][y] != pattern[i + offset + 1][y] else 0
                offset += 1
            if difference == 1:
                solution += (i + 1) * 100

        for i in range(len(pattern[0]) - 1):
            string1 = [x[i] for x in pattern]
            string2 = [x[i + 1] for x in pattern]
            difference = 0
            for y in range(len(string1)):
                difference += 1 if string1[y] != string2[y] else 0
            offset = 1
            while i - offset >= 0 and i + offset + 1 < len(pattern[0]) and difference < 2:
                for y in range(len(string1)):
                    difference += 1 if pattern[y][i - offset] != pattern[y][i + offset + 1] else 0
                offset += 1
            if difference == 1:
                solution += i + 1
    return solution


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
