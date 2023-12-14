num = 0
with open("input.txt") as file:
    for each in file:
        char = each[each.find(' ') + 1]
        word = each[each.find(':') + 2:].rstrip("\n")
        try:
            a1 = int(each[0: each.find('-')])
            a2 = int(each[each.find('-') + 1: each.find(' ')])
            if a1 <= word.count(char) <= a2:
                num += 1
        except IndexError:
            pass

print(num)
