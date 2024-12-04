import re

def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    return lines[:-1]


def solvePart1(data):  # solves the question
    number = 0
    joined = "\n".join(data)
    rotated = ["".join([data[y][x] for y in range(len(data))]) for x in range(len(data[0]))]
    joined += "\n\n"+"\n".join(rotated)
    diagonal = ["".join([data[min(y, len(data)-1)-min(len(data[0]), len(data[0])+len(data)-y-1)+x+1][x] for x in range(max(0, len(data[0])-y-1), min(len(data[0]), len(data[0])+len(data)-y-1))]) for y in range(len(data) + len(data[0]) - 1)]
    joined += "\n\n"+"\n".join(diagonal)
    data = data[::-1]
    diagonal2 = ["".join([data[min(y, len(data)-1)-min(len(data[0]), len(data[0])+len(data)-y-1)+x+1][x] for x in range(max(0, len(data[0])-y-1), min(len(data[0]), len(data[0])+len(data)-y-1))]) for y in range(len(data) + len(data[0]) - 1)]
    joined += "\n\n"+"\n".join(diagonal2)
    number += len(re.findall("XMAS", joined))
    number += len(re.findall("SAMX", joined))
    return number

def solvePart2(data):  # solves the question
    xmas = 0
    for y in range(1, len(data)-1):
        for x in range(1, len(data[0])-1):
            if data[y][x] == "A":
                if {"S","M"} == {data[y-1][x-1], data[y+1][x+1]} == {data[y-1][x+1], data[y+1][x-1]}:
                    xmas += 1
    return xmas


def main():
    lines = readInput()
    data = parseInput(lines)
    print(f"Part 1: {solvePart1(data)}")
    print("")
    print(f"Part 2: {solvePart2(data)}")


if __name__ == "__main__":
    main()
