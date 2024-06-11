import random

def get_player_choice():
    """Gets the player's choice (rock, paper, or scissors)."""
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    """Generates a random choice for the computer."""
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def determine_winner(player_choice, computer_choice):
    """Determines the winner based on the choices."""
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        return "It's a tie!"

    winning_combinations = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    if winning_combinations[player_choice] == computer_choice:
        return "You win!"
    else:
        return "Computer wins!"

def main():
    player_score = 0
    computer_score = 0

    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if "win" in result:
            player_score += 1
        elif "Computer wins" in result:
            computer_score += 1

        print(f"\nScore: You: {player_score}, Computer: {computer_score}")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    main()
