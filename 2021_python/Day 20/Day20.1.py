def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    ieas = lines[0].rstrip("\n")
    lines = lines[2:]
    data = [("." * (len(lines[0]) + 3)), "." * (len(lines[0]) + 3)]
    for line in lines:
        data.append("." + "." + line.rstrip("\n") + "." + ".")
    data.append(len(data[0]) * ".")
    data.append(len(data[0]) * ".")
    return ieas, data


def solve(data):  # solves the question
    ieas, data = data
    for times in range(2):
        new_data = []
        for x in range(len(data)):
            new_line = ""
            for y in range(len(data[x])):
                binary_s = ""
                for x_off in range(-1, 2):
                    for y_off in range(-1, 2):
                        if 0 <= x + x_off < len(data) and 0 <= y + y_off < len(data[x]):
                            binary_s = binary_s + data[x + x_off][y + y_off]
                        else:
                            if ieas[0] == "." or times % 2 == 0:
                                binary_s = binary_s + "."
                            else:
                                binary_s = binary_s + "#"
                binary = int(binary_s.replace(".", "0").replace("#", "1"), 2)
                new_line = new_line + ieas[binary]
            new_data.append(new_line)
        data = new_data

    print(data)
    num = 0
    for line in data:
        num += line.count("#")
    return num


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
