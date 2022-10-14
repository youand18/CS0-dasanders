import random

#David Sanders Beginning Python Guess the Number Game

name = input("Hello! What is your name? ")
playing = True
while(playing):
    rightNumber = random.randrange(1,20)


    guessNumber = 0
    totalGuesses = 0
    while (guessNumber != rightNumber or (totalGuesses >= 6)):
        print("You have guessed " + str(totalGuesses) + " time(s).")
        guessNumber = int(input("Guess a number between 1 and 20: "))
        if (guessNumber != rightNumber and guessNumber > rightNumber):
            print("Your Guess Was Too High!")
        elif(guessNumber < rightNumber):
            print("Your Guess Was Too Low!")
        totalGuesses = totalGuesses + 1

    if (guessNumber == rightNumber):
        print("You Win! The right number was " + str(rightNumber))
    else:
        print("You Lose! The right number was " + str(rightNumber))
    check = input("Do you want to keep playing? (Y/N): ")
    if (check == "Y" or check == "y"):
        playing = True
    else:
        playing = False