c = [0]
with open("input.txt") as file:
    for line in file:
        c.append(int(line.rstrip("\n")))

posebillites = []
c.sort()
for i in range(len(c)):
    pos = 1 if i == 0 else 0
    for j in range(1, 4):
        if i - j >= 0 and (c[i] - c[i - j]) <= 3:
            pos += posebillites[i - j]
    posebillites.append(pos)

print(posebillites[-1])
