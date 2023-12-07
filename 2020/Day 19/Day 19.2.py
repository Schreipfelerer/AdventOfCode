filelines = open("input.txt").read().split("\n")

rules_str = filelines[:filelines.index("")]
testlines = filelines[filelines.index("")+1:]
max_len = max(testlines, key=len)


rules = [None]*len(rules_str)
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

            if rule_index == 8:
                safed_rules = set()
                for i in range(1, 10):
                    safed_rules.add("0"*i*8)
                rules[8] = safed_rules
                return

            if rule_index == 11:
                safed_rules = set()
                for i in range(1, 10):
                    safed_rules.add("0"*i*16)
                rules[11] = safed_rules
                return

            saved_rules = set()
            rules_to_add = set()
            for dependecie in dependencies:
                if dependecie == "|":
                    saved_rules = saved_rules.union(rules_to_add)
                    rules_to_add = set()
                elif len(rules_to_add) == 0:
                    rules_to_add = rules[int(dependecie)]
                else:
                    rules_to_add = add_multiply_set(rules_to_add, rules[int(dependecie)])

            rules[rule_index] = set(saved_rules.union(rules_to_add))


def add_multiply_set(set_a, set_b):
    if len(set_a) == 0:
        return set_b
    if len(set_b) == 0:
        return set_a
    new_rules = set()
    for rule_1 in set_a:
        for rule_2 in set_b:
            new_rule = rule_1 + rule_2
            new_rules.add(new_rule)
    return new_rules


match_rule(0)

passing_lines = 0
for testline in testlines:
    for rule in rules[0]:
        stop = False
        if len(testline) != len(rule):
            stop = True
        else:
            for i in range(len(testline)):
                if testline[i] == rule[i] or rule[i] == "0":
                    pass
                else:
                    stop = True
        if not stop:
            passing_lines += 1
            break

print(passing_lines)

