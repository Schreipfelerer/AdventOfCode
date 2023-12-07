def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = [[int(x) for x in lines[0].rstrip("\n").lstrip("seeds: ").split(" ")]]
    range_map = []
    for line in lines[2:]:

        if line.endswith("map:\n"):
            pass
        elif line == "\n":
            data.append(range_map)
            range_map = []
        else:
            range_map.append([int(x) for x in line.rstrip("\n").split(" ")])
    data.append(range_map)

    return data


def solve(data):  # solves the question
    seeds = data[0]
    for map_con in data[1:]:
        for seed in seeds:
            for row in map_con:
                if seed in range(row[1], row[1]+row[2]+1):
                    num = seed
                    seeds.remove(seed)
                    seeds.insert(0, num-row[1]+row[0])
                    break
    return min(seeds)


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
