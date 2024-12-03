def readInput(use_example=False) -> list:  # Reads the Input cas be set to read from example.txt
    if use_example:
        with open('example.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def parseInput(lines):  # parses the input to the desired typ
    broadcast = []
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
    return broadcast, flipflops, conjunction


def solve(data):  # solves the question
    button_presses = 0
    broadcast, flipflops, conjunction = data
    while True:
        button_presses += 1
        to_send = [("broadcast", False, "button")]
        while to_send:
            to, signal, fro = to_send.pop(0)

            if to == "rx" and not signal:
                return button_presses

            if to == "broadcast":
                for s in broadcast:
                    to_send.append((s, signal, to))
            elif to in flipflops.keys():
                if signal:
                    continue
                f = flipflops[to]
                f[0] = not f[0]
                for s in f[1]:
                    to_send.append((s, f[0], to))
            elif to in conjunction.keys():
                c = conjunction[to]
                c[0][fro] = signal
                ss = not all(c[0].values())
                for s in c[1]:
                    to_send.append((s, ss, to))


def main():
    lines = readInput()
    data = parseInput(lines)
    print(solve(data))


if __name__ == "__main__":
    main()
