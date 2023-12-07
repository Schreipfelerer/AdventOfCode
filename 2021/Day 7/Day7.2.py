def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for num in lines[0].rstrip("\n").split(","):
        data.append(int(num))
    return data


def solve(data):  # solves the question
    min_fuel = None
    for i in range(min(data), max(data)+1):
        crabs = data[:]
        fuelcost = 0
        for crab in crabs:
            fuelcost += sum(range(1, abs(i-crab)+1))
        if not min_fuel or min_fuel > fuelcost:
            min_fuel = fuelcost
    return min_fuel


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
