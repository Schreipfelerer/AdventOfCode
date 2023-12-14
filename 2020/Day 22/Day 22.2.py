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


def playRound(cards1, cards2):
    previousRounds = []
    while len(cards1) != 0 and len(cards2) != 0:
        if [cards1[:], cards2[:]] in previousRounds:
            cards2.clear()
            break
        else:
            previousRounds.append([cards1[:], cards2[:]])

        if cards1[0] < len(cards1) and cards2[0] < len(cards2):
            winner = playRound(cards1[1:cards1[0] + 1], cards2[1:cards2[0] + 1])
        elif cards1[0] > cards2[0]:
            winner = "P1"
        else:
            winner = "P2"

        if winner == "P1":
            cards1.append(cards1[0])
            cards1.remove(cards1[0])
            cards1.append(cards2[0])
            cards2.remove(cards2[0])
        else:
            cards2.append(cards2[0])
            cards2.remove(cards2[0])
            cards2.append(cards1[0])
            cards1.remove(cards1[0])

    return "P1" if len(cards2) == 0 else "P2"


playRound(Player1cards, Player2cards)
winningCards = Player1cards + Player2cards
win = 0
for i in range(1, len(winningCards) + 1):
    win += i * winningCards[len(winningCards) - i]
print(win)
