file = open("input.txt").read().split("\n")
rules = []
myTicket = []
nearbytickets = []
invalid_rate = 0

index = file.index("")
for line in file[:index]:
    name = line.split(":")[0]
    allowed_numbers = line.split(":")[1].lstrip(" ")
    rules.append([name, allowed_numbers.split(" or ")[0], allowed_numbers.split(" or ")[1]])

myTicket = file[index + 2].split(",")

for ticket_line in file[index + 5:]:
    nearbytickets.append(ticket_line.split(","))

for ticket in nearbytickets:
    for number in ticket:
        valid = False
        for rule in rules:
            for i in range(1, 3):
                if int(rule[i].split("-")[0]) <= int(number) <= int(rule[i].split("-")[1]):
                    valid = True
        if not valid:
            invalid_rate += int(number)

print(invalid_rate)
