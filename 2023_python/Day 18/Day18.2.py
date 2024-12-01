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
        hex_code = line.split(" ")[2]
        data.append([int(hex_code[7]), int(hex_code[2:7], base=16)])
    return data


def solve(data):  # solves the question
    vertices = [(0, 0)]
    for instr in data:
        offset = (0, 0)
        if instr[0] == 3:
            offset = (-1, 0)
        if instr[0] == 1:
            offset = (1, 0)
        if instr[0] == 0:
            offset = (0, 1)
        if instr[0] == 2:
            offset = (0, -1)
        vertices.append((vertices[-1][0]+instr[1]*offset[0], vertices[-1][1]+instr[1]*offset[1]))

    area = 0

    for i in range(len(vertices)-1):
        area += vertices[i][0]*vertices[i+1][1]
        area -= vertices[i][1]*vertices[i+1][0]

    area //= 2
    area = abs(area)
    area += sum([x[1] for x in data])//2 + 1
    return area


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
