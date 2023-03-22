# This is Day 4 of 100 for the Udemy Python Bootcamp
import random

rock = '''
R O C K
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
P A P E R
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
S C I S S O R S
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
print("\nR O C K\nP A P E R\nS C I S S O R S")

options = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n" ))
computer_choice = random.randint(0, 2)

if player_choice >= 3 or player_choice < 0:
    print("That isn't a valid move")
else:
    if player_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice == 0 and player_choice == 2:
        print("You lose")
    elif computer_choice == player_choice:
        print("It's a draw")
    elif player_choice > computer_choice:
        print("You win")
    elif computer_choice > player_choice:
        print("You lose")




