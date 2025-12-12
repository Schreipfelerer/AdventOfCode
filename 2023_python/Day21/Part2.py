def readInput(use_example=False) -> list[str]:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines: list[str]) -> tuple[list[list[bool]], tuple[int, int]]:  # parses the input to the desired typ
    data: list[list[bool]] = []
    s = (-1, -1)
    for y, line in enumerate(lines):
        line = line[:-1]
        if not line:
            continue
        dataline: list[bool] = []
        for x, char in enumerate(line):
            dataline.append(char == '#')
            if char == 'S':
                s = (x, y)
        data.append(dataline)
    return data, s


def solve(data: tuple[list[list[bool]], tuple[int, int]]) -> int:  # solves the question
    map, start_pos = data
    plots = 0
    width = len(map)
    hight = len(map[0])

    steps = 26501365

    # Upwards
    upwards_covered = getCoveredPlots(map, (hight-1, start_pos[1]))
    even_full, odd_full = tuple(upwards_covered[-2:])
    if len(upwards_covered)%2==0:
        even_full, odd_full = odd_full, even_full
    plots += even_full * ((steps-start_pos[0])//(hight*2))
    plots += odd_full * ((steps-start_pos[0]-hight)//(hight*2))
    for s in range(steps-star_pos[0], )
    

    


    return plots

def getCoveredPlots(map: list[list[bool]], start_pos: tuple[int, int]) -> list[int]:
    return []


def main():
    lines = readInput(True)
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
