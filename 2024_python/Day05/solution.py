import re

def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    rules = []
    updates = []
    first_sec = True
    for line in lines:
        if not line:
            first_sec = False
            continue
        if first_sec:
            rules.append(list(map(int, line.split("|"))))
        else:
            updates.append(list(map(int, line.split(","))))
    return rules, updates


def solvePart1(data):  # solves the question
    rules, updates = data
    middles = 0

    for u in updates:
        is_correct = True
        for i, s in enumerate(u):
            for t in u[:i]:
                if [s, t] in rules:
                    is_correct = False
            for t in u[i+1:]:
                if [t, s] in rules:
                    is_correct = False

        if is_correct:
            middles += u[len(u)//2]
    return middles

def solvePart2(data):  # solves the question
    rules, updates = data
    middles = 0
    for u in updates:
        is_correct = True
        for i, s in enumerate(u):
            for t in u[:i]:
                if [s, t] in rules:
                    is_correct = False
            for t in u[i+1:]:
                if [t, s] in rules:
                    is_correct = False

        if is_correct:
            continue

        u = order(u, rules)
        middles += u[len(u) // 2]
    return middles


def order(to_order, rules):
    if len(to_order) < 2:
        return to_order
    pivot = to_order[len(to_order) // 2]
    l = []
    r = []
    for u in to_order:
        if u == pivot:
            continue
        if [u, pivot] in rules:
            l.append(u)
        elif [pivot, u] in rules:
            r.append(u)
        else:
            print("Fuck")

    return order(l, rules) + [pivot] + order(r, rules)


def main():
    lines = readInput()
    data = parseInput(lines)
    print(f"Part 1: {solvePart1(data)}")
    print("")
    print(f"Part 2: {solvePart2(data)}")


if __name__ == "__main__":
    main()
