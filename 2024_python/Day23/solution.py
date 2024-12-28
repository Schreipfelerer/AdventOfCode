#!/usr/bin/env python3
def read_input(
    *,
    use_example=False,
) -> list:  # Reads the Input cas be set to read from example.txt
    file_loc = "example.txt" if use_example else "input.txt"
    with open(file_loc) as f:
        return f.read().split("\n")


def parse_input(lines):  # parses the input to the desired typ
    return [x.split("-") for x in lines[:-2]]


def bors_kerbosch_v2(r, p, x, g, c):
    if len(p) == 0 and len(x) == 0:
        if len(r) > 2:
            c.append(sorted(r))
        return

    d, pivot = max([(len(g[v]), v) for v in p.union(x)])

    for v in p.difference(g[pivot]):
        bors_kerbosch_v2(r.union({v}), p.intersection(g[v]), x.intersection(g[v]), g, c)
        p.remove(v)
        x.add(v)


def solve_part1(data):  # solves the question
    vertices = {xs for x in data for xs in x}
    graph = {}
    for v in vertices:
        graph[v] = [d[(d.index(v) + 1) % 2] for d in data if v in d]

    sets = 0
    vv = list(vertices)
    for i, v1 in enumerate(vv):
        for j, v2 in enumerate(vv[i + 1 :]):
            if v2 not in graph[v1]:
                continue
            for v3 in vv[i + j + 1:]:
                if (
                    (v1.startswith("t") or v2.startswith("t") or v3.startswith("t"))
                    and v3 in graph[v2]
                    and v3 in graph[v1]
                ):
                    sets += 1
    return sets


def solve_part2(data):  # solves the question
    vertices = {xs for x in data for xs in x}
    graph = {}
    for v in vertices:
        graph[v] = [d[(d.index(v) + 1) % 2] for d in data if v in d]
    c = []

    bors_kerbosch_v2(set(), vertices, set(), graph, c)

    largest = max([(len(cs), cs) for cs in c])
    return ",".join(sorted(largest[1]))


def main():
    lines = read_input(use_example=False)
    print(f"Part 1: {solve_part1(parse_input(lines))}")
    print()
    print(f"Part 2: {solve_part2(parse_input(lines))}")


if __name__ == "__main__":
    main()
