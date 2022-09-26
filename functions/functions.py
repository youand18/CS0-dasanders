#David Sanders Functions Assignment 
import math
import random

def addSum(a,b):
    return a + b

def multiSum(a,b):
    return a*b

def divSum(a,b):
    return a/b

def subSum(a,b):
    return a-b

def remainder(a,b):
    return a%b

def power(a,b):
    return math.pow(a,b)

def squareRoot(a):
    return math.pow(a,-2)


num1 = input("Input first number: ")
num2 = input("Input second number: ")
num1 = float(num1)
num2 = float(num2)

print("addSum of " + str(num1) +" and " + str(num2) + " = " + str(addSum(num1,num2)))
print("multiSum of " + str(num1) +" and " + str(num2) + " = " + str(multiSum(num1,num2)))
print("divSum of " + str(num1) +" and " + str(num2) + " = " + str(divSum(num1,num2)))
print("subSum of " + str(num1) +" and " + str(num2) + " = " + str(subSum(num1,num2)))
print("Remainder of " + str(num1) +" and " + str(num2) + " = " + str(remainder(num1,num2)))
print(str(num1) + " to the power of " + str(num2) + " = " + str(power(num1,num2)))
print("Square Root of " + str(num1) + " = " + str(squareRoot(num1)))


def test():
    num1 = random.randrange(0,100)
    num2 = random.randrange(0,100)
    print("addSum of " + str(num1) +" and " + str(num2) + " = " + str(addSum(num1,num2)))
    print("multiSum of " + str(num1) +" and " + str(num2) + " = " + str(multiSum(num1,num2)))
    print("divSum of " + str(num1) +" and " + str(num2) + " = " + str(divSum(num1,num2)))
    print("subSum of " + str(num1) +" and " + str(num2) + " = " + str(subSum(num1,num2)))
    print("Remainder of " + str(num1) +" and " + str(num2) + " = " + str(remainder(num1,num2)))
    print(str(num1) + " to the power of " + str(num2) + " = " + str(power(num1,num2)))
    print("Square Root of " + str(num1) + " = " + str(squareRoot(num1)))
    num1 = random.randrange(0,100)
    num2 = random.randrange(0,100)
    print("addSum of " + str(num1) +" and " + str(num2) + " = " + str(addSum(num1,num2)))
    print("multiSum of " + str(num1) +" and " + str(num2) + " = " + str(multiSum(num1,num2)))
    print("divSum of " + str(num1) +" and " + str(num2) + " = " + str(divSum(num1,num2)))
    print("subSum of " + str(num1) +" and " + str(num2) + " = " + str(subSum(num1,num2)))
    print("Remainder of " + str(num1) +" and " + str(num2) + " = " + str(remainder(num1,num2)))
    print(str(num1) + " to the power of " + str(num2) + " = " + str(power(num1,num2)))
    print("Square Root of " + str(num1) + " = " + str(squareRoot(num1)))
    num2 = random.randrange(0,100)
    print("addSum of " + str(num1) +" and " + str(num2) + " = " + str(addSum(num1,num2)))
    print("multiSum of " + str(num1) +" and " + str(num2) + " = " + str(multiSum(num1,num2)))
    print("divSum of " + str(num1) +" and " + str(num2) + " = " + str(divSum(num1,num2)))
    print("subSum of " + str(num1) +" and " + str(num2) + " = " + str(subSum(num1,num2)))
    print("Remainder of " + str(num1) +" and " + str(num2) + " = " + str(remainder(num1,num2)))
    print(str(num1) + " to the power of " + str(num2) + " = " + str(power(num1,num2)))
    print("Square Root of " + str(num1) + " = " + str(squareRoot(num1)))

test()