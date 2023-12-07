def solve(expression):
    if len(expression) == 1:
        return expression
    elif expression[0].count("(") + expression[2].count("(") == 0:
        if expression[1] == "+":
            return solve([str(int(expression[0]) + int(expression[2]))] + expression[3:])
        elif expression[1] == "*":
            return solve([str(int(expression[0]) * int(expression[2]))] + expression[3:])

    start = 2
    if expression[0].startswith("("):
        start = 0
    end = start
    num_open = expression[start].count("(")
    num_close = expression[start].count(")")
    while num_open > num_close:
        end += 2
        num_open += expression[end].count("(")
        num_close += expression[end].count(")")
    return solve(expression[:start] + solve([expression[start][1:]] + expression[start + 1:end] + [expression[end][:-1]]) + expression[end + 1:])


result_list = []
with open("input.txt") as f:
    for line in f.readlines():
        line = line.rstrip("\n")
        line_list = line.split(" ")
        result_list.append(int(solve(line_list)[0]))
print(sum(result_list))
