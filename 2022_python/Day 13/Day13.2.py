from functools import cmp_to_key


def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for i in range(0, len(lines), 3):
        list_stack = []
        latest_pop = None
        for j in (0, 1):
            for k, char in enumerate(lines[i + j]):
                if char == "[":
                    new_list = []
                    if list_stack:
                        list_stack[-1].append(new_list)
                    list_stack.append(new_list)
                elif char == "]":
                    latest_pop = list_stack.pop()
                elif char != ",":
                    if lines[i + j][k - 1] == "[" or lines[i + j][k - 1] == ",":
                        int_len = 1
                        while lines[i + j][k + int_len] != "," and lines[i + j][k + int_len] != "]":
                            int_len += 1
                        list_stack[-1].append(int(lines[i + j][k:k + int_len]))
            data.append(latest_pop)
    return data


def evaluate(param, param1):
    if type(param) == int and type(param1) == int:
        if param < param1:
            return -1
        if param == param1:
            return 0
        if param > param1:
            return 1
    if type(param) == list and type(param1) == list:
        for i in range(min(len(param), len(param1))):
            result = evaluate(param[i], param1[i])
            if result != 0:
                return result
        return evaluate(len(param), len(param1))
    return evaluate(param, [param1]) if type(param1) == int else evaluate([param], param1)


def solve(data):  # solves the question
    data.append([[2]])
    data.append([[6]])
    data.sort(key=cmp_to_key(evaluate))
    decoder = 1
    for i, packet in enumerate(data):
        if packet == [[2]] or packet == [[6]]:
            decoder *= i + 1
    return decoder


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
