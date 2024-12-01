num = 0
with open("input.txt") as file:
    for each in file:
        char = each[each.find(' ') + 1]
        word = each[each.find(':') + 2:].rstrip("\n")
        try:
            a1 = word[int(each[0: each.find('-')]) - 1] == each[each.find(' ') + 1]
            a2 = word[int(each[each.find('-') + 1: each.find(' ')]) - 1] == each[each.find(' ') + 1]
            if a1 != a2:  # XOR Gate
                num += 1
        except IndexError:
            pass

print(num)
