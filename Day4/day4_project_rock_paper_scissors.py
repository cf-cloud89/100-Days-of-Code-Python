import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

# Player inputs choice
player_choice = (int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")))
if player_choice >= 0 and player_choice <= 2:
    print(options[player_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(options[computer_choice])

# Use if statements to decide the winner
if player_choice >= 3 or player_choice <0:
    print("That's an invalid number. You lose!")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and player_choice == 2:
    print("You lose!")
elif computer_choice > player_choice:
    print("You lose!")
elif player_choice > computer_choice:
    print("You win!")
elif computer_choice == player_choice:
    print("It's a draw!")
