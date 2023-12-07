c = []
with open("input.txt") as file:
    for line in file:
        c.append(int(line.rstrip("\n")))

num = [0, 0, 0]
c.sort()
for i in range(len(c)):
    dif = c[i] if i == 0 else c[i]-c[i - 1]
    num[dif - 1] += 1

print(num[0]*(num[2]+1))
