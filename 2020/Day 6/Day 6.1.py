sum = 0
chars = set()
with open("input.txt") as file:
    for line in file:
        line = line.rstrip("\n")
        if line == "":
            sum += len(chars)
            chars = set()
        else:
            for char in line:
                chars.add(char)

print(sum)
