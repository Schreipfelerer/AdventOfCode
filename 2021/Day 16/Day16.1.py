def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = lines[0].rstrip("\n")

    return data


def solve(data):  # solves the question
    return decode("0" * (4 - len(format(int(data[0], base=16), "b"))) + format(int(data, base=16), "b"))[0]


def decode(b):
    version_sum = 0
    binary = b
    version = int(binary[:3], base=2)
    version_sum += version
    id_number = int(binary[3:6], base=2)
    binary = binary[6:]

    if id_number == 4:
        datastream = True
        literal = []
        while datastream:
            bits = binary[:5]
            if bits.startswith("0"):
                datastream = False
            binary = binary[5:]
            bits = bits[1:]
            literal.append(bits)
        value = int("".join(literal), 2)

    if id_number != 4:
        len_type_id = binary[0]
        binary = binary[1:]
        length = 0
        if len_type_id == "0":
            length = int(binary[:15], 2)
            binary = binary[15:]
            original = binary
            while len(original)-len(binary) < length:
                ret = decode(binary)
                version_sum += ret[0]
                binary = ret[1]
        if len_type_id == "1":
            length = int(binary[:11], 2)
            binary = binary[11:]
            subs = 0
            while subs < length:
                subs += 1
                ret = decode(binary)
                version_sum += ret[0]
                binary = ret[1]

    return [version_sum, binary]


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
