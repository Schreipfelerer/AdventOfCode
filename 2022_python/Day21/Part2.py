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
    return getX("root", True, data)


def makeString(m, data):
    if m == "humn":
        return "x"
    for monkey in data:
        if monkey[0] == m:
            if monkey[1].isnumeric():
                return monkey[1]
            else:
                ms = monkey[1].split(" ")
                if m == "root":
                    ms[1] = "=="
                if ms[1] == "/":
                    ms[1] = "//"
                return "(" + makeString(ms[0], data) + ")" + ms[1] + "(" + makeString(ms[2], data) + ")"


def getX(m, solution, data):
    for monkey in data:
        if m == monkey[0]:
            if m == "humn":
                return solution
            m1 = makeString(monkey[1].split(" ")[0], data)
            m2 = makeString(monkey[1].split(" ")[2], data)
            swapped = False
            if "x" not in m1:
                m1, m2 = m2, m1
                swapped = True

            if m == "root":
                return getX(monkey[1].split(" ")[0 if not swapped else 2], eval(m2), data)
            else:
                match monkey[1].split(" ")[1]:
                    case "+":
                        def op(a, b):
                            return b - a
                    case "-":
                        if not swapped:
                            def op(a, b):
                                return a + b
                        else:
                            def op(a, b):
                                return a - b
                    case "*":
                        def op(a, b):
                            return b // a
                    case "/":
                        if not swapped:
                            def op(a, b):
                                return a * b
                        else:
                            def op(a, b):
                                return a // b
                    case _:
                        def op():
                            assert False
                newsol = op(eval(m2), solution)
                return getX(monkey[1].split(" ")[0 if not swapped else 2], newsol, data)


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
