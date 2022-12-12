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

def checkWin(correctString, correctStringChecks):
    for boole in correctStringChecks:
        if (boole == False):
            return False
    return True

def hangman(stateInt, correctString, correctStringChecks):
    clear()
    going = True
    lettersGuessed = []

    while (going):
        hangmanStates(stateInt)
        hangmanGuessLine(correctStringChecks, correctString)
        letterGuess = input("Enter Guess: ")
        if(letterGuess.isalpha()):
            lettersGuessed.append(letterGuess)
            guessString = "Guesses: "
            for letter in lettersGuessed:
                guessString = guessString + (letter + ",")
            print(guessString)
            changed = False
            i = 0
            for char in correctString:
                if (letterGuess == char):
                    correctStringChecks[i] = True
                    changed = True
                i = i + 1
            if (changed == False):
                stateInt = stateInt + 1
                if (stateInt >= 6):
                    hangmanStates(6)
                    print("You Lose! The correct word was %s"%(correctString) + ".")
                    time.sleep(3)
                    going = False
                    main()
            elif (checkWin(correctString, correctStringChecks)):
                hangmanGuessLine(correctStringChecks, correctString)
                print("Congratulations, you won!")
                time.sleep()
                going = False
                main()

def main():
    lineCount = 0
    #Hangman wordlist from https://github.com/Xethron/Hangman/blob/master/words.txt
    file = open('hangmanwords.txt')
    content = file.readlines()
    correctString = content[random.randrange(0,853)]
    correctStringChecks = []
    state = 0
    for char in correctString:
        if (char.isalpha()):
            correctStringChecks.append(False)   
    hangman(state, correctString, correctStringChecks) 

main()