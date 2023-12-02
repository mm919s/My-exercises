import random
# Imports 'random' library.
print("Please enter your choice")
print("among the three items of")
print("'rock','paper' and 'scissors'")
item1 = input("to continue the game = ")
print("_" * 44)
# Puts user's input in a variable called 'item1'.
item2 = random.randrange(0, 3)
if item2 == 0:
    item2 = "rock"
elif item2 == 1:
    item2 = "paper"
else:
    item2 = "scissors"
# Chooses randomly among 3 items(objects) of this game via 'random' library.
while item1 == item2:
    print("Both of you and the computer")
    print("has chose the same item.please")
    print("try another item until one of")
    item1 = input("you wins = ")
    print("_" * 44)
    item2 = random.randrange(0, 3)
    if item2 == 0:
        item2 = "rock"
    elif item2 == 1:
        item2 = "paper"
    else:
        item2 = "scissors"
    if item1 != item2:
        break
# If user and the computer both chose the same item, it will receive another input until one of them wins.
if item1 == "rock":
    if item2 == "paper":
        print("The computer chose ", item2, ".")
        print("The computer won!")
    else:
        print("The computer chose ", item2, ".")
        print("You won!")
elif item1 == "paper":
    if item2 == "rock":
        print("The computer chose ", item2, ".")
        print("You won!")
    else:
        print("The computer chose ", item2, ".")
        print("The computer won!")
else:
    if item2 == "rock":
        print("The computer chose ", item2, ".")
        print("The computer won!")
    else:
        print("The computer chose ", item2, ".")
        print("You won!")
# It defines conditions to get the final result of this game.
