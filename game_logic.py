import random
game_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(game_options)
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
print(computer_choice)
print(user_choice)
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("Computer wins!")