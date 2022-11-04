#David Sanders Falling Apart Kattis

line1 = input()
line2 = list(input().split())


line2.sort()

AliceScore = 0
BobScore = 0
AliceTurn = True
i = 0
while i < int(line1): 
    if (AliceTurn):
        AliceScore = AliceScore + int(line2[i])
    else:
        BobScore = BobScore + int(line2[i])
    i = i + 1
    AliceTurn = not(AliceTurn)

print(str(AliceScore) + " " + str(BobScore))
