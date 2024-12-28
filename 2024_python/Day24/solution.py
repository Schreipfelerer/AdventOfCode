#!/usr/bin/env python3
def read_input(
    *,
    use_example=False,
) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example2.txt" if use_example else "input.txt"
    with open(file_loc) as f:
        return f.read().split("\n")


def parse_input(lines):  # parses the input to the desired typ
    l1, l2 = "\n".join(lines[:-2]).split("\n\n")
    wires = {}
    for l1s in l1.split("\n"):
        k, v = l1s.split(": ")
        wires[k] = int(v)
    l2 = [x.split(" -> ") for x in l2.split("\n")]
    l2 = [[x[0].split(" "), x[1]] for x in l2]
    return wires, l2


def solve_part1(data):  # solves the question
    wires, connections = data
    has_changed = True
    while has_changed:
        has_changed = False
        for c in connections:
            if c[0][0] in wires and c[0][2] in wires and c[1] not in wires:
                has_changed = True
                match c[0][1]:
                    case "AND":
                        wires[c[1]] = int(wires[c[0][0]] and wires[c[0][2]])
                    case "OR":
                        wires[c[1]] = int(wires[c[0][0]] or wires[c[0][2]])
                    case "XOR":
                        wires[c[1]] = int(wires[c[0][0]] != wires[c[0][2]])
    number = 0
    count = 0
    key = "z00"
    while key in wires:
        if wires[key]:
            number += 2 ** count
        count += 1
        key = "z0" + str(count) if len(str(count)) == 1 else "z" + str(count)

    return number


def solve_part2(data):  # solves the question
    wires, connections = data
    swap("z39", "pfw", connections)
    swap("dqr", "z33", connections)
    swap("vgs", "dtk", connections)
    swap("shh", "z21", connections)
    for i in range(45):
        print(f"Expected: {2**i}({i}) + {1} == {2**i+1} Actual:")
        print(add(2**i, 1, wires.copy(), connections))
        print(f"Expected: {2**i-1} + {1} == {2**i} Actual:")
        print(add(2**i-1, 1, wires.copy(), connections))
    return ",".join(sorted(["z39", "pfw", "dqr", "z33", "vgs", "dtk", "shh", "z21"]))


def add(x, y, wires, connection):
    for i in range(45):
        if len(str(i)) == 1:
            wires["x0"+str(i)] = 0
            wires["y0"+str(i)] = 0
        else:
            wires["x"+str(i)] = 0
            wires["y"+str(i)] = 0

    i = 0
    for xs in bin(x)[:1:-1]:
        iss = str(i)
        if len(str(i)) == 1:
            iss = "0" + str(i)
        if int(xs):
            wires["x"+iss] = 1
        i += 1

    i = 0
    for ys in bin(y)[:1:-1]:
        iss = str(i)
        if len(str(i)) == 1:
            iss = "0" + str(i)
        if int(ys):
            wires["y"+iss] = 1
        i += 1

    return solve_part1((wires, connection))


def swap(x, y, connections):
    for cs in connections:
        if x == cs[1]:
            for css in connections:
                if y == css[1]:
                    tmp = css[0]
                    css[0] = cs[0]
                    cs[0] = tmp


def main():
    lines = read_input(use_example=False)
    print(f"Part 1: {solve_part1(parse_input(lines))}")
    print()
    print(f"Part 2: {solve_part2(parse_input(lines))}")


if __name__ == "__main__":
    main()
