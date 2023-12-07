rules = []
with open("input.txt") as file:
    for line in file:
        rule = []
        line = line.rstrip("\n")
        words = line.split(" ")
        rule.append(words[0]+" "+words[1])
        if words[4] != "no":
            i = 5
            while words[i+2].endswith(","):
                rule.append(words[i] + " " + words[i+1])
                i += 4
            rule.append(words[i] + " " + words[i + 1])
        rules.append(rule)

temp = []
possibleBags = ["shiny gold"]
while temp != possibleBags:
    temp = possibleBags[:]
    for rule in rules:
        for bag in rule[1:]:
            for p_bag in possibleBags:
                if bag == p_bag:
                    if rule[0] not in possibleBags:
                        possibleBags.append(rule[0])

print(len(possibleBags)-1)
