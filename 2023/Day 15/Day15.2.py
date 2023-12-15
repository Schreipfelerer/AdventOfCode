def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    return lines[0].rstrip("\n").split(",")


def solve(data):  # solves the question
    boxes = [[] for _ in range(256)]
    for string in data:
        index_op = max(string.find("="), string.find("-"))
        label = string[:index_op]
        hash_value = get_hash(label)
        box_label = [x.split(" ")[0] for x in boxes[hash_value]]
        if string[index_op] == "=":
            if label in box_label:
                boxes[hash_value][box_label.index(label)] = string.replace("=", " ")
            else:
                boxes[hash_value].append(string.replace("=", " "))
        else:
            if label in box_label:
                boxes[hash_value].pop(box_label.index(label))

    focus_power = 0
    for i in range(256):
        for j, box in enumerate(boxes[i]):
            focus_power += (i + 1) * (j + 1) * int(box.split(" ")[1])

    return focus_power


def get_hash(string):
    hash_value = 0
    for char in string:
        hash_value += ord(char)
        hash_value *= 17
        hash_value %= 256
    return hash_value


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
