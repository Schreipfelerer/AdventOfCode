def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for line in lines:
        data.append(line.split(" "))
        if data[-1][0] == "addx":
            data[-1][1] = int(data[-1][1])
    return data


def solve(data):  # solves the question
    cycle = 1
    printstr = ""
    reg = 1
    ip = 0
    wait = False
    addto = 0
    while ip < len(data):
        if not wait:
            reg += addto
            addto = 0
            if data[ip][0] == "addx":
                addto = data[ip][1]
                wait = True
            ip += 1
        else:
            wait = False

        printstr += "#" if 1 >= reg - (cycle - 1) % 40 >= -1 else "."

        if cycle % 40 == 0:
            printstr += "\n"
        cycle += 1
    return printstr


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
