def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for kekw in lines[0].rstrip("\n").lstrip("target area: ").split(", "):
        row = []
        for dat in kekw.split("=")[1].split(".."):
            row.append(int(dat))
        data.append(row)

    return data


def solve(data):  # solves the question
    difs = 0
    min_y = data[1][0]
    max_y = abs(data[1][0]) + -1
    min_x = 0
    max_x = data[0][1]
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            vel_x = x
            vel_y = y
            pos_y = 0
            pos_x = 0
            while pos_x <= data[0][1] and pos_y >= data[1][0]:
                pos_x += vel_x
                pos_y += vel_y
                if data[0][0] <= pos_x <= data[0][1] and data[1][0] <= pos_y <= data[1][1]:
                    difs += 1
                    pos_x = data[0][1]+1
                vel_y -= 1
                if vel_x < 0:
                    vel_x += 1
                if vel_x > 0:
                    vel_x -= 1
    return difs


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
