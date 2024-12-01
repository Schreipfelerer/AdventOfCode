def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    seeds = lines[0].rstrip("\n").lstrip("seeds: ").split(" ")
    data = [[(int(seeds[i]), int(seeds[i + 1])) for i in range(0, len(seeds), 2)]]
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
        converted_seeds = []
        for row in map_con:
            i = 0
            while i < len(seeds):
                seed = seeds[i]
                if seed is int or row is int:
                    print("lol")
                if (row[1] < (seed[0] + seed[1])) and ((row[1] + row[2]) > seed[0]):
                    overlap = min(seed[0] + seed[1], row[1] + row[2]) - max(row[1], seed[0])
                    converted_seeds.append((max(row[1], seed[0]) - row[1] + row[0], overlap))
                    if row[1] > seed[0]:
                        seeds.append((seed[0], row[1] - seed[0]))
                    if row[1] + row[2] < seed[0] + seed[1]:
                        seeds.append((row[1] + row[2], seed[0] + seed[1] - (row[1] + row[2])))
                    seeds.remove(seed)
                else:
                    i += 1
        seeds = converted_seeds + seeds
    return min(seeds, key=lambda x: x[0])[0]


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
