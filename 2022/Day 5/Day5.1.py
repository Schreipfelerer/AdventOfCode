def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    is_parsing_moves = False
    moves = []
    location = []
    for line in lines:
        if is_parsing_moves:
            split = line.split(" ")
            moves.append([int(split[1]), int(split[3]), int(split[5])])
        else:
            if line:
                row = []
                for i in range(1, len(line), 4):
                    row.append(line[i].strip())
                location.append(row)
            else:
                is_parsing_moves = True
                location = location[:-1]
    return moves, location


def solve(data):  # solves the question
    moves, location = data
    stacks = []
    for i in range(len(location[-1])):
        stacks.append([])
        for loc in reversed(location):
            if i < len(loc) and loc[i]:
                stacks[i].append(loc[i])

    for move in moves:
        for _ in range(move[0]):
            if stacks[move[1]-1]:
                stacks[move[2]-1].append(stacks[move[1]-1].pop())
            else:
                break

    result = ""
    for stack in stacks:
        result += stack[-1]
    return result


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
