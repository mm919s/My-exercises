import random
first_name, last_name = input("Please enter your full name(first name and last name) = ").split(" ")
print("Hello " + first_name + "!")
print("_" * 99)
print("Explanations :")
print("1) This is a rock,paper,scissors game.")
print("2) It'll be played in 3 rounds.")
print("3) The final winner among you and the computer will be announced at the end of the game.")
print("_" * 99)
print("Let's begin!")
# Gets the user's name and explains the game to the user.
computer_score = 0
user_score = 0
for i in range(1, 4):
    if i == 1:
        round_num = "first round"
    elif i == 2:
        round_num = "second round"
    else:
        round_num = "third round"
    user_item = input("Please choose an item(object) among 'rock','paper' and 'scissors' for the " + round_num + " = ")
    computer_item = random.randrange(1, 4)
    if computer_item == 1:
        computer_item = "rock"
    elif computer_item == 2:
        computer_item = "paper"
    else:
        computer_item = "scissors"
    print("Computer's chosen item is = " + computer_item)
    if user_item == computer_item:
        print("Both of you and the computer has chose the same item(object);")
        print("Then the result of the " + round_num + " is equal!")
    else:
        if user_item == "rock":
            if computer_item == "paper":
                print("The winner of the " + round_num + " is the computer!")
                computer_score += 1
            else:
                print("The winner of the " + round_num + " is you!")
                user_score += 1
        elif user_item == "paper":
            if computer_item == "rock":
                print("The winner of the " + round_num + " is you!")
                user_score += 1
            else:
                print("The winner of the " + round_num + " is the computer!")
                computer_score += 1
        else:
            if computer_item == "rock":
                print("The winner of the " + round_num + " is the computer!")
                computer_score += 1
            else:
                print("The winner of the " + round_num + " is you!")
                user_score += 1
    print("_" * 99)
# It's a loop for the 3 rounds that takes users choice;then prints the computers choice and the result of the round.
if user_score == computer_score:
    print("The final winner is no one!")
    print("Because the results of 3 rounds were equal!")
else:
    if user_score > computer_score:
        print("You are the final winner!")
    else:
        print("The computer is the final winner!")
# It checks the total result and prints it.
