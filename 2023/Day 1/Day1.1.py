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
        number = 0
        for char in line:
            if char in "0123456789":
                number += 10*int(char)
                break
        for char in line[::-1]:
            if char in "0123456789":
                number += int(char)
                break
        data.append(number)
    return data


def solve(data):  # solves the question
    return sum(data)


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
