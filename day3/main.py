def main():
    print(
        """
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `\"=._o.\" ,-\"\"\"-._ \".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
"""
    )
    print("Welcome to Treasure Island.")
    print("Your mission is to find the hidden treasure.")
    print("You're at a crossroad. Where do you want to go?")
    print('Type "left" or "right"')

    choice1 = input()
    if choice1.casefold() == "left":
        print(
            "You've come to a serene lake. There is a mysterious island in the middle of the lake."
        )
        print('Type "wait" to wait for a boat. Type "swim" to swim across')
        choice2 = input()
        if choice2.casefold() == "wait":
            print("A boat arrives and takes you to the island.")
            print(
                "You arrive at the island unharmed. There is a house with three doors: one red, one blue, and one yellow."
            )
            print('Which door do you choose? Type "red", "blue", or "yellow"')
            choice3 = input()
            if choice3.casefold() == "yellow":
                print(
                    "You open the yellow door to find a room filled with gold and jewels. You Win!"
                )
            elif choice3.casefold() == "red":
                print(
                    "You open the red door and are greeted by a fierce dragon. Game Over."
                )
            elif choice3.casefold() == "blue":
                print(
                    "You open the blue door and find yourself in a room filled with water. You drown. Game Over."
                )
            else:
                print("You chose a door that doesn't exist. Game Over.")
        else:
            print(
                "You try to swim across but are attacked by a swarm of piranhas. Game Over."
            )
    else:
        print("You take a step to the right and fall into a hidden pit. Game Over.")


if __name__ == "__main__":
    main()
