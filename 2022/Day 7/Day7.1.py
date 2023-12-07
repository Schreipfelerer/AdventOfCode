def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc, 'r') as f:
        return f.read().split("\n")


def parseInput(lines):  # parses the input to the desired typ
    path_list = []
    data = dict()
    for line in lines:
        line_sp = line.split(" ")
        if line_sp[0] == "$":
            if line_sp[1] == "cd":
                if line_sp[2] == "/":
                    path_list = []
                elif line_sp[2] == "..":
                    path_list.pop()
                else:
                    path_list.append(line_sp[2])
        else:
            current_dic = data
            for path in path_list:
                current_dic = current_dic[path]
            if line_sp[0] == "dir":
                if line_sp[1] not in current_dic.keys():
                    current_dic[line_sp[1]] = dict()
            else:
                current_dic[line_sp[1]] = int(line_sp[0])

    return data


def solve(data):  # solves the question
    n = getSize(data)
    size = 0 if n > 100000 else n
    for item in data.values():
        if type(item) == dict:
            size += solve(item)
    return size


def getSize(dicts):
    size = 0
    for item in dicts.values():
        if type(item) == dict:
            size += getSize(item)
        else:
            size += item
    return size


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
