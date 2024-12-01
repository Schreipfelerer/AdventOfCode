filelines = open("input.txt").read().split("\n")

Player1cards = []
Player2cards = []

Player1FullFlag = False
for line in filelines:  # Parse Input
    if not line.startswith("Player"):
        if line == "":
            Player1FullFlag = True
        elif not Player1FullFlag:
            Player1cards.append(int(line))
        else:
            Player2cards.append(int(line))

while len(Player1cards) != 0 and len(Player2cards) != 0:
    if Player1cards[0] > Player2cards[0]:
        Player1cards.append(Player1cards[0])
        Player1cards.remove(Player1cards[0])
        Player1cards.append(Player2cards[0])
        Player2cards.remove(Player2cards[0])
    else:
        Player2cards.append(Player2cards[0])
        Player2cards.remove(Player2cards[0])
        Player2cards.append(Player1cards[0])
        Player1cards.remove(Player1cards[0])

winningCards = Player1cards + Player2cards
win = 0
for i in range(1, len(winningCards) + 1):
    win += i * winningCards[len(winningCards) - i]
print(win)
