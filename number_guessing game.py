import random
while True:
    print("Welcome to the Number Guessing Game!")
    print("Select an option from below:")
    print("1. Start a new game")
    print("2. Exit")

    choice = input("Enter your choice (1-2): ")
    
    if choice == "1":
        number_to_guess = random.randint(1, 100)
        attempts = 0
        
        while True:
            guess = input("Guess a number between 1 and 100: ")
            attempts += 1
            
            try:
                guess = int(guess)
                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                    continue
                
                elif guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    elif choice == "2":
        print("Exiting the game. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select option 1 or 2.")