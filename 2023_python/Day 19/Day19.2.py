def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = {}

    for line in lines:
        if line == "\n":
            continue
        if not line.startswith("{"):
            line = line.split("{")
            key = line[0]
            data[key] = [x.split(":") for x in line[1][:-2].split(",")]
    return data


def solve(data):  # solves the question
    letter_to_index = {"x": 0, "m": 1, "a": 2, "s": 3}
    solution = 0
    parts = [["in", (1, 4001), (1, 4001), (1, 4001), (1, 4001)]]
    while parts:
        part = parts.pop(0)
        if part[0] == "R":
            continue
        for sub_range in part[1:]:
            if sub_range[0] >= sub_range[1]:
                continue
        if part[0] == "A":
            solution += (part[1][1] - part[1][0]) * (part[2][1] - part[2][0]) * (part[3][1] - part[3][0]) * (
                    part[4][1] - part[4][0])
            continue

        rule = data[part[0]]
        for rule_sub in rule:
            if len(rule_sub) == 1:
                part[0] = rule_sub[0]
                parts.append(part)
            else:
                new_part = part[:]
                index = letter_to_index[rule_sub[0][0]] + 1
                new_part[0] = rule_sub[1]
                rule_value = int(rule_sub[0][2:])
                if rule_sub[0][1] == "<":
                    part[index] = (max(part[index][0], rule_value), part[index][1])
                    new_part[index] = (new_part[index][0], min(new_part[index][1], rule_value))
                elif rule_sub[0][1] == ">":
                    part[index] = (part[index][0], min(part[index][1], rule_value + 1))
                    new_part[index] = (max(new_part[index][0], rule_value + 1), new_part[index][1])
                parts.append(new_part)
    return solution


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
