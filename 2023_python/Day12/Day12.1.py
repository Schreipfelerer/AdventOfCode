# import time


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
        data.append(datapoint)
    return data


memom = {}


def getPossibilities(record):
    springs, arrangement = record

    if not arrangement:
        if "#" not in springs:
            return 1
        else:
            return 0

    springs = springs.lstrip(".").rstrip(".")

    if len(arrangement) == 1 and len(springs) == arrangement[0]:
        return 0 if "." in springs else 1

    if len(springs) < sum(arrangement) + len(arrangement) - 1:
        return 0

    key = ",".join([str(x) for x in arrangement]) + springs

    if key in memom.keys():
        return memom[key]

    possib = 0
    biggest = max(arrangement)
    length = len(springs)

    for i in range(length - biggest + 1):
        if "." not in springs[i:i + biggest]:
            if i == 0 or springs[i - 1] != "#":
                if i + biggest == length or springs[i + biggest] != "#":
                    multi_possib = getPossibilities(
                        (springs[:max(0, i - 1)], arrangement[:arrangement.index(biggest)]))
                    if multi_possib:
                        possib += multi_possib * getPossibilities(
                            (springs[i + biggest + 1:], arrangement[arrangement.index(biggest) + 1:]))

    memom[key] = possib
    return possib


def solve(data):  # solves the question
    solution = 0
    # old_time = time.time_ns()
    for i, record in enumerate(data):
        sol = getPossibilities(record)
        solution += sol
        # print(f"Line {i}: in {(time.time_ns()-old_time)/1000000:.2f} ms solution:{sol}")
        # old_time = time.time_ns()

    # print(f"Solved in: {(time.time_ns() - old_time) / 1000000:.2f} ms")
    return solution


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
