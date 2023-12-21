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
        datapoint = line.split(" ")[:2]
        datapoint[1] = int(datapoint[1])
        data.append(datapoint)
    return data


def solve(data):  # solves the question
    edges = [(0, 0)]
    for instr in data:
        for _ in range(instr[1]):
            offset = (0, 0)
            if instr[0] == "U":
                offset = (-1, 0)
            if instr[0] == "D":
                offset = (1, 0)
            if instr[0] == "R":
                offset = (0, 1)
            if instr[0] == "L":
                offset = (0, -1)
            edges.append((edges[-1][0]+offset[0], edges[-1][1]+offset[1]))
    assert edges.pop() == (0, 0)
    min_x = min(edges, key=lambda x: x[0])[0]
    max_x = max(edges, key=lambda x: x[0])[0]
    min_y = min(edges, key=lambda x: x[1])[1]
    max_y = max(edges, key=lambda x: x[1])[1]
    outside = []
    queue = [(min_x-1, min_y-1)]
    while queue:
        pos = queue.pop(0)
        if pos in outside:
            continue
        if max_x+1 < pos[0] or pos[0] < min_x-1:
            continue
        if max_y+1 < pos[1] or pos[1] < min_y-1:
            continue
        if pos in edges:
            continue
        outside.append(pos)
        queue.append((pos[0]+1, pos[1]))
        queue.append((pos[0]-1, pos[1]))
        queue.append((pos[0], pos[1]+1))
        queue.append((pos[0], pos[1]-1))

    outside.sort()

    return (max_x-min_x+3)*(max_y-min_y+3)-len(outside)


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
