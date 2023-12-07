def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    data = []
    for line in lines:
        region = [line.split(" ")[0] == "on"]
        line = line.split(" ")[1].rstrip("\n")
        for segment in line.split(","):
            segment = segment.lstrip("xyz=")
            region.append((int((segment.split("..")[0])), int((segment.split("..")[1]))))
        data.append(region)
    return data


def solve(data):  # solves the question
    turned_on = []
    for step in data:
        if step[0]:
            add(turned_on, step[1:])
        else:
            sub(turned_on, step[1:])

    num_on = 0
    for cube in turned_on:
        num_on += (cube[0][1] - cube[0][0] + 1) * (cube[1][1] - cube[1][0] + 1) * (cube[2][1] - cube[2][0] + 1)
    return num_on


def add(cube_list, cube):
    for cube_l in cube_list:
        if intersects(cube, cube_l):
            if not is_inside(cube, cube_l):
                for new_cube in newCubes(cube, cube_l):
                    add(cube_list, new_cube)
            return
    cube_list.append(cube)
    return


def sub(cube_list, cube):
    for cube_l in cube_list[:]:
        if intersects(cube, cube_l):
            cube_list.remove(cube_l)
            if not is_inside(cube_l, cube):
                for new_cube in newCubes(cube_l, cube):
                    add(cube_list, new_cube)
                sub(cube_list, cube)
                return
    return


def intersects(cube1, cube2):
    return (cube2[0][0] <= cube1[0][1] and cube2[0][1] >= cube1[0][0]) and \
           (cube2[1][0] <= cube1[1][1] and cube2[1][1] >= cube1[1][0]) and \
           (cube2[2][0] <= cube1[2][1] and cube2[2][1] >= cube1[2][0])


def is_inside(cube1, cube2):
    return cube2[0][0] <= cube1[0][0] and cube2[0][1] >= cube1[0][1] and cube2[1][0] <= cube1[1][0] and \
           cube2[1][1] >= cube1[1][1] and cube2[2][0] <= cube1[2][0] and cube2[2][1] >= cube1[2][1]


def newCubes(cube_to_div, cube):
    x_sec = []
    y_sec = []
    z_sec = []
    if cube_to_div[0][0] < cube[0][0]:
        x_sec.append((cube_to_div[0][0], cube[0][0]-1))
    if cube_to_div[0][1] > cube[0][1]:
        x_sec.append((cube[0][1]+1, cube_to_div[0][1]))
    x_sec.append((max(cube_to_div[0][0], cube[0][0]), min(cube_to_div[0][1], cube[0][1])))

    if cube_to_div[1][0] < cube[1][0]:
        y_sec.append((cube_to_div[1][0], cube[1][0]-1))
    if cube_to_div[1][1] > cube[1][1]:
        y_sec.append((cube[1][1]+1, cube_to_div[1][1]))
    y_sec.append((max(cube_to_div[1][0], cube[1][0]), min(cube_to_div[1][1], cube[1][1])))

    if cube_to_div[2][0] < cube[2][0]:
        z_sec.append((cube_to_div[2][0], cube[2][0]-1))
    if cube_to_div[2][1] > cube[2][1]:
        z_sec.append((cube[2][1]+1, cube_to_div[2][1]))
    z_sec.append((max(cube_to_div[2][0], cube[2][0]), min(cube_to_div[2][1], cube[2][1])))

    return [(x, y, z) for x in x_sec for y in y_sec for z in z_sec]


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
