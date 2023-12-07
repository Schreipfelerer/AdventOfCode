def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    return [[int(line.split("Blueprint ")[1].split(":")[0]), int(line.split("costs ")[1].split(" ore")[0]),
             int(line.split("costs ")[2].split(" ore")[0]),
             [int(line.split("costs ")[3].split(" ore")[0]), int(line.split("and ")[1].split(" clay")[0])],
             [int(line.split("costs ")[4].split(" ore")[0]), int(line.split("and ")[2].split(" obsidian")[0])]]
            for line in lines]


def solve(data):  # solves the question
    qualitylevels = 1
    for blueprint in data[:3]:
        qualitylevels *= getmaxdiods(blueprint, 32, 0, 0, 0, 0, 1, 0, 0, 0, True)
    return qualitylevels


def getmaxdiods(blueprint, minute_left, ore, clay, obsidian, geode, ore_r, clay_r, obsidian_r, geode_r, do_print):
    if minute_left < 2:
        return geode+geode_r*minute_left

    pos = []
    if obsidian_r:
        ff = max(-(-(blueprint[4][0]-ore) // ore_r), -(-(blueprint[4][1]-obsidian) // obsidian_r)) + 1
        if ore >= blueprint[4][0] and obsidian >= blueprint[4][1]:
            ff = 1
        pos.append(getmaxdiods(blueprint, minute_left - ff, ore + ore_r * ff - blueprint[4][0],
                               clay + clay_r * ff, obsidian + obsidian_r * ff - blueprint[4][1], geode + geode_r * ff,
                               ore_r, clay_r, obsidian_r, geode_r + 1, do_print))

    if clay_r and obsidian_r * minute_left+obsidian < minute_left * blueprint[4][1]:
        ff = max(-(-(blueprint[3][0]-ore) // ore_r), -(-(blueprint[3][1]-clay) // clay_r)) + 1
        if ore >= blueprint[3][0] and clay >= blueprint[3][1]:
            ff = 1
        pos.append(getmaxdiods(blueprint, minute_left - ff, ore + ore_r * ff - blueprint[3][0],
                               clay + clay_r * ff - blueprint[3][1], obsidian + obsidian_r * ff, geode + geode_r * ff,
                               ore_r, clay_r, obsidian_r + 1, geode_r, do_print))

    if clay_r * minute_left+clay < minute_left * blueprint[3][1]:
        ff = -(-(blueprint[2]-ore) // ore_r) + 1
        if ore >= blueprint[2]:
            ff = 1
        pos.append(getmaxdiods(blueprint, minute_left - ff, ore + ore_r * ff - blueprint[2], clay + clay_r * ff,
                               obsidian + obsidian_r * ff, geode + geode_r * ff, ore_r, clay_r + 1, obsidian_r,
                               geode_r, len(pos) == 0 and do_print))
    if ore_r * minute_left+ore < minute_left * max(blueprint[2], blueprint[3][0], blueprint[4][0]):
        ff = -(-(blueprint[1] - ore) // ore_r) + 1
        if ore >= blueprint[1]:
            ff = 1
        pos.append(getmaxdiods(blueprint, minute_left - ff, ore + ore_r * ff - blueprint[1], clay + clay_r * ff,
                               obsidian + obsidian_r * ff, geode + geode_r * ff, ore_r + 1, clay_r, obsidian_r,
                               geode_r, len(pos) == 0 and do_print))

    if do_print:
        pass
        #  print((minute_left, max(pos)))

    return max(pos)


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
