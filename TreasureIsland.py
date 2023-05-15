print(input("(Press Enter to Continue.)"), end='')
print("Welcome to Treasure Island. ", end='')
print("Your mission is to find the treasure. ")
print("You're at a cross road. Where do you want to go?")
LR = (input('Type "Left" or "Right." ').lower())
if LR == "right":
    print("Game Over")
    exit()
if LR == "left":
    print("You come to a lake. There is an island in the middle of the lake. What do you do? ", end='')
else:
    print("Game Over")
    exit()
WS = (input('Type "wait" to wait for a boat. Type "swim" tp swim across. ').lower())
if WS == "wait":
    print("You arrive at the island unharmed. There is a house with 3 doors. 1 red, 1 yellow, and 1 blue. ", end='')
elif WS == "swim":
    print("Game Over")
    exit()
else:
    print("Game Over")
    exit()
RYB = (input('\nWhich colour do you choose? Type "Red", "Yellow", or "Blue". ').lower())
if RYB == "red":
    print("Game Over")
    exit()
elif RYB == "yellow":
    print("You Win!")
elif RYB == "blue":
    print("Game Over")
    exit()
else:
    print("Game Over")
    exit()
