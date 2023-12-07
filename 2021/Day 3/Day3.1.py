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
        for i, bit in enumerate(line.rstrip("\n")):
            if len(data) < i+1:
                data.append([])
            data[i].append(bit)
    return data


def solve(data):  # solves the question
    gamma = ""
    epsilon = ""
    for position in data:
        gamma = gamma + str(max(set(position), key=position.count))
        epsilon = epsilon + str(min(set(position), key=position.count))
    powercon = int(gamma, 2) * int(epsilon, 2)
    return powercon


def main():
    lines = readInput(False)
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
