def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for line in lines:
        datapoint = line.rstrip("\n").split(" ")
        datapoint[1] = [int(x) for x in datapoint[1].split(",")]
        datapoint[0] = datapoint[0]+"?"+datapoint[0]+"?"+datapoint[0]+"?"+datapoint[0]+"?"+datapoint[0]
        datapoint[1] = datapoint[1][:]+datapoint[1][:]+datapoint[1][:]+datapoint[1][:]+datapoint[1][:]
        data.append(datapoint)
    return data


def getPossibilities(record):
    springs, arrangement = record

    arrangement_cp = arrangement[:]
    is_gap = True
    i = 0
    while i < len(springs) and springs[i] != "?" :
        if springs[i] == ".":
            is_gap = True
        else:
            if not arrangement_cp:
                return 0
            if is_gap:
                if i+arrangement_cp[0] > len(springs):
                    return 0
                if "." in springs[i:i+arrangement_cp[0]]:
                    return 0
                else:
                    i += arrangement_cp[0]-1
                    arrangement_cp = arrangement_cp[1:]
                    is_gap = False
            else:
                return 0
        i += 1

    if "?" not in springs:
        return 0 if arrangement_cp else 1
    possib = 0
    index = springs.index("?")
    for replacement in ".#":
        possib += getPossibilities((springs[:index]+replacement+springs[index+1:], arrangement))
    return possib


def solve(data):  # solves the question
    solution = 0
    for i, record in enumerate(data):
        solution += getPossibilities(record)
        print(f"Line {i}")
    return solution


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
