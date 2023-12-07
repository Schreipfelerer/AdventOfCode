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
        if not 1920 <= int(passport["byr"]) <= 2002:
            return False
        if not 2010 <= int(passport["iyr"]) <= 2020:
            return False
        if not 2020 <= int(passport["eyr"]) <= 2030:
            return False
        if not passport["hcl"][0] == "#":
            return False
        if not len(passport["hcl"]) == 7:
            return False
        for char in passport["hcl"][1:]:
            if not (char == "a" or char == "b" or char == "c" or char == "d" or char == "e" or char == "f" or char == "0" or char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9"):
                return False
        if not (passport["ecl"] == "amb" or passport["ecl"] == "blu" or passport["ecl"] == "brn" or passport["ecl"] == "gry" or passport["ecl"] == "grn" or passport["ecl"] == "hzl" or passport["ecl"] == "oth"):
            return False
        if not len(passport["pid"]) == 9:
            return False
        int(passport["pid"])
        if passport["hgt"][-2:] == "cm":
            if not 150 <= int(passport["hgt"][:-2]) <= 193:
                return False
        elif passport["hgt"][-2:] == "in":
            if not 59 <= int(passport["hgt"][:-2]) <= 76:
                return False
        else:
            return False
        return True
    except KeyError:
        return False


for passport in col:
    if check_valid(passport):
        valid += 1


print(valid)
