sum = 0
duplis = "Reset me"
with open("input.txt") as file:
    for line in file:
        line = line.rstrip("\n")
        if line == "":
            sum += len(duplis)
            duplis = "Reset me"
        else:
            if duplis == "Reset me":
                duplis = list(line)
            else:
                duplis = [dup for dup in duplis if dup in line]

print(sum)
