inst = []
with open("input.txt") as file:
    for line in file:
        inst.append([line[:3], int(line[4:]), False])

i = 0
acc = 0
while not inst[i][2]:
    inst[i][2] = True
    if inst[i][0] == "acc":
        acc += inst[i][1]
    elif inst[i][0] == "jmp":
        i += inst[i][1]-1
    i += 1

print(acc)
