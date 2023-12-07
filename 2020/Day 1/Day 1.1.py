c = []
with open("input.txt") as file:
    for line in file:
        c.append(int(line))


for each in c:
    for each2 in c:
        if each+each2 == 2020:
            print(str(each) + " * " + str(each2) + " = "+str(each*each2))
