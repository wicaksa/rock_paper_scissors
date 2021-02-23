# This program is a Rock, Paper, Scissors game between the computer and user. 
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

# Ask user input and generate computer input randomly.
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))
comp_choice = random.randint(0,2) 

# User choice
if user_choice == 0:
    user = rock 
elif user_choice == 1:
    user = paper 
else : 
    user = scissors 

# Computer Choice
if comp_choice == 0 : 
    comp = rock
elif comp_choice == 1:
    comp = paper
else:
    comp = scissors 

# Print out the choices by the user and computer.
print(f"You picked {user}." )
print(f"Computer picked {comp}." )

# Make cases. 
# Rock beats Scissors but loses to paper.
if user_choice == 0: # Rock
    if comp_choice == 0: # Rock
        print("You tie! The computer also chose Rock!")
    elif comp_choice == 1: # Paper
        print("You lose! Paper beats Rock!") 
    else: # Scissors
        print("You win! Rock beats Scissors!")
# Paper beats Rock but loses to scissors.
if user_choice == 1: # Paper
    if comp_choice == 0: # Rock
        print("You win! Paper beats Rock!")
    elif comp_choice == 1: # Paper
        print("You tie! The computer also chose Paper!") 
    else: # Scissors
        print("You lose! Scissors beat Paper!")
# Scissors beat Paper but loses to rock. 
if user_choice == 2: # Scissors
    if comp_choice == 0: # Rock
        print("You lose! Rock beats Scissors!")
    elif comp_choice == 1: # Paper
        print("You win! Scissors beat paper!") 
    else: # Scissors
        print("You tie! The computer also chose scissors!")
