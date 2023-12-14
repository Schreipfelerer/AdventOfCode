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
            if pattern[i] == pattern[i+1]:
                offset = 1
                is_true_reflection = True
                while i-offset >= 0 and i+offset+1 < len(pattern) and is_true_reflection:
                    is_true_reflection = pattern[i-offset] == pattern[i+offset+1]
                    offset += 1
                if is_true_reflection:
                    solution += (i+1)*100

        for i in range(len(pattern[0])-1):
            if [x[i] for x in pattern] == [x[i+1] for x in pattern]:
                offset = 1
                is_true_reflection = True
                while i-offset >= 0 and i+offset+1 < len(pattern[0]) and is_true_reflection:
                    is_true_reflection = [x[i-offset] for x in pattern] == [x[i+offset+1] for x in pattern]
                    offset += 1
                if is_true_reflection:
                    solution += (i+1)
    return solution


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
