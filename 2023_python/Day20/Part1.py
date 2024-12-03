def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    broadcaster = []
    flipflops = {}
    conjunction = {}
    for line in lines:
        line = line[:-1]
        if not line:
            continue
        rightside = line.split(" -> ")[1].split(", ")
        if line.startswith("broadcast"):
            broadcast = rightside
        if line.startswith("%"):
            flipflops[line.split(" -> ")[0][1:]] = [False, rightside]
        if line.startswith("&"):
            conjunction[line.split(" -> ")[0][1:]] = [{}, rightside]

    for c_key, c in conjunction.items():
        for f_key, f in flipflops.items():
            if c_key in f[1]:
                c[0][f_key] = False
        for c2_key, c2 in conjunction.items():
            if c_key in c2[1]:
                c[0][c2_key] = False
    return (broadcast, flipflops, conjunction)


def solve(data):  # solves the question
    low_pulses = 0
    high_pulses = 0
    broadcast, flipflops, conjunction = data
    for i in range(1000):
        to_send = [("broadcast", Low)]
        while to_send:
            send = to_send.pop(0)

    
    return data


def main():
    lines = readInput(True)
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
