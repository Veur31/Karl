def middle():
    l1st = []
    word = int(input("Enter how many numbers: "))
    for i in range(0,word):
        num1 = int(input("Enter a number: "))
        l1st.append(num1)
    print(f"This are the list of numbers: {l1st}")

    mid = int((len(l1st)/2))
    print(l1st[mid])
middle()



        