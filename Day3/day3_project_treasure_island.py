print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Ask the player where they want to go.
direction = input("Where do you want to go? Left or Right?: ").lower()

if direction == "right":
    print("You fell into a hole. GAME OVER!!!")
elif direction == "left":
    action = input("Swim or Wait?: ").lower()
    if action == "swim":
        print("You were attacked by a trout. GAME OVER!!!")
    elif action == "wait":
        door = input("Which door? Red, Blue, Green, and Yellow: ").lower()
        if door == "red":
            print("You were burned by fire. GAME OVER!!!")
        elif door == "blue":
            print("You were eaten by beasts. GAME OVER!!!")
        elif door == "green":
            print("You got bitten by a snake. GAME OVER!!!")
        elif door == "yellow":
            river = input("You got lucky, but there's a stream. Boat or Canoe?: ").lower()
            if river == "canoe":
                print("You fell into the river. GAME OVER!!!")
            elif river == "boat":
                other_side = input("You crossed safely. Can you see the treasure island ahead? Yes or No?: ").lower()
                if other_side == "no":
                    print("You cannot see far. GAME OVER!!!")
                elif other_side == "yes":
                    print("You finally made it because you can see far. YOU WON!!!!!")
                else:
                    print("Invalid choice. GAME OVER!!!")
            else:
                print("Invalid river choice. GAME OVER!!!")
        else:
            print("Invalid door. GAME OVER!!!")
    else:
        print("Invalid action. GAME OVER!!!")
else:
    print("INVALID DIRECTION!")
