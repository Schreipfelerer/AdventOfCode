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
        line2 = line
        while True:
            if line2.startswith(("1", "one")):
                number += 10
                break
            elif line2.startswith(("2", "two")):
                number += 20
                break
            elif line2.startswith(("3", "three")):
                number += 30
                break
            elif line2.startswith(("4", "four")):
                number += 40
                break
            elif line2.startswith(("5", "five")):
                number += 50
                break
            elif line2.startswith(("6", "six")):
                number += 60
                break
            elif line2.startswith(("7", "seven")):
                number += 70
                break
            elif line2.startswith(("8", "eight")):
                number += 80
                break
            elif line2.startswith(("9", "nine")):
                number += 90
                break
            else:
                line2 = line2[1:]
        while True:
            if line.endswith(("1", "one")):
                number += 1
                break
            elif line.endswith(("2", "two")):
                number += 2
                break
            elif line.endswith(("3", "three")):
                number += 3
                break
            elif line.endswith(("4", "four")):
                number += 4
                break
            elif line.endswith(("5", "five")):
                number += 5
                break
            elif line.endswith(("6", "six")):
                number += 6
                break
            elif line.endswith(("7", "seven")):
                number += 7
                break
            elif line.endswith(("8", "eight")):
                number += 8
                break
            elif line.endswith(("9", "nine")):
                number += 9
                break
            else:
                line = line[:-1]
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
