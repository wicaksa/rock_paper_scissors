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

try_again = True

while try_again == True: 
    # Ask user input and generate computer input randomly.
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))
    while user_choice < 0 or user_choice > 2:
        user_choice = int(input("Incorrect number. Please try again."))

    # Computer choice. 
    comp_choice = random.randint(0,2) 

    # Store images in a list.
    game_images = [rock, paper, scissors]

    # Print out the choices by the user and computer.
    print(f"You picked {game_images[user_choice]}." )
    print(f"Computer picked {game_images[comp_choice]}." )

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

    # Prompt user to try again. 
    user_repeat = int(input("Do you want to play again? (1 = YES/ 0 = NO."))
    while user_repeat > 1 or user_repeat < 0:
        user_repeat = int(input("Incorrect response. Please try again: "))
    if user_repeat == 0:
        try_again = False

# Print Goodbye message when the user doesn't wanna replay.
print("Goodbye! Play again later!")



# End
