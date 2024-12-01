bus_list = []
every_x = 1
firstnum = 1
i = 0
with open("input.txt") as file:
    tmp = file.readlines()[-1].rstrip("\n").split(",")
    for bus in tmp:
        if bus != "x":
            while (firstnum + i) % int(bus) != 0:
                firstnum += every_x
            every_x *= int(bus)
        i += 1

print(firstnum)
