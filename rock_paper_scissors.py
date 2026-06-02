import random

# Initialize the scoreboard tracking variables
user_score = 0
computer_score = 0

print("=== WELCOME TO ROCK-PAPER-SCISSORS GAME ===")

while True:
    # Display the current scores at the start of each round
    print(f"\nScoreboard -> You: {user_score} | Computer: {computer_score}")
    
    # Prompt the user for input and convert it to lowercase
    user_choice = input("Choose rock, paper, or scissors (or type 'exit' to quit): ").lower()
    
    # Check if the user wants to terminate the application loop
    if user_choice == 'exit':
        print("\nThank you for playing! Final Game Scores:")
        print(f"Your Score: {user_score} | Computer Score: {computer_score}")
        break
        
    # Validate user inputs against accepted choice rules
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid entry! Please type exactly rock, paper, or scissors.")
        continue
        
    # Let the computer make its random choice from the list options
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")
    
    # Evaluate game rules to determine the round winner
    if user_choice == computer_choice:
        print("It's a tie match!")
        
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("Congratulations! You win this round.")
        user_score += 1
        
    else:
        print("Computer wins this round!")
        computer_score += 1
