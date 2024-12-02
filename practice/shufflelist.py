from random import shuffle
def l1st():
    l1st1 = []
    num = int(input("Enter how many elements: "))
    for i in range(0, num):
        elements = input("Enter a word: ")
        l1st1.append(elements)
    print(l1st1)

    shuffle(l1st1)
    print(l1st1)
l1st()
