"""Creating a treasure hunt using using conditionals is the goal for day 3"""

print(""" _                                     
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ \\
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___|\n""")

print("Welcome to Treasure Island \nYour mission is to find the treasure")

direction = input("You're at a cross road. Where do you want to go? \"left\" or \"right\"\n")
while direction not in ["left", "right"]:
    print("Invalid input. Try again\n")
    direction = input("You're at a cross road. Where do you want to go? \"left\" or \"right\"\n")

if direction == 'left':
    lake_decision = input("You come to a lake. There is an island in the middle of the lake."
                          " Type \"wait\" to wait for a boat. Type \"swim\" to swim across\n")
    while lake_decision not in ["swim", "wait"]:
        print("Invalid input. Try again\n")
        lake_decision = input("You come to a lake. There is an island in the middle of the lake."
                              " Type \"wait\" to wait for a boat. Type \"swim\" to swim across\n")

    if lake_decision == "wait":
        door_decision = input("An old man helped you cross the road. There are 3 houses."
                              " One red, one yellow and one blue. Which color do you choose? \"red\", \"yellow\", \"blue\"\n")
        while door_decision not in ["red", "blue", "yellow"]:
            print("Invalid input. Try again\n")
            door_decision = input("An old man helped you cross the road. There are 3 houses."
                                  " One red, one yellow and one blue. Which color do you choose? \"red\", \"yellow\", \"blue\"\n")

        if door_decision == "blue":
            print("Congratulation! You found the way to prevent hair loss and became a billionaire.")

        else:
            print("You chose the whole house and were killed for trespassing. Try again.")
    else:
        print("You jumped in the lake all confident but forgot you didn't know how to swim and drowned. Try again.")
else:
    print("You chose right thinking right is always right but you were wrong. Suddenly a wizard "
          "jumped you and asked for money but you were broke which angered the wizard to "
          "use fire spell to finish your life. Try again.")

