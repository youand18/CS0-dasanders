#David Sanders Area and Perimeter of a Triangle code

#Algorithm Steps:
#1. 

def isIntStr(string):
    for char in string:
        if (not(char == "1" or char == "2" or char == "3" or char == "4" or char == "5" or char == "6" or char == "7" or char == "8" or char == "9" or char == "0")):
            return False
    return True




def prompt():
    answer = input("Enter three sides of a triangle, separated by spaces(3 4 5): ")
    (x,y,z) = (0,0,0)
    a = []
    a = answer.split()
    if (len(a) < 3):
        prompt()
        return
    if (isIntStr(a[0]) and isIntStr(a[1]) and isIntStr(a[2])):
        x = int(a[0])
        y = int(a[1])
        z = int(a[2])
    else:
        prompt()
    return


prompt()