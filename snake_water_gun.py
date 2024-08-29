import random


computer = random.choice([-1, 0, 1])  # -1: Rock, 0: Paper, 1: Scissors


youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")


youDict = {"s": 1, "w": -1, "g": 0}


if youstr not in youDict:
    print("Invalid choice! Please enter 's', 'w', or 'g'.")
else:
    you = youDict[youstr]

    
    if computer == you:
        print("It's a Draw!")
    else:
        if (computer == -1 and you == 1) or (computer == 0 and you == -1) or (computer == 1 and you == 0):
            print("You Lose!")
        else:
            print("You Win!")
