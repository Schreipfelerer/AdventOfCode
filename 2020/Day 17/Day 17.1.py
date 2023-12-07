import copy

size = 30

cube = [[[False for x in range(size)] for y in range(size)] for z in range(size)]

with open("input.txt") as f:
    x = size//2
    for line in f.readlines():
        y = size//2
        for char in line:
            if char != "\n":
                if char == "#":
                    cube[x][y][size//2] = True
                y += 1
        x += 1

for i in range(6):
    cube_copy = copy.deepcopy(cube)
    for x in range(len(cube_copy)):
        for y in range(len(cube_copy[x])):
            for z in range(len(cube_copy[x][y])):

                active_n = 0
                for x_off in range(-1, 2):
                    for y_off in range(-1, 2):
                        for z_off in range(-1, 2):

                            if 0 <= x + x_off < len(cube_copy):
                                if 0 <= y + y_off < len(cube_copy[x+x_off]):
                                    if 0 <= z + z_off < len(cube_copy[x+x_off][y+y_off]):
                                        if x_off != 0 or y_off != 0 or z_off != 0:

                                            if cube_copy[x+x_off][y+y_off][z+z_off]:
                                                active_n += 1

                if cube_copy[x][y][z]:
                    if 3 < active_n or active_n < 2:
                        cube[x][y][z] = False
                else:
                    if active_n == 3:
                        cube[x][y][z] = True

num = 0
for x in range(len(cube)):
    for y in range(len(cube[x])):
        for z in range(len(cube[x][y])):
            if cube[x][y][z]:
                num += 1
print(num)
