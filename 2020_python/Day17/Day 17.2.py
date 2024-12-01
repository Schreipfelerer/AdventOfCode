import copy

size_input = 8
generations = 6
size = generations + (size_input * 2) + 3

cube = [[[[False for x in range(size)] for y in range(size)] for z in range(size)] for w in range(size)]

with open("input.txt") as f:
    x = generations
    for line in f.readlines():
        y = generations
        for char in line:
            if char != "\n":
                if char == "#":
                    cube[x][y][generations][generations] = True
                y += 1
        x += 1

for i in range(6):
    print("Generation " + str(i + 1))
    cube_copy = copy.deepcopy(cube)
    for x in range(len(cube_copy)):
        for y in range(len(cube_copy[x])):
            for z in range(len(cube_copy[x][y])):
                for w in range(len(cube_copy[x][y][z])):

                    active_n = 0
                    for x_off in range(-1, 2):
                        for y_off in range(-1, 2):
                            for z_off in range(-1, 2):
                                for w_off in range(-1, 2):

                                    if 0 <= x + x_off < size:
                                        if 0 <= y + y_off < size:
                                            if 0 <= z + z_off < size:
                                                if 0 <= w + w_off < size:
                                                    if x_off != 0 or y_off != 0 or z_off != 0 or w_off != 0:

                                                        if cube_copy[x + x_off][y + y_off][z + z_off][w + w_off]:
                                                            active_n += 1

                    if cube_copy[x][y][z][w]:
                        if 3 < active_n or active_n < 2:
                            cube[x][y][z][w] = False
                    else:
                        if active_n == 3:
                            cube[x][y][z][w] = True

num = 0
for x in range(len(cube)):
    for y in range(len(cube[x])):
        for z in range(len(cube[x][y])):
            for w in range(len(cube[x][y][z])):
                if cube[x][y][z][w]:
                    num += 1
print(num)
