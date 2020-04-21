
import random

SysOutPut = ["snake","gun","water"]

system = random.choice(SysOutPut)

print("Welcome TO Snake...Water....Gun.... Game")
print("You Will Enter the snake or water or gun TO Play the game")


Attempts = int(input("Attempts to Play Game:"))

AttemptCount = 1
UserWon = 0
SystemWon = 0
Tie = 0

while AttemptCount <= Attempts:

    print("Attempt Count :",AttemptCount)

    You = input("Enter the name to play Game:")

    
    
    if You == "snake" and system == "gun":
        
        print("System choosen {} & You choosen {}  : System Won,Better Luck Next Time ".format(system,You))
        AttemptCount = AttemptCount + 1
        SystemWon = SystemWon + 1
        
        
    elif You == "gun" and system == "snake":
        
        print("You choosen {} & System choosen {} : You Won, Congratulations".format(You,system))
        AttemptCount = AttemptCount + 1
        UserWon = UserWon + 1
        
    elif You =="water" and system == "gun":
        
        print("You Choosen {} & System choosen {} : You Won, Congratulations".format(You,system))
        AttemptCount = AttemptCount + 1
        UserWon = UserWon + 1
        
    elif You == "gun" and system == "water":
        
        print("System choosen {} & You choosen {} : System Won, Better Luck Next Time".format(system,You))
        AttemptCount = AttemptCount + 1
        SystemWon = SystemWon + 1
        
    elif You == "snake" and system == "water":
        
        print("You Choosen {} & System choosen {} : You Won, COngratulations".format(You,system))
        AttemptCount = AttemptCount + 1
        UserWon = UserWon + 1
        
    elif You == "water" and system == "snake":
        
        print("Syetem choosen {} & You choosen {} : System Won, Better Luck Next Time".format(system,You))
        AttemptCount = AttemptCount + 1
        SystemWon = SystemWon + 1
        
    elif You == "water" and system == "water":
        
        print("You choosen {} & System Choosen {} : Match Tied".format(You,system))
        AttemptCount = AttemptCount + 1
        Tie = Tie + 1
        
    elif You == "gun" and system == "gun":
            
        print("You choosen {} & System Choosen {} : Match Tied".format(You,system))
        AttemptCount = AttemptCount + 1
        Tie = Tie + 1
        
        
    elif You == "snake" and system == "snake":
        
        print("You choosen {} & System Choosen {} : Match Tied".format(You,system))
        AttemptCount = AttemptCount + 1
        Tie = Tie + 1
    else:
        print("Please enter the correct name : Invalid Input")


print("Its Time to Check the Winner")

if UserWon > SystemWon or UserWon > Tie:
    print("Congratulations You Won the Game")
elif SystemWon > UserWon or SystemWon > Tie:
    print("You Lost the Game , Better Luck Next Time")
elif Tie > UserWon or Tie > SystemWon:
    print("Looks Match Tied")
elif UserWon == SystemWon == Tie:
    print("Looks Match Tied")
else:
    print("You Lost The Game,Better Luck Next Time")

print("You Won :",UserWon)
print("System Won :",SystemWon)
print("Match Tied :", Tie)



