filelines = open("example.txt").read().split("\n")

rules_str = filelines[:filelines.index("")]
testlines = filelines[filelines.index("") + 1:]

rules = [None] * len(rules_str)
for i in range(len(rules_str)):
    rules[int(rules_str[i].split(": ")[0])] = rules_str[i].split(": ")[1]


def match_rule(rule_index: int):
    rule = rules[rule_index]
    if type(rule) == str:
        if rule.startswith("\""):
            rules[rule_index] = {rule[1]}
        else:
            dependencies = rule.split(" ")
            for dependecie in dependencies:
                if dependecie != "|":
                    if type(rules[int(dependecie)]) == str:
                        match_rule(int(dependecie))

            saved_rules = set()
            rules_to_add = set()
            for dependecie in dependencies:
                if dependecie == "|":
                    saved_rules = saved_rules.union(rules_to_add)
                    rules_to_add = set()
                elif len(rules_to_add) == 0:
                    rules_to_add = rules[int(dependecie)]
                else:
                    new_rules = set()
                    for rule_1 in rules_to_add:
                        for rule_2 in rules[int(dependecie)]:
                            new_rule = rule_1 + rule_2
                            new_rules.add(new_rule)

                    rules_to_add = new_rules
            rules[rule_index] = set(saved_rules.union(rules_to_add))


match_rule(0)

passing_lines = 0
for testline in testlines:
    if testline in rules[0]:
        passing_lines += 1

print(passing_lines)
