# David Sanders Conditionals Program Python 110
import random


def sum5(num1,num2,num3,num4,num5):
    return(num1+num2+num3+num4+num5)


def product5(num1,num2,num3,num4,num5):
    return(num1*num2*num3*num4*num5)

def average5(num1,num2,num3,num4,num5):
    total = sum5(num1,num2,num3,num4,num5)
    return(total/5)

def largest(num1,num2,num3,num4,num5):
    if (num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5):
        return(num1)
    elif (num2 > num3 and num2 > num4 and num2 > num5):
        return(num2)
    elif (num3 > num4 and num3 > num5):
        return(num3)
    elif (num4 > num5):
        return(num4)
    else:
        return(num5)

def smallest(num1,num2,num3,num4,num5):
    if (num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5):
        return(num1)
    elif (num2 < num3 and num2 < num4 and num2 < num5):
        return(num2)
    elif (num3 < num4 and num3 < num5):
        return(num3)
    elif (num4 < num5):
        return(num4)
    else:
        return(num5)
def test():
    num1 = 1
    num2 = 2
    num3 = 3
    num4 = 4
    num5 = 5
    print(sum5(num1,num2,num3,num4,num5))
    print(product5(num1,num2,num3,num4,num5))
    print(average5(num1,num2,num3,num4,num5))
    print(largest(num1,num2,num3,num4,num5))
    print(smallest(num1,num2,num3,num4,num5))
    assert sum5(num1,num2,num3,num4,num5) == 15
    assert product5(num1,num2,num3,num4,num5) == 120
    assert average5(num1,num2,num3,num4,num5) == 3
    assert largest(num1,num2,num3,num4,num5) == 5
    assert smallest(num1,num2,num3,num4,num5) == 1
    num1 = 1.5
    num2 = 2.5
    num3 = 5.5
    num4 = 10.2
    num5 = 5.5
    print(sum5(num1,num2,num3,num4,num5))
    print(product5(num1,num2,num3,num4,num5))
    print(average5(num1,num2,num3,num4,num5))
    print(largest(num1,num2,num3,num4,num5))
    print(smallest(num1,num2,num3,num4,num5))
    assert sum5(num1,num2,num3,num4,num5) == 25.2
    assert product5(num1,num2,num3,num4,num5) < 1158 and product5(num1,num2,num3,num4,num5) > 1157
    assert average5(num1,num2,num3,num4,num5) == 5.04
    assert largest(num1,num2,num3,num4,num5) == 10.2
    assert smallest(num1,num2,num3,num4,num5) == 1.5   



def main():
    looping = True
    while (looping):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        num4 = float(input("Enter fourth number: "))
        num5 = float(input("Enter fifth number: "))
        print("sum of 5: " + str(sum5(num1,num2,num3,num4,num5)))

        print("product of 5: " + str(product5(num1,num2,num3,num4,num5)))
        print("average of 5: " + str(average5(num1,num2,num3,num4,num5)))
        print("largest: " + str(largest(num1,num2,num3,num4,num5)))
        print("smallest: " + str(smallest(num1,num2,num3,num4,num5)))
        check = input("Do you want to continue? Y/N: ")
        if (check == "N" or check == "n"):
            looping = False
    #test()

main()