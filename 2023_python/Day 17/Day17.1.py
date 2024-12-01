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
        data.append([int(x) for x in line.rstrip("\n")])
    return data


def solve(data):  # solves the question
    cheapest = [[2**31 - 1 for _ in data[0]]for _ in data]
    to_visit = [(0, 0, 0, 0)]
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    while to_visit:
        c = to_visit.pop(0)
        if c[2] >= cheapest[c[0]][c[1]]:
            continue
        cheapest[c[0]][c[1]] = c[2]
        for i, direction in enumerate(directions):
            for y in range(1,4):
                new_x = c[0]+direction[0]*y
                new_y = c[1]+direction[1]*y
                if new_x < 0 or new_x >= len(data):
                    continue
                if new_y < 0 or new_y >= len(data[0]):
                    continue
                new_cost = c[2]
                for yy in range(1, y+1):
                    new_cost +=data[c[0]+direction[0]*yy][c[1]+direction[1]*yy]
                if i != c[3]:
                    to_visit.append((new_x, new_y, new_cost, i))
        # to_visit.sort(key=lambda x: x[2])
    return cheapest[-1][-1]


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
