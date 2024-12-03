import sys
import threading


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
    biggest = 0
    for x_pos in range(len(data)):
        print(f"x: {x_pos} checked / {len(data)}")
        tt = getTraveledTrough(data, x_pos, 0, 1) # Beams from Left
        current_length = len(tt[0] | tt[1] | tt[2] | tt[3])
        if current_length > biggest:
             biggest = current_length
        tt = getTraveledTrough(data, x_pos, len(data[x_pos])-1, 3) # Beams from Right
        current_length = len(tt[0] | tt[1] | tt[2] | tt[3])
        if current_length > biggest:
            biggest = current_length
    for y_pos in range(len(data[0])):
        print(f"x: {y_pos} checked / {len(data[0])}")
        tt = getTraveledTrough(data, 0, y_pos, 2) # Beams from Top
        current_length = len(tt[0] | tt[1] | tt[2] | tt[3])
        if current_length > biggest:
            biggest = current_length
        tt = getTraveledTrough(data, len(data)-1, y_pos, 0) # Beams from Bottom
        current_length = len(tt[0] | tt[1] | tt[2] | tt[3])
        if current_length > biggest:
            biggest = current_length

    return biggest


memom = {}
currently_solving = []
loop = False

def getTraveledTrough(data, x_pos, y_pos, direction):
    global currently_solving
    global loop
    traveled_trough = [set(), set(), set(), set()]
    if 0 > x_pos or x_pos >= len(data):
        return traveled_trough
    if 0 > y_pos or y_pos >= len(data[0]):
        return traveled_trough
    if (x_pos, y_pos, direction) in currently_solving: # Loop detection
        if not loop:
            loop_index = currently_solving.index((x_pos, y_pos, direction))
            curren_loop = currently_solving[loop_index:]
            loop = True
            currently_solving = currently_solving[:loop_index]
            r = [t.copy() for t in getTraveledTrough(data, x_pos, y_pos, direction)]
            currently_solving += curren_loop
            loop = False

        #for i in range(len(currently_solving)-1, currently_solving.index((x_pos, y_pos, direction))-1, -1):
        #    traveled_trough[currently_solving[i][2]].add(currently_solving[i][:2])
            return r
        else:
            return traveled_trough

    key = str(x_pos)+","+str(y_pos)+","+str(direction)
    if key in memom.keys():
        return [t.copy() for t in memom[key]]

    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

    currently_solving.append((x_pos, y_pos, direction))
    traveled_trough[direction].add((x_pos, y_pos))

    char = data[x_pos][y_pos]
    ntt = []

    if direction % 2 == 0 and char in "|.":
        ntt.append(getTraveledTrough(data, x_pos + directions[direction][0], y_pos + directions[direction][1], direction))
    elif direction % 2 and char in "-.":
        ntt.append(getTraveledTrough(data, x_pos + directions[direction][0], y_pos + directions[direction][1], direction))
    elif char == "/":
        new_direction = (direction + (-1 if direction % 2 else 1)) % 4
        ntt.append(getTraveledTrough(
            data, x_pos + directions[new_direction][0], y_pos + directions[new_direction][1], new_direction))
    elif char == "\\":
        new_direction = (direction + (1 if direction % 2 else -1)) % 4
        ntt.append(getTraveledTrough(
            data, x_pos + directions[new_direction][0], y_pos + directions[new_direction][1], new_direction))
    else:
        for new_direction in (direction + 1, direction + 3):
            new_direction %= 4
            ntt.append(getTraveledTrough(
                data,x_pos + directions[new_direction][0], y_pos + directions[new_direction][1], new_direction))

    for tt in ntt:
        tt = tt.copy()
        for i in range(4):
            traveled_trough[i] = traveled_trough[i] | tt[i]
    if not loop:
        memom[key] = [t.copy() for t in traveled_trough]
    currently_solving.remove((x_pos, y_pos, direction))
    return traveled_trough

def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    sys.setrecursionlimit(5000)
    threading.stack_size(2 ** 26)
    threading.Thread(target=main).start()
