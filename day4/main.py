# Day 4: Rock Paper and Scissors
import os
from random import randint


list_choices = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """,
    """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    """,
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """,
]

while True:
    print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    try:
        user_choice = int(input())
        print(list_choices[user_choice])
        computer_choice = randint(0, len(list_choices) - 1)
        print("Computer choose:")
        print(list_choices[computer_choice])

        if user_choice == computer_choice:
            print("It's a draw 😕")
        elif user_choice == 0 and computer_choice == 1:
            print("You lose 😞")
        elif user_choice == 1 and computer_choice == 2:
            print("You lose 😞")
        elif user_choice == 2 and computer_choice == 0:
            print("You lose 😞")
        else:
            print("You win 😃")
    except:
        print("incorrect choice")
    input('Press "Enter" to play again...')
    os.system("clear")
