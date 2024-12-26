#!/usr/bin/env python3
def read_input(
    *,
    use_example=False,
) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc) as f:
        return f.read().split("\n")


def parse_input(lines):  # parses the input to the desired typ
    return lines[:-2]


def numeric_inputs(code):  # noqa: C901, PLR0912
    instruction = []
    x, y = 2, 3
    gx, gy = None, None
    for c in code:
        match c:
            case "0":
                gx, gy = 1, 3
            case "A":
                gx, gy = 2, 3
            case "1":
                gx, gy = 0, 2
            case "2":
                gx, gy = 1, 2
            case "3":
                gx, gy = 2, 2
            case "4":
                gx, gy = 0, 1
            case "5":
                gx, gy = 1, 1
            case "6":
                gx, gy = 2, 1
            case "7":
                gx, gy = 0, 0
            case "8":
                gx, gy = 1, 0
            case "9":
                gx, gy = 2, 0
        if x > gx and (gx != 0 or y != 3):
            instruction += ["<"]*(x-gx)
            x = gx
        if y > gy:
            instruction += ["^"]*(y-gy)
            y = gy
        if y < gy and (gy != 3 or x != 0):
            instruction += ["v"]*(gy-y)
            y = gy
        if x < gx:
            instruction += [">"]*(gx-x)
            x = gx

        if x > gx:
            instruction += ["<"]*(x-gx)
            x = gx
        if y < gy:
            instruction += ["v"]*(gy-y)
            y = gy
        instruction.append("A")
    return "".join(instruction)


def keyboard_instruction(code):  # noqa: C901
    instruction = []
    x, y = 2, 0
    gx, gy = None, None
    for c in code:
        match c:
            case "^":
                gx, gy = 1, 0
            case "A":
                gx, gy = 2, 0
            case "<":
                gx, gy = 0, 1
            case "v":
                gx, gy = 1, 1
            case ">":
                gx, gy = 2, 1
        if x > gx and (gx != 0 or y != 0):
            instruction += ["<"]*(x-gx)
            x = gx
        if y < gy:
            instruction += ["v"]*(gy-y)
            y = gy
        if y > gy and (x != 0 or gy != 0):
            instruction += ["^"]*(y-gy)
            y = gy
        if x < gx:
            instruction += [">"]*(gx-x)
            x = gx

        if x > gx:
            instruction += ["<"]*(x-gx)
            x = gx
        if y > gy:
            instruction += ["^"]*(y-gy)
            y = gy
        instruction.append("A")
    return "".join(instruction)



def solve_part1(data):  # solves the question
    complexity_score = 0
    for code in data:
        ins = numeric_inputs(code)
        for _ in range(2):
            ins = keyboard_instruction(ins)
        complexity_score += len(ins) * int(code[:-1])
    return complexity_score


def solve_part2(data):  # solves the question
    complexity_score = 0
    for code in data:
        ins = numeric_inputs(code)
        for _ in range(2):
            ins = keyboard_instruction(ins)
        complexity_score += len(ins) * int(code[:-1])
    return complexity_score


def main():
    lines = read_input(use_example=False)
    print(f"Part 1: {solve_part1(parse_input(lines))}")
    print()
    print(f"Part 2: {solve_part2(parse_input(lines))}")


if __name__ == "__main__":
    main()
