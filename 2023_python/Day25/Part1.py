def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    v = set()
    e = set()
    for line in lines:
        line = line[:-1]
        if not line:
            continue

        line = line.split(": ")
        left = line[0]
        right = line[1].split(" ")
        v.add(left)
        for r in right:
            v.add(r)
            e.add((left, r))
    return v, e


def solve(data):  # solves the question
    v, e = data
    start = v.pop()
    v.add(start)

    colored = set()
    to_color = [start]
    while to_color:
        c = to_color.pop()
        if c in colored:
            continue
        colored.add(c)
        for edge in e:
            if c in edge:
                to_color.append(edge[(edge.index(c)+1)%2])

    return len(colored)*(len(v)-len(colored))


def main():
    lines = readInput(True)
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
