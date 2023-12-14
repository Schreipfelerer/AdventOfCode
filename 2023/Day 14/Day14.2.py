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
    past_positions = []
    cycle = 0
    while cycle < 1_000_000_000:
        for offset in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            i_range = range(len(data)-1, -1, -1) if offset[0] == 1 else range(len(data))
            for i in i_range:
                y_range = range(len(data[0])-1, -1, -1) if offset[1] == 1 else range(len(data[0]))
                for y in y_range:
                    if data[i][y] == "O":
                        empty_rows = 1
                        while (0 <= i+empty_rows*offset[0] < len(data)
                               and 0 <= y+empty_rows*offset[1] < len(data[0])
                               and data[i + empty_rows * offset[0]][y + empty_rows * offset[1]] == "."):
                            empty_rows += 1

                        empty_rows -= 1
                        if empty_rows:
                            data[i][y] = "."
                            data[i + empty_rows * offset[0]][y + empty_rows * offset[1]] = "O"
        data_to_row = "".join(["".join(row) for row in data])
        if data_to_row in past_positions:
            index = past_positions.index(data_to_row)
            cycle_length = len(past_positions)-index
            cycle += (999_999_999-cycle)//cycle_length*cycle_length
            past_positions = []
        else:
            past_positions.append(data_to_row)
        cycle += 1


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
