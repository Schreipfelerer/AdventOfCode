def get_all_index(uib, m):
    for i in range(36):
        if m[i] == "X":
            return get_all_index(uib, m[:i] + "1" + m[i+1:]) + get_all_index(uib, m[:i] + "Z" + m[i+1:])

    mib = ""
    for i in range(36):
        if m[i] == "Z":
            mib += "0"
        if m[i] == "1":
            mib += "1"
        if m[i] == "0":
            mib += uib[i]
    return [mib]


f = open("input.txt").read().split("\n")

mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
mem = {}
for instruction in f:
    operation = instruction.split("=")[0].rstrip(" ")
    value = instruction.split("=")[1].lstrip(" ")

    if operation == "mask":
        mask = value

    if operation.startswith("mem"):
        index = operation[4:-1]
        index_bin = bin(int(index))[2:]
        unmasked_index_bin = (36-len(index_bin))*"0" + index_bin

        masked_indexes = get_all_index(unmasked_index_bin, mask)
        for masked_index in masked_indexes:
            mem[masked_index] = int(value)


print(sum(mem.values()))
