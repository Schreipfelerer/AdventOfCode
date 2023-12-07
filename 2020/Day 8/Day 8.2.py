inst = []
with open("input.txt") as file:
    for line in file:
        operation = line[:3]
        arg = int(line[4:])
        inst.append([operation, arg, False])

j = 0
acc = 0
try:
    while True:
        if inst[j][0] == "jmp":
            inst[j][0] = "nop"
            tmp = "jmp"
        elif inst[j][0] == "nop":
            inst[j][0] = "jmp"
            tmp = "nop"
        else:
            tmp = "acc"
        i = 0
        acc = 0
        while not inst[i][2]:
            inst[i][2] = True
            if inst[i][0] == "acc":
                acc += inst[i][1]
            elif inst[i][0] == "jmp":
                i += inst[i][1]-1
            i += 1
        for i in range(len(inst)):
            inst[i][2] = False
        inst[j][0] = tmp
        j += 1

except IndexError:
    print(acc)
