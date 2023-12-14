def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for row in lines:
        data_row = []
        for char in row.rstrip("\n"):
            data_row.append(char)
        data.append(data_row)
    return data


def solve(data):  # solves the question
    for y in range(len(data[0])):
        for i in range(1, len(data)):
            if data[i][y] == "O":
                empty_rows = 1
                while data[i - empty_rows][y] == "." and i - empty_rows >= 0:
                    empty_rows += 1

                if empty_rows > 1:
                    data[i][y] = "."
                    data[i - empty_rows + 1][y] = "O"

    load = 0
    for i in range(len(data)):
        load += (len(data) - i) * data[i].count("O")
    return load


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
