def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for line in lines:
        data.append([int(line.split("x=")[1].split(",")[0]), int(line.split("y=")[1].split(":")[0]),
                     int(line.split("x=")[2].split(",")[0]), int(line.split("y=")[2])])
    return data


def solve(data):  # solves the question
    y_of_interest = 2000000
    notpos = set()
    for sensor in data:
        md = get_md(sensor[0], sensor[1], sensor[2], sensor[3])
        dif = md - abs(sensor[1] - y_of_interest)
        for i in range(dif+1):
            notpos.add(sensor[0] + i)
            notpos.add(sensor[0] - i)

    for sensor in data:
        if sensor[3] == y_of_interest:
            if sensor[2] in notpos:
                notpos.remove(sensor[2])

    return len(notpos)


def get_md(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
