#!/usr/bin/env python3
def read_input(
        *,
        use_example=False,
) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example2.txt" if use_example else "input.txt"
    with open(file_loc) as f:
        return f.read().split("\n")


def parse_input(lines):  # parses the input to the desired typ
    return [int(x.split(": ")[1]) for x in lines[:3]], [int(x) for x in lines[4].split(": ")[1].split(",")]


def solve_part1(data):  # solves the question
    reg, op = data
    p = 0
    out = []
    while p < len(op):
        match op[p]:
            case 0:
                reg[0] = reg[0] >> readCombo(op[p+1], reg)
            case 1:
                reg[1] = reg[1] ^ op[p+1]
            case 2:
                reg[1] = readCombo(op[p+1], reg) & 7
            case 3:
                if reg[0]: p = op[p+1] - 2
            case 4:
                reg[1] = reg[1] ^ reg[2]
            case 5:
                out.append(str(readCombo(op[p+1], reg) & 7))
            case 6:
                reg[1] = reg[0] >> readCombo(op[p + 1], reg)
            case 7:
                reg[2] = reg[0] >> readCombo(op[p + 1], reg)
        p += 2
    return ",".join(out)


def readCombo(combo, reg):
    if 0 <= combo < 4:
        return combo
    if 4 <= combo < 7:
        return reg[combo-4]


def solve_part2(data):  # solves the question
    reg, op = data
    reg[0] = 0
    for i in range(len(op)-1, -1, -1):
        reg[0] = reg[0] << 3
        for _ in range(8):
            if solve_part1((reg[:], op)) == ",".join([str(x) for x in op[i:]]):
                break
            reg[0] += 1
    return reg[0]


def main():
    lines = read_input(use_example=False)
    print(f"Part 1: {solve_part1(parse_input(lines))}")
    print()
    print(f"Part 2: {solve_part2(parse_input(lines))}")


if __name__ == "__main__":
    main()
