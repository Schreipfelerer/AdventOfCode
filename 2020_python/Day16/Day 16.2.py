file = open("input.txt").read().split("\n")
rules = []
myTicket = None
nearbytickets = []
valid_nearbytickets = []

index = file.index("")
for line in file[:index]:
    name = line.split(":")[0]
    allowed_numbers = line.split(":")[1].lstrip(" ")
    rules.append(
        [name, allowed_numbers.split(" or ")[0], allowed_numbers.split(" or ")[1], list(range(len(file[:index])))])

myTicket = file[index + 2].split(",")

for ticket_line in file[index + 5:]:
    nearbytickets.append(ticket_line.split(","))

for ticket in nearbytickets:
    ticket_valid = True
    for number in ticket:
        valid = False
        for rule in rules:
            for i in range(1, 3):
                if int(rule[i].split("-")[0]) <= int(number) <= int(rule[i].split("-")[1]):
                    valid = True
        if not valid:
            ticket_valid = False
    if ticket_valid:
        valid_nearbytickets.append(ticket)

for valid_ticket in valid_nearbytickets:
    for i in range(len(valid_ticket)):
        for rule in rules:
            if not ((int(rule[1].split("-")[0]) <= int(valid_ticket[i]) <= int(rule[1].split("-")[1])) or
                    (int(rule[2].split("-")[0]) <= int(valid_ticket[i]) <= int(rule[2].split("-")[1]))):
                if i in rule[3]:
                    rule[3].remove(i)

changed = True
while changed:
    changed = False
    for i in range(len(rules)):
        if len(rules[i][3]) == 1:
            for rule in rules:
                if rule[0] != rules[i][0]:
                    if rules[i][3][0] in rule[3]:
                        rule[3].remove(rules[i][3][0])
                        changed = True

result = 1
for rule in rules:
    if rule[0].startswith("departure"):
        for i in range(len(rules)):
            if i == rule[3][0]:
                result *= int(myTicket[i])

print(result)
