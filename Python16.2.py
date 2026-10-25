import random

while True:
    user_action = input("Enter a choice (rock, paper, or scissors): ")
    possible_actions = ["rock", "paper", "scissors"]

    computer_cation = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_cation}.\n")

    if user_action == computer_cation:
        print(f"Both players selected {user_action}. It a tie!")
    elif user_action == "rock":
        if computer_cation == "scissors":
            print("Rock smashes scissors! you win!")
        else:
            print("Paper covers rock! You lose!")
    elif user_action == "paper":
        if computer_cation == "rock":
            print("Paper covers rock! You lose!")
        else:
            print("Scissors cuts paper! You lose!")
    elif user_action == "scissors":
        if computer_cation == "paper":
            print("Scissors cuts paper! You Win!")
        else:
            print("Rock smashes scissors! you lose!")

    play_again = input("Play again? (y/n): ")
    if play_again != "y":
        break
