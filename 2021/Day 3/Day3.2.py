from copy import deepcopy


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
        for i, bit in enumerate(line.rstrip("\n")):
            if len(data) < i + 1:
                data.append([])
            data[i].append(int(bit))
    return data


def solve(data):  # solves the question
    oxygen_rating = deepcopy(data)
    co2_rating = deepcopy(data)
    onlysave = None
    for i, position in enumerate(oxygen_rating):
        onlysave = int(not bool(min(set(oxygen_rating[i]), key=oxygen_rating[i].count)))
        num_pop = 0
        for j in range(len(position)):
            if position[j - num_pop] != onlysave:
                for pos in oxygen_rating:
                    pos.pop(j - num_pop)
                num_pop += 1
        if len(oxygen_rating) == 1:
            break

    for i, position in enumerate(co2_rating):
        onlysave = min(set(co2_rating[i]), key=co2_rating[i].count)
        num_pop = 0
        for j in range(len(position)):
            if position[j - num_pop] != onlysave:
                for pos in co2_rating:
                    pos.pop(j - num_pop)
                num_pop += 1
        if len(co2_rating) == 1:
            break
    oxygen_rating_dec = int("".join(str(e[0]) for e in oxygen_rating), 2)
    co2_rating_dec = int("".join(str(e[0]) for e in co2_rating), 2)
    return oxygen_rating_dec * co2_rating_dec


def main():
    lines = readInput(False)
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
