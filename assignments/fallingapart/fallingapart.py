#David Sanders Falling Apart Kattis
def working(line1,line2):
    line2 = [ int(item) for item in line2]
    line2.sort(reverse = True)
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
    print(AliceScore, BobScore)
    return(AliceScore,BobScore)

def test():
    assert working("3", ["1","3","2"]) == (4,2), "error on test 1"
    assert working("1", ["100"]) == (100,0), "error on test 2"
    assert working("5", ["1","10","2","3","4"]) == (14, 6), "error on test 3"
    print("testing passed.")
    main()



def main():
    line1 = input()
    if (line1 == "TEST"):
        line2 = test()
    line2 = list(input().split())
    working(line1,line2)



    
main()