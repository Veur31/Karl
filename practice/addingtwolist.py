def add():
    l1st = []
    l2st = []
    l3st = []
    num = int(input("Enter how many numbers: "))
    for i in range(0, num):
        num1 = int(input("Enter a number: "))
        l1st.append(num1)
    print(l1st)

    num2 = int(input("Enter how many numbers: "))
    
    for o in range(0, num2):
        num3 = int(input("Enter a number: "))
        l2st.append(num3)
    print(l2st)

    for p in range (0, len(l1st)):
        l3st.append(l1st[p] + l2st[p])
    print(l3st)
add()
    