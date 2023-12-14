c = []
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
                print(int(line))
