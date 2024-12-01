import math


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
    loop_length = [0 for _ in pos]
    end_indexes = [0 for _ in pos]
    while True:
        if not steps % instruction_length:
            if all(loop_length):
                print(loop_length, end_indexes)
            else:
                for i, end_index in enumerate(end_indexes):
                    if not end_indexes[i]:
                        if pos[i].endswith("Z"):
                            end_indexes[i] = steps // instruction_length
                for i, pos_i in enumerate(pos):
                    if not loop_length[i]:
                        if pos_i in visited_at_start[i]:
                            loop_length[i] = steps // instruction_length - visited_at_start[i].index(pos_i)
                            if all(loop_length):
                                end_indexes = [end_indexes[i] % loop_length[i] for i in range(len(end_indexes))]
                                while len(loop_length) > 1:
                                    new_end_index = end_indexes[0] + loop_length[0]
                                    while new_end_index % loop_length[1] != end_indexes[1]:
                                        new_end_index += loop_length[0]
                                    end_indexes[0] = new_end_index
                                    end_indexes.pop(1)
                                    loop_length[0] = math.lcm(loop_length[0], loop_length[1])
                                    loop_length.pop(1)
                                return end_indexes[0] * instruction_length
                        else:
                            visited_at_start[i].append(pos_i)
        direction = 0 if data[0][steps % instruction_length] == "L" else 1
        pos = [data[1][x][direction] for x in pos]
        steps += 1


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
