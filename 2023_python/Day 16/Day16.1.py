def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    return [line.rstrip("\n") for line in lines]


def solve(data):  # solves the question
    traveled_trough = [[],[],[],[]]
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    beams = [(0, 0, 1)]
    while beams:
        beam = beams.pop(0)
        beam_no_dir = beam[:2]
        direction = beam[2]
        if 0 > beam[0] or beam[0] >= len(data):
            continue
        if 0 > beam[1] or beam[1] >= len(data[0]):
            continue
        if beam_no_dir in traveled_trough[direction]:
            continue
        traveled_trough[direction].append(beam_no_dir)

        char = data[beam_no_dir[0]][beam_no_dir[1]]

        if direction%2 == 0 and char in "|.":
            beams.append((beam[0]+directions[direction][0], beam[1]+directions[direction][1], direction))
        elif direction%2 and char in "-.":
            beams.append((beam[0]+directions[direction][0], beam[1]+directions[direction][1], direction))
        elif char == "/":
            new_direction = (direction + (-1 if direction%2 else 1))%4
            beams.append((beam[0] + directions[new_direction][0], beam[1] + directions[new_direction][1], new_direction))
        elif char == "\\":
            new_direction = (direction + (1 if direction%2 else -1))%4
            beams.append((beam[0] + directions[new_direction][0], beam[1] + directions[new_direction][1], new_direction))
        else:
            for new_direction in (direction+1, direction-1):
                new_direction %= 4
                beams.append(
                    (beam[0] + directions[new_direction][0], beam[1] + directions[new_direction][1], new_direction))


    return len(set(traveled_trough[0]+traveled_trough[1]+traveled_trough[2]+traveled_trough[3]))


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
