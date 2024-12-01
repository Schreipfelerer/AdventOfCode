def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    return lines[0].rstrip("\n").split(",")


def solve(data):  # solves the question
    hash_sum = 0
    for string in data:
        hash_value = 0
        for char in string:
            hash_value += ord(char)
            hash_value *= 17
            hash_value %= 256
        hash_sum += hash_value
    return hash_sum


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
