c = []
num = 0
with open("input.txt") as file:
    for line in file:
        c.append(int(line))
        if len(c) > 25:
            bol = False
            for i in c[-26:-1]:
                for j in c[-26:-1]:
                    if j + i == int(line):
                        bol = True
            if not bol:
                num = int(line)

for i in range(len(c)):
    for j in range(i):
        if sum(c[j:i + 1]) == num:
            print(min(c[j:i + 1]) + max(c[j:i + 1]))
