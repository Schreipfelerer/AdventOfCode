from copy import deepcopy


def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    string = lines[0].rstrip("\n")
    data = []
    for line in lines[2:]:
        data.append(line.rstrip("\n").split(" -> "))

    return string, data


def solve(data):  # solves the question
    polymer, rules = data
    polymer_pairs = []
    for i in range(len(polymer) - 1):
        pp = polymer[i] + polymer[i + 1]
        inserted = False
        for poly_pair in polymer_pairs:
            if poly_pair[0] == pp:
                poly_pair[1] += 1
                inserted = True
                break
        if not inserted:
            polymer_pairs.append([pp, 1])

    for i in range(40):
        for pp in deepcopy(polymer_pairs):
            for rule in rules:
                if rule[0] == pp[0]:
                    new_pairs = [[pp[0][0] + rule[1], pp[1]], [rule[1] + pp[0][1], pp[1]]]
                    for new_pair in new_pairs:
                        inserted = False
                        for poly_pair in polymer_pairs:
                            if poly_pair[0] == new_pair[0]:
                                poly_pair[1] += new_pair[1]
                                inserted = True
                                break
                        if not inserted:
                            polymer_pairs.append(new_pair)
                    for pp_2 in polymer_pairs:
                        if pp_2[0] == pp[0]:
                            pp_2[1] -= pp[1]

    counts = dict()
    for pp in polymer_pairs:
        if pp[0][0] in counts.keys():
            counts[pp[0][0]] += pp[1]
        else:
            counts[pp[0][0]] = pp[1]

    if polymer[-1] in counts.keys():
        counts[polymer[-1]] += 1
    else:
        counts[polymer[-1]] = 1

    return counts[max(counts, key=counts.get)] - counts[min(counts, key=counts.get)]


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
