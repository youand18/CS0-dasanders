#David Sanders Area and Perimeter of a Triangle code
import math
import random
#Algorithm Steps:
#1. Get input of three side values
#2. Check input values
#3. calculate the half-perimeter/s and Area values using herons formula, being cautious not to put a negative radicand into the sqrt function
#4. Finally, check the validity of the triangle through two ways:
#   I. if the radicand was negative, that means the area of the triangle was negative, which means the triangle doesn't work
#USED II. use the triangle inequality theorem to check if any two sides added up are smaller than the third side; the triangle doesn't work if that's the case

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
    if (answer == "TEST"):
        (a,b,c) = (random.randrange(1,100),random.randrange(1,100),random.randrange(1,100))
    else:
        (a,b,c) = (0,0,0)
        l = []
        l = answer.split()
        if (len(l) < 3):
            prompt()
            return()
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
    return()
    
prompt()