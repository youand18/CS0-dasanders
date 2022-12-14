#David Sanders Avion CIA ping detection code





def FBIcheck(pingStr):
    i = 0
    for char in pingStr:
        if (char == "F"):
            if (i < len(pingStr)-2):
                if (pingStr[i+1] == "B" and pingStr[i+2] == "I"):
                    return True
        i = i + 1    
    return False

def main():
    pings = []#[input() for _ in range(5)]
    i = 1
    goodPingLocations = []
    atLeastOne = False
    for ping in pings:
        if (FBIcheck(ping)):
            goodPingLocations.append(str(i))
            atLeastOne = True
        i = i + 1
    if (atLeastOne):
        printString = ""
        for ping in goodPingLocations:
            printString = printString + ping + " "
        print(printString)
    else:
        print("HE GOT AWAY!")

main()


def test():
    assert FBIcheck("FERQSDFBI-1") == True
    assert FBIcheck("") == False
    assert FBIcheck("FBI0") == True
    print("Passed all tests!")

test()