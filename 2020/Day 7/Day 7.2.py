class Rule:
    con_rules = []
    color = ""

    def __init__(self, string_line):
        self.con_rules = []
        words = string_line.split(" ")
        self.color = words[0] + " " + words[1]
        if words[4] != "no":
            i = 4
            while words[i + 3].endswith(","):
                self.con_rules.append([int(words[i]), str(words[i + 1] + " " + words[i + 2])])
                i += 4
            self.con_rules.append([int(words[i]), str(words[i + 1] + " " + words[i + 2])])

    def __str__(self):
        return self.color + ": " + str(self.con_rules)


rules = []
with open("input.txt") as file:
    for line in file:
        rule = Rule(line.rstrip("\n"))
        rules.append(rule)


def does_contains(bag):
    for element in rules:
        if element.color == bag:
            num = 1
            for con_rule in element.con_rules:
                num += con_rule[0] * does_contains(con_rule[1])
            return num
    print("None found")


print(does_contains("shiny gold")-1)