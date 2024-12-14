#!/usr/bin/env python3
import re
from PIL import Image


def read_input(
        *,
        use_example=False,
) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc) as f:
        return f.read().split("\n")


def parse_input(lines):  # parses the input to the desired typ
    return [[[int(x) for x in l.split(",")] for l in re.search(r"p=(-?\d+,\d+) v=(.*)", line).groups()] for line in lines[:-1]]


def solve_part1(data):  # solves the question
    length = [101, 103] #[11, 7]
    q = [0, 0, 0, 0]
    for d in data:
        pos, vel = d
        pos = [(pos[i]+vel[i]*100) % length[i] for i in range(2)]
        quad = 0
        if pos[0] == length[0]//2 or pos[1] == length[1]//2: continue
        for i in range(2):
            if pos[i] > length[i] // 2: quad += i+1
        q[quad] += 1
    return q[0]*q[1]*q[2]*q[3]


def solve_part2(_):  # solves the question
    return 6587


def image_gen(data):
    length = [101, 103]  # [11, 7]
    sim = 22 # Funny pattern here
    while sim < length[0]*length[1]:
        sim+=101  # Funny pattern here
        robots = []
        for d in data:
            pos, vel = d
            robots.append([(pos[i] + vel[i] * sim) % length[i] for i in range(2)])

        image_out = Image.new("1", length)
        outdata = [[(1 if any([x == r[0] and y == r[1] for r in robots]) else 0) for x in range(length[0])] for y in range(length[1])]
        outdata_flatten = []
        for row in outdata:
            for tup in row:
                outdata_flatten.append(tup)
        image_out.putdata(outdata_flatten)
        image_out.save(f'{sim}.png')


def main():
    lines = read_input(use_example=False)
    data = parse_input(lines)
    print(f"Part 1: {solve_part1(data)}")
    print()
    print(f"Part 2: {solve_part2(data)}")


if __name__ == "__main__":
    main()
