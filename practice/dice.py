#using the random module
import random
#making defining a function 
def roll_dice(number_of_dice, number_of_sides):
#roll is an empty list
    roll = []
#making a for loop statement
    for _ in range(number_of_dice):
#this code will initialze a random number
        rolls = random.randint(1, number_of_sides)
        roll.append(rolls)
    return roll
#this is the main function of the program, it will ask for user input for both number of dice and sides
def main():
    print("WELCOME WALA KANG CHOICE MAGLALARO KA!")
    user_input = input("Please select your choice (YES OR YES) \n Answer: ").lower()

    if user_input == "y":
        number_of_dice = int(input("How many dice you want to roll? "))
        number_of_sides = int(input("How many sides should each dice should have? "))
#using the roll_dice function to the main function
        roll = roll_dice(number_of_dice, number_of_sides)
#printing the result 
        print("AM ROLLING THE DICE")
        print(f"Result: ", roll)
        print("Total", sum(roll))

if __name__ == "__main__":
    main()



