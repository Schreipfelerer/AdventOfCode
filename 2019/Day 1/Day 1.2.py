lines = open("input.txt").readlines()

total_fuel = 0
for line in lines:
    mass = int(line)
    fuel = int(mass / 3) - 2
    while fuel > 0:
        if fuel < 0:
            fuel = 0
        else:
            total_fuel += fuel
            fuel = int(fuel / 3) - 2

print(total_fuel)
