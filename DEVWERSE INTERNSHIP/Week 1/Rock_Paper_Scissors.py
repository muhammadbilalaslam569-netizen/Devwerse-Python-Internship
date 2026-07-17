import random

choices = ["Rock","Paper","Scissors"]

while True:
    user = input("Enter Rock,Paper or Scissors or type end to quit:")

    if user.lower()=="end":
        print("Thank you for playing")
        break

    user = user.capitalize()

    if user not in choices:
        print("Invalid choice")
        continue

    computer = random.choice(choices)

    print("Computer Chose:", computer)

    if user == computer:
        print("Its a Draw")

    elif user == "Rock":
        if computer == "Scissors":
            print("You Win! Rock beats Scissors")
        else:
            print("You win! Paper beats Rock")

    elif user == "Paper":
        if computer == "Rock":
            print("You win! Paper beats Rock")
        else:
            print("Computer wins! Paper beats Rock")

    elif user == "Scissors":
        if computer == "Paper":
            print("You win! Scissors beats Paper")
        else:
            print("Computer wins! Rock beats Scissors")


    print()