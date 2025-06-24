import random

def play_round():
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice.")
        return

    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        play_round()
        if input("Play again? (y/n): ").lower() == ("y" or "yes"):
            continue
    print("Thanks for playing!")
play_game()