print("Welcome to Treasure Island. Your mission is to find the treasure")

direction = input("Do you want to go left or right")

if direction == "left":
    swim = input("Do you want to swim or take a boat")
    if swim == "swim":
        print("Attacked by trout. Game Over")
    elif swim != "boat":
        print("You are dead meat!!!!!!")
    else:
        selection = input("Which door do you want to take? Red, Blue, Yellow")
        if selection == 'red':
            print("Burned by fire. Game over.")
        elif selection == 'blue':
            print("Eaten by a beast")
        elif  selection == "yellow":
            print("You Win!")
        else:
            print("Game Over!")
else:
    print("Sorry!You have fallend into a hole. Game over.")
