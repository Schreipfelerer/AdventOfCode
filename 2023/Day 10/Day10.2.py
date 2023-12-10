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
    char_dict = {"J" : [(0, -1), (-1, 0)],
                 "L" : [(0, 1), (-1, 0)],
                 "7" : [(0, -1), (1, 0)],
                 "F" : [(0, 1), (1, 0)],
                 "-" : [(0, 1), (0, -1)],
                 "|" : [(1, 0), (-1, 0)],
                 "." : [],
                 "S" : []}
    index = (0, 0)
    for i, line in enumerate(data):
        if "S" in line:
            index = (i, line.index("S"))

    start_index = index

    offsets = (0, 1), (1, 0), (0, -1), (-1, 0)
    for offset in offsets:
        y = index[0] + offset[0]
        x = index[1] + offset[1]

        if 0 <= y < len(data):
            if 0 <= x < len(data[y]):
                char = data[y][x]
                neg_offset =(-offset[0], -offset[1])
                if neg_offset in char_dict[char]:
                    char_dict["S"].append(offset)

    direction = char_dict["S"][0]

    if direction == (0, 1):
        if char_dict["S"][1] == (1, 0):
            data[index[0]] = data[index[0]][:index[1]] + "F" + data[index[0]][index[1] + 1:]
        elif char_dict["S"][1] == (0, -1):
            data[index[0]] = data[index[0]][:index[1]] + "-" + data[index[0]][index[1] + 1:]
        else:
            data[index[0]] = data[index[0]][:index[1]] + "L" + data[index[0]][index[1] + 1:]
    if direction == (1, 0):
        if char_dict["S"][1] == (-1, 0):
            data[index[0]] = data[index[0]][:index[1]] + "|" + data[index[0]][index[1] + 1:]
        else:
            data[index[0]] = data[index[0]][:index[1]] + "7" + data[index[0]][index[1] + 1:]
    if direction == (0, -1):
        data[index[0]] = data[index[0]][:index[1]] + "J" + data[index[0]][index[1] + 1:]

    visited_tiles = []
    while start_index != index or len(visited_tiles) == 0:
        index = (index[0]+direction[0], index[1]+direction[1])
        direction_list = char_dict[data[index[0]][index[1]]][:]
        direction_list.remove((-direction[0], -direction[1]))
        direction = direction_list[0]
        visited_tiles.append(index)

    inside_loop = 0
    outside_tiles = []
    for i, row in enumerate(data):
        for y, char in enumerate(row):
            if (i, y) in outside_tiles:
                continue
            if (i, y) in visited_tiles:
                continue
            offset = (-1, 0) if i < len(data)//2 else (1, 0)
            steps = 1
            edges = 0
            last_char = ""
            while 0 <= i+offset[0]*steps < len(data) and 0 <= y+offset[1]*steps < len(data[i]):
                if (i+offset[0]*steps, y+offset[1]*steps) in visited_tiles:
                    non_dir = offset.index(0)
                    current_char = data[i+offset[0]*steps][y+offset[1]*steps]
                    if any([char_dir[non_dir] for char_dir in char_dict[current_char]]):
                        if current_char in "FLJ7":
                            is_fake = False
                            if offset == (-1, 0):
                                if last_char == "J":
                                    if current_char == "F":
                                        is_fake = True
                                elif last_char == "L":
                                    if current_char == "7":
                                        is_fake = True
                            if offset == (1, 0):
                                if last_char == "7":
                                    if current_char == "L":
                                        is_fake = True
                                elif last_char == "F":
                                    if current_char == "J":
                                        is_fake = True
                            if is_fake:
                                last_char = ""
                            else:
                                edges += 1
                                last_char = current_char
                        else:
                            edges += 1
                steps += 1
            if edges%2:
                inside_loop += 1
            else:
                add_to_outside = {(i, y)}
                while add_to_outside:
                    add_to_outside_tile = add_to_outside.pop()
                    if add_to_outside_tile not in outside_tiles:
                        if add_to_outside_tile not in visited_tiles:
                            if 0 <= add_to_outside_tile[0] < len(data) and 0 <= add_to_outside_tile[1] < len(data[0]):
                                outside_tiles.append(add_to_outside_tile)
                                add_to_outside.add((add_to_outside_tile[0]+1, add_to_outside_tile[1]))
                                add_to_outside.add((add_to_outside_tile[0]-1, add_to_outside_tile[1]))
                                add_to_outside.add((add_to_outside_tile[0], add_to_outside_tile[1]+1))
                                add_to_outside.add((add_to_outside_tile[0], add_to_outside_tile[1]-1))

    return inside_loop


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
