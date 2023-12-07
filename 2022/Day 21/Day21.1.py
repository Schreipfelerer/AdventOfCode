def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for line in lines:
        data.append(line.split(": "))
    return data


def solve(data):  # solves the question
    monkeys = dict()
    for monkey in data[:]:
        if monkey[1].isnumeric():
            monkeys[monkey[0]] = int(monkey[1])
            data.remove(monkey)
        else:
            monkey[1] = monkey[1].split()

    while "root" not in monkeys.keys():
        for monkey in data[:]:
            if monkey[1][0] in monkeys.keys() and monkey[1][2] in monkeys.keys():
                match monkey[1][1]:
                    case "+":
                        def op(a, b): return a + b
                    case "-":
                        def op(a, b): return a - b
                    case "*":
                        def op(a, b): return a * b
                    case "/":
                        def op(a, b): return a // b
                    case _:
                        def op(): assert False
                monkeys[monkey[0]] = op(monkeys[monkey[1][0]], monkeys[monkey[1][2]])
                data.remove(monkey)

    return monkeys["root"]


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
