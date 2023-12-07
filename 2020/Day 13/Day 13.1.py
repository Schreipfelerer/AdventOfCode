time = None
bus = []
with open("input.txt") as file:
    time = int(file.readline().rstrip("\n"))
    tmp = file.readline().rstrip("\n").split(",")
    for each in tmp:
        if each != "x":
            bus.append(int(each))

smallest = time-1
for num in bus:
    if num - (time % num) < smallest - (time % smallest):
        smallest = num

print((smallest - (time % smallest)) * smallest)
