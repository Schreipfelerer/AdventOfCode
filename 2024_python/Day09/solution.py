def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    return lines[0]


def solvePart1(line):  # solves the question
    solve_list = []
    cur_id = 0
    do_empty = False
    for c in line:
        i = int(c)
        if do_empty:
            for _ in range(i):
                solve_list.append(-1)
        else:
            for _ in range(i):
                solve_list.append(cur_id)
            cur_id += 1
        do_empty = not do_empty

    while -1 in solve_list:
        while solve_list[-1] == -1:
            solve_list.pop()
        try:
            ind = solve_list.index(-1)
        except ValueError:
            ind = -1
        if ind != -1:
            solve_list[ind] = solve_list[-1]
            solve_list.pop()

    solution = 0
    for i, c in enumerate(solve_list):
        solution += i*c
    return solution


def solvePart2(line: str):  # solves the question
    solve_list = []
    cur_id = -1
    do_empty = False
    for c in line:
        i = int(c)
        if do_empty:
            for _ in range(i):
                solve_list.append(-1)
        else:
            cur_id += 1
            for _ in range(i):
                solve_list.append(cur_id)
        do_empty = not do_empty

    for i in line[::2][::-1]:
        streak = 0
        old_ind = solve_list.index(cur_id)
        for ind, c in enumerate(solve_list[:old_ind]):
            if c == -1:
                streak += 1
            else:
                streak = 0
            if streak == int(i):
                solve_list[ind-streak+1:ind+1] = [cur_id] * streak
                solve_list[old_ind:old_ind+streak] = [-1] * streak
                break
        cur_id -= 1


    solution = 0
    for i, c in enumerate(solve_list):
        if c == -1:
            continue
        solution += i * c
    return solution


def main():
    lines = readInput()
    data = parseInput(lines)
    print(f"Part 1: {solvePart1(data)}")
    print("")
    print(f"Part 2: {solvePart2(data)}")


if __name__ == "__main__":
    main()
