def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    start = (0, 0)
    for i, line in enumerate(lines):
        mstart = line.find("^")
        if mstart != -1:
            start = (mstart, i)
            lines[i] = line[:mstart] + "." + line[mstart+ 1:]
    return lines[:-1], start


def solvePart1(data):  # solves the question
    data, pos = data
    visitedpos = set()
    facings = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    face = 0
    while 0<=pos[0]<len(data[0]) and 0<=pos[1]<len(data):
        visitedpos.add(pos)
        newpos = (pos[0]+facings[face][0], pos[1]+facings[face][1])
        if not (0<=newpos[0]<len(data[0]) and 0<=newpos[1]<len(data)):
            break
        if data[newpos[1]][newpos[0]] == "#":
            face += 1
            face %= 4
        else:
            pos = newpos
    return len(visitedpos)

def solvePart2(data):  # solves the question
    data, pos = data
    start = pos
    visitedpos = set()
    facings = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    face = 0
    while 0 <= pos[0] < len(data[0]) and 0 <= pos[1] < len(data):
        newpos = (pos[0] + facings[face][0], pos[1] + facings[face][1])
        if not (0 <= newpos[0] < len(data[0]) and 0 <= newpos[1] < len(data)):
            visitedpos.add(pos)
            break
        if data[newpos[1]][newpos[0]] == "#":
            face += 1
            face %= 4
        else:
            visitedpos.add(pos)
            pos = newpos

    try_block = visitedpos.copy()
    try_block.discard(start)

    loops = 0
    for b in try_block:
        pos = start
        visitedpos = set()
        face = 0
        while 0 <= pos[0] < len(data[0]) and 0 <= pos[1] < len(data):
            if (pos, face) in visitedpos:
                loops+=1
                break
            newpos = (pos[0] + facings[face][0], pos[1] + facings[face][1])
            if not (0 <= newpos[0] < len(data[0]) and 0 <= newpos[1] < len(data)):
                visitedpos.add((pos, face))
                break
            if data[newpos[1]][newpos[0]] == "#" or newpos == b:
                face += 1
                face %= 4
            else:
                visitedpos.add((pos, face))
                pos = newpos

    return loops


def main():
    lines = readInput()
    data = parseInput(lines)
    print(f"Part 1: {solvePart1(data)}")
    print("")
    print(f"Part 2: {solvePart2(data)}")


if __name__ == "__main__":
    main()
