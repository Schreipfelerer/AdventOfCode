c = []
with open("input.txt") as file:
    for line in file:
        c.append(line.rstrip("\n"))

dic = {}
col = []
for each in c:
    if each == "":
        col.append(dic)
        dic = {}
    else:
        for data in each.split(" "):
            point = data.split(":")
            dic[point[0]] = point[1]
col.append(dic)

valid = 0


def check_valid(p):
    try:
        passport["byr"]
        passport["iyr"]
        passport["eyr"]
        passport["hcl"]
        passport["hcl"]
        passport["ecl"]
        passport["pid"]
        passport["pid"]
        passport["hgt"]
        return True
    except KeyError:
        return False


for passport in col:
    if check_valid(passport):
        valid += 1

print(valid)
