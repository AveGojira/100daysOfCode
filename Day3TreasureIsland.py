print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

crossroad = input("You're at a crossroad. Where do you want to go?\n"
                  "Do you go [left] or [right]? ")
lower_crossroad = crossroad.lower()
if lower_crossroad == "left":
    lake = input("You come to a lake. There is an island in the middle of the lake.\n"
                 "Do you [wait] for a boat, or [swim] across? ")
    lower_lake = lake.lower()
    if lower_lake == "wait":
        doors = input("You arrive at the island unharmed. There is a house with three doors.\n"
                      "One [red], one [yellow], and one [blue]. Which door do you choose? ")
        lower_doors = doors.lower()
        if lower_doors == "yellow":
            print("You open the yellow door and find the treasure brilliantly shining in the middle of the room.\n"
                  "Congratulations! You win!")
        elif lower_doors == "red":
            print("You open the red door, only for the house to burst into flames!\n"
                  "Game Over.")
        elif lower_doors == "blue":
            print("You open the blue door, only to be attacked by beasts!\n"
                  "Game Over.")
    elif lower_lake == "swim":
        print("You attempt to swim across the lake. Unfortunately unable to tame the waters, you drown.\n"
              "Game Over.")
elif lower_crossroad == "right":
    print("You've fallen into a hidden sink hole!\n"
          "Game Over.")