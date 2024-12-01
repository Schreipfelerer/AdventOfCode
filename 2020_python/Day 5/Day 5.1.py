highest = 0
with open("input.txt") as file:
    for seat in file:
        id = 0
        for fb in range(7):
            if seat[fb] == "B":
                id += (2 ** (6 - fb) * 8)
        for rl in range(3):
            if seat[rl + 7] == "R":
                id += 2 ** (2 - rl)
        if highest < id:
            highest = id
    print(highest)
