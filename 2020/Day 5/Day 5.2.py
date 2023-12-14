highest = 0
c = []
with open("input.txt") as file:
    for seat in file:
        id = 0
        for fb in range(7):
            if seat[fb] == "B":
                id += (2 ** (6 - fb) * 8)
                pass
        for rl in range(3):
            if seat[rl + 7] == "R":
                id += 2 ** (2 - rl)
        c.append(id)

c.sort()
for each in range(len(c) - 1):
    if c[each] + 2 == c[1 + each]:
        print(c[each] + 1)
