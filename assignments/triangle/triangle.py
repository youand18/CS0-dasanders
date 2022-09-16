#David Sanders Area and Perimeter of a Triangle code
import math
#Algorithm Steps:
#1. 

def isIntStr(string):
    for char in string:
        if (not(char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9" or char == "0")):
            return False
    return True


def herons(a,b,c):
    #Herons Formula: A = SQRT(s(s-a)(s-b)(s-c)) where s = (a+b+c)/2
    (area, s) = (0, 0)
    s = (a+b+c)/2
    if ((s*(s-a)*(s-b)*(s-c)) > 0):
        area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
    else:
        area = 0
    return (area, s)

def realTriangle(a,b,c):
    return ((a+b>c) and (b+c>a) and (c+a>b))

def prompt():
    answer = input("Enter three sides of a triangle, separated by spaces(3 4 5): ")
    (a,b,c) = (0,0,0)
    l = []
    l = answer.split()
    if (len(l) < 3):
        prompt()
        return
    if (isIntStr(l[0]) and isIntStr(l[1]) and isIntStr(l[2])):
        a = int(l[0])
        b = int(l[1])
        c = int(l[2])
    else:
        prompt()
    
    (area, s) = (herons(a,b,c))
    print("Area: " + str(area))
    print("Perimeter: " + str(2*s))
    if (realTriangle(a,b,c)):
        print(str(a) + ", " + str(b) + ", and " + str(c) + " are valid sides of a triangle!")
    else:
        print(str(a) + ", " + str(b) + ", and " + str(c) + " are not valid sides of a triangle...")
    


prompt()