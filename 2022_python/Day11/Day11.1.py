def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    data = []
    monkey = []
    for line in lines:
        line = line.lstrip()
        if line.startswith("Monkey"):
            monkey = []
        if line.startswith("Starting"):
            monkey.append([])
            for item in line.split(": ")[1].split(", "):
                monkey[-1].append(int(item))
        if line.startswith("Operation"):
            op = line.split(" = ")[1]
            if "+" in op:
                if op.split(" ")[2] == "old":
                    monkey.append(lambda a, b: 2 * a)
                else:
                    monkey.append(lambda a, b: a + int(b))
            else:
                if op.split(" ")[2] == "old":
                    monkey.append(lambda a, b: a * a)
                else:
                    monkey.append(lambda a, b: a * int(b))
            monkey.append(op.split(" ")[2])
        if line.startswith("Test"):
            monkey.append(int(line.split("by ")[1]))
        if line.startswith("If true"):
            monkey.append(int(line.split("monkey ")[1]))
        if line.startswith("If false"):
            monkey.append(int(line.split("monkey ")[1]))
        if not line:
            monkey.append(0)
            data.append(monkey)
    monkey.append(0)
    data.append(monkey)
    return data


def solve(data):  # solves the question
    for _ in range(20):
        for monkey in data:
            while monkey[0]:
                monkey[6] += 1
                worry = monkey[0].pop(0)
                worry = monkey[1](worry, monkey[2])
                worry = worry // 3
                new_monke = monkey[4] if worry % monkey[3] == 0 else monkey[5]
                data[new_monke][0].append(worry)

    high = [0, 0]
    for monkey in data:
        high.append(monkey[6])
        high.sort()
        high = high[1:]
    return high[0] * high[1]


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
