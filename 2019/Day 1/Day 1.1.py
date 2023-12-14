lines = open("input.txt").readlines()

total_fuel = 0
for line in lines:
    mass = int(line)
    total_fuel += int(mass / 3) - 2

print(total_fuel)
