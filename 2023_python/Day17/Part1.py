import heapq

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
    to_visit = [(0, (0, 0, 0)), (0, (0, 0, 3))]
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    visited = set()
    height = len(data)
    width = len(data[0])
    end = (height-1, width-1)
    while to_visit:
        cost, c = heapq.heappop(to_visit)
        if c in visited:
            continue
        visited.add(c)
        if (c[0], c[1]) == end:
            return cost
        for i, direction in enumerate(directions):
            if i == c[2] or i == (c[2]+2)%4:
                continue
            new_cost = cost
            for y in range(1,4):
                new_x = c[0]+direction[0]*y
                new_y = c[1]+direction[1]*y
                if new_x < 0 or new_x >= height:
                    break
                if new_y < 0 or new_y >= width:
                    break
                new_cost += data[new_x][new_y]
                heapq.heappush(to_visit, (new_cost, (new_x, new_y, i)))
    return 0


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
