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
    ppoints = []  # derterminine possible points where outerlines of 4 diamonds intersect
    lines = []
    for report in data:
        md = get_md(report[0], report[1], report[2], report[3]) + 1
        points = [[report[0], report[1] + md], [report[0] + md, report[1]],
                  [report[0], report[1] - md], [report[0] - md, report[1]]]
        for i in range(3, -1, -1):
            lines.append([points[i], points[i - 1]])

    for i in range(len(lines) - 4):
        for j in range(i + 1, len(lines), 2):
            if j - i != j % 4:
                x1 = lines[i][0][0]
                y1 = lines[i][0][1]
                x2 = lines[i][1][0]
                y2 = lines[i][1][1]
                x3 = lines[j][0][0]
                y3 = lines[j][0][1]
                x4 = lines[j][1][0]
                y4 = lines[j][1][1]

                if x1 > x2:  # Smaller x first
                    x1, x2 = x2, x1
                    y1, y2 = y2, y1
                if x3 > x4:
                    x3, x4 = x4, x3
                    y3, y4 = y4, y3

                if y1 > y2:  # Falling Line first
                    x1, x3 = x3, x1
                    y1, y3 = y3, y1
                    x2, x4 = x4, x2
                    y2, y4 = y4, y2

                if not (x1 > x4 or x2 < x3 or y1 > y3 or y2 < y4):  # Determine Intersection between 2 lines
                    if (x1 + y1) % 2 == (x3 + y3) % 2:
                        y_inter = (y1 + y3 + x3 - x1) // 2  # y of intersection
                        x_inter = x1 + y_inter - y1  # x of intersection
                        if x4 >= x_inter >= x3 and x_inter <= x2 and y2 >= y_inter >= y4:
                            ppoints.append([x_inter, y_inter])

    for p in ppoints:
        if 0 <= p[0] <= 4_000_000 and 0 <= p[1] <= 4_000_000:
            is_pos = True
            for report in data:
                md = get_md(report[0], report[1], report[2], report[3])
                mandis2 = get_md(report[0], report[1], p[0], p[1])
                if md >= mandis2:
                    is_pos = False
                    break
            if is_pos:
                return p[0] * 4000000 + p[1]


def get_md(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
