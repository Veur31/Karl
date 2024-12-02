
import random
def play():
    print("Welcome to the game!!")
    user = input("'r' for rock, 's' for scissor, and 'p' for paper: ")
    computer = random.choice(["r", "s", "p"])
    if user == computer:
        return "it\s a tie"
    if win(user, computer):
        return "You win"
    else:
        return "You lost"
#r>s, s>p p>r
def win(winner, opponent):
    return (winner == "r" and opponent == "s") or\
    (winner == "s" and opponent =="p") or\
    (winner == "p" and opponent == "r")
while True:
    print(play())
    again = input("Do you want to play again? Y/N: ").upper()
    if again != "Y":
        break
    
