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