import random

def play():
    print("Welcome to the game!")
    print()
    
    choice = ["rock","paper", "scissors"]

    while True:
        print()
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if player_choice not in choice:
            print("Please input from the choices")
            continue
        computer = random.choice(choice)

        if player_choice == computer:
            print("It's a tie")
        elif (player_choice == "rock" and computer == "scissors") or\
             (player_choice == "paper" and computer == "rock") or\
             (player_choice == "scissors" and computer == "paper"):
            print("You win")
        else:
            print("YOU LOSE")
        print()
        again = input("Do you want to play again? (Y/N): ").lower()

        if again != "y":
            print()
            print("Thank you for playing")
            break
play()