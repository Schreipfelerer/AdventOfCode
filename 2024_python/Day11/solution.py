def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    data = list(map(int, lines[0].split(" ")))
    return data


def solvePart1(data):  # solves the question
    for _ in range(25):
        new_data = []
        for d in data:
            str_d = str(d)
            if d == 0:
                new_data.append(1)
            elif len(str_d) % 2 == 0:
                new_data.append(int(str_d[:len(str_d) // 2]))
                new_data.append(int(str_d[len(str_d) // 2:]))
            else:
                new_data.append(d*2024)
        data = new_data
    return len(data)



def solvePart2(data):  # solves the question
    for _ in range(75):
        print(_)
        new_data = []
        for d in data:
            str_d = str(d)
            if d == 0:
                new_data.append(1)
            elif len(str_d) % 2 == 0:
                new_data.append(int(str_d[:len(str_d) // 2]))
                new_data.append(int(str_d[len(str_d) // 2:]))
            else:
                new_data.append(d * 2024)
        data = new_data
    return len(data)



def main():
    lines = readInput()
    data = parseInput(lines)
    print(f"Part 1: {solvePart1(data)}")
    print("")
    print(f"Part 2: {solvePart2(data)}")


if __name__ == "__main__":
    main()
