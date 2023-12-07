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
        value_bin = bin(int(value))[2:]
        unmasked_value_bin = (36-len(value_bin))*"0" + value_bin
        masked_value_bin = ""
        for i in range(36):
            if mask[i] != "X":
                masked_value_bin += mask[i]
            else:
                masked_value_bin += unmasked_value_bin[i]
        masked_value = int("0b"+masked_value_bin, 2)
        mem[index] = masked_value

print(mem)
print(sum(mem.values()))
