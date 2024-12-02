def minnum ():
    l1st = []
    num = int(input("Enter how many numbers: "))

    for i in range(0, num):
        num2 = int(input("Enter number: "))
        l1st.append(num2)
    print(l1st)

    minnum1 = l1st[0]
    for o in l1st:
        if minnum1 > o:
            minnum1 = 0
    print(minnum1)

minnum()