import time
from os import system, name
import random

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


#The hangman states from the first assignment
def hangmanStates(stateInt):
    if(stateInt == 0):
        print("""
|__________ 						
|/      | 
| 	    
|       
| 	
|
| 				              
------------- 	   
        """)
    elif(stateInt == 1):
        print("""
|__________ 						
|/      | 
|       O
|      
| 	
|
| 				              
------------- 	   
        """)
    elif(stateInt == 2):
        print("""
|__________ 						
|/      | 
|       O
|       |
| 	
|
| 				              
------------- 	   	   
        """)
    elif(stateInt == 3):
        print("""
|__________ 						
|/      | 
|       O
|      /|
| 	
|
| 				              
-------------   
        """)
    elif(stateInt == 4):
        print("""
|__________ 						
|/      | 
|       O
|      /|\\
| 
|
| 				              
-------------    
        """)
    elif(stateInt == 5):
        print("""
|__________ 						
|/      | 
|       O
|      /|\\
|      / 
|
| 				              
------------- 		   
        """)
    elif(stateInt == 6):
        print("""
|__________ 						
|/      | 
|       O
|      /|\\
|      / \\
|
| 				              
------------- 	    
        """)


#this function handles the output of the guess line
#for example: T_S_ could be a potential guessline for the word test
def hangmanGuessLine(correctStringChecks, correctString):
    printString = ""
    i = 0
    for boole in correctStringChecks:
        if(boole == True):
            printString = printString + correctString[i]
        else:
            printString = printString + "_"
        i = i + 1
    print(printString)

#checking to see if all the boolean states are true, meaning the player has correctly guessed all the letters
def checkWin(correctString, correctStringChecks):
    for boole in correctStringChecks:
        if (boole == False):
            return False
    return True


#driver function
def hangman(stateInt, correctString, correctStringChecks):
    clear()
    going = True
    lettersGuessed = []

    while (going):
        hangmanStates(stateInt)
        hangmanGuessLine(correctStringChecks, correctString)
        letterGuess = input("Enter Guess: ")
        #the isalpha check makes sure you don't accidentally send in an invalid attempt.
        if(letterGuess.isalpha()):
            lettersGuessed.append(letterGuess)
            guessString = "Guesses: "
            for letter in lettersGuessed:
                guessString = guessString + (letter + ",")
            print(guessString)
            changed = False
            i = 0
            #checking if guess was correct
            for char in correctString:
                if (letterGuess == char):
                    correctStringChecks[i] = True
                    changed = True
                i = i + 1
            #these if statements check the game state, and will either cycle to the next hangman state or tell the player they won/lost
            if (changed == False):
                stateInt = stateInt + 1
                if (stateInt >= 6):
                    hangmanStates(6)
                    print("You Lose! The correct word was %s"%(correctString) + ".")
                    time.sleep(3)
                    going = False
                    endingcheck = input("Would you like to continue? (Y/N): ")
                    if (endingcheck == "N" or endingcheck == "n"):
                        return()
                    main()
            elif (checkWin(correctString, correctStringChecks)):
                hangmanGuessLine(correctStringChecks, correctString)
                print("Congratulations, you won!")
                time.sleep(3)
                going = False
                endingcheck = input("Would you like to continue? (Y/N): ")
                if (endingcheck == "N" or endingcheck == "n"):
                    return()
                main()

def main():
    #Hangman wordlist from https://github.com/Xethron/Hangman/blob/master/words.txt
    file = open('hangmanwords.txt')
    #reads in the words to the content array
    content = file.readlines()
    #then picks a random word
    correctString = content[random.randrange(0,853)]
    #this is all just setting the base values for the start of a hangman game.
    correctStringChecks = []
    state = 0
    for char in correctString:
        if (char.isalpha()):
            correctStringChecks.append(False)   
    hangman(state, correctString, correctStringChecks) 

main()