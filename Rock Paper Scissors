import random

while True:
    user_action = input("Enter Choice (rock, paper, scissor):")
    possible_action = ["rock", "paper", "scissor"]
    computer_action = random.choice(possible_action)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "paper":
            print("Rock smashes scissors!\U0001f600")
        else:
            print("Paper covers rock ! Computer wins!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper covers rock! \U0001f606")
        else:
            print("Scissors cuts paper! Computer Win!")
    elif user_action == "scissor":
        if computer_action == "paper":
            print("scissor cuts paper! \U0001F641")
        else:
            print("Rock smashes scissor!Computer win!")

    play_again = input("play again? (y/n):")
    if play_again != 'y':
        break
