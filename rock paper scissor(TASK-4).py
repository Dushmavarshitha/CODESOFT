import random

def determine_winner(user_choice, computer_choice):
    # Rock beats scissors, scissors beat paper, paper beats rock
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("Welcome to Rock-Paper-Scissors Game!")
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0
    
    play_again = True
    while play_again:
        print("\nChoose one: rock, paper, scissors")
        user_choice = input("Enter your choice: ").lower()
        
        while user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            user_choice = input("Enter your choice: ").lower()
        
        computer_choice = random.choice(choices)
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        print(f"\nYour score: {user_score}")
        print(f"Computer's score: {computer_score}")
        
        play_again_input = input("\nDo you want to play again? (yes/no): ").lower()
        play_again = play_again_input == 'yes'
    
    print("\nThanks for playing!")

if __name__ == "__main__":
    main()
