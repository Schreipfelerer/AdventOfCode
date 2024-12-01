filelines = open("input.txt").read().split("\n")

door_publickey = int(filelines[0])
card_publickey = int(filelines[1])


def transform(value, subjectnumber):
    value *= subjectnumber
    value %= 20201227
    return value


def findloopsize(public_key):
    loopsize = 0

    testkey = 1
    while public_key != testkey:
        testkey = transform(testkey, 7)
        loopsize += 1
    return loopsize


door_loopsize = findloopsize(door_publickey)
card_loopsize = findloopsize(card_publickey)

encryption_key = 1
for i in range(card_loopsize):
    encryption_key = transform(encryption_key, door_publickey)

print(encryption_key)
