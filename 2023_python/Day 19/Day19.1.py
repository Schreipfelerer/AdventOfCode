def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = [{}, []]

    for line in lines:
        if line == "\n":
            continue
        if line.startswith("{"):
            line = line[1:-2]
            part = {}
            for xmas in line.split(","):
                xmas = xmas.split("=")
                part[xmas[0]] = int(xmas[1])
            data[1].append(part)
        else:
            line = line.split("{")
            key = line[0]
            data[0][key] = [x.split(":") for x in line[1][:-2].split(",")]
    return data


def solve(data):  # solves the question
    rules, parts = data
    solution = 0
    for part in parts:
        op = "in"
        while op != "R" and op != "A":
            rule = rules[op]
            for rule_sub in rule:
                if len(rule_sub) == 1:
                    op = rule_sub[0]
                else:
                    value = part[rule_sub[0][0]]
                    comp = rule_sub[0][1]
                    rule_value = int(rule_sub[0][2:])
                    if comp == "<":
                        if value < rule_value:
                            op = rule_sub[1]
                            break
                    elif comp == ">":
                        if value > rule_value:
                            op = rule_sub[1]
                            break
        if op == "A":
            solution += sum(part.values())
    return solution


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
