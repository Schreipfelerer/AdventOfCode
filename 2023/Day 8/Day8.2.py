def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = [lines[0].strip("\n"), dict()]
    for line in lines[2:]:
        data[1][line[0:3]] = (line[7:10], line[12:15])
    return data


def solve(data):  # solves the question
    pos = [x for x in data[1] if x.endswith("A")]
    steps = 0
    instruction_length = len(data[0])
    visited_at_start = [[] for _ in pos]
    while any(not x.endswith("Z") for x in pos):
        if not steps%instruction_length:
            if all([pos_i in visited_at_start[i] for i, pos_i in enumerate(pos)]):
                print([len(pos_i) for pos_i in visited_at_start])
                print(visited_at_start)
            else:
                for i, pos_i in enumerate(pos):
                    if pos_i in visited_at_start[i]:
                        # print(f"Loop in {i} after {steps//instruction_length} passes.")
                        pass
                    else:
                        visited_at_start[i].append(pos_i)
        direction = 0 if data[0][steps%instruction_length] == "L" else 1
        pos = [data[1][x][direction] for x in pos]
        steps +=1


    return steps


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
