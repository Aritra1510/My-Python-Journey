
import random

# ASCII Art
rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''     _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of choices
list_of_choices = [rock, paper, scissors]

# Get user input
choice_of_user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if choice_of_user < 0 or choice_of_user > 2:
    print("Invalid choice. You lose by default!")
else:
    choice_of_computer = random.randint(0, 2)

    print("\nYou chose:")
    print(list_of_choices[choice_of_user])

    print("Computer chose:")
    print(list_of_choices[choice_of_computer])

    # Game logic
    if choice_of_user == choice_of_computer:
        print("It's a draw!")
    elif (choice_of_user == 0 and choice_of_computer == 2) or \
         (choice_of_user == 1 and choice_of_computer == 0) or \
         (choice_of_user == 2 and choice_of_computer == 1):
        print("You win!")
    else:
        print("You lose!")
