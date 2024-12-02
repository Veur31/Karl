def occurence():
    word = input("Enter a word: ")
    occurence = input("What letter: ")
    count = 0
    for i in (word):
        if i == occurence:
            count += 1

    print(count)
occurence()

while True:
    again = input("Do you want to try again? Y/N: ")
    if again == "Y":
        occurence()
       
    else:
        print("Goodbye!")
        break



