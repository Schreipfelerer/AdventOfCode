from collections import deque


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
        row = []
        for risk in line.rstrip("\n"):
            row.append(int(risk))
        data.append(row)

    return data


def solve(data):  # solves the question
    cost = []
    for i in range(len(data)):
        cost.append([9999]*len(data[0]))
    cost[0][0] = 0

    stack = deque()
    in_stack = set()
    first_el = (0, 0)
    stack.append(first_el)
    in_stack.add(first_el)
    while stack:
        el = stack.popleft()
        i, j = el
        in_stack.remove(el)
        neighbours = []
        if j != len(cost[i]) - 1:
            neighbours.append((i, j + 1))
        if i != len(cost) - 1:
            neighbours.append((i + 1, j))
        if i != 0:
            neighbours.append((i - 1, j))
        if j != 0:
            neighbours.append((i, j - 1))

        for neighbour in neighbours:
            i2, j2 = neighbour
            if cost[i][j] + data[i2][j2] < cost[i2][j2]:
                cost[i2][j2] = cost[i][j] + data[i2][j2]
                if (i2, j2) not in in_stack:
                    stack.append(neighbour)
                    in_stack.add(neighbour)

    return cost[-1][-1]


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
