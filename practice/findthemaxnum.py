def maxnum():
    l1st = []
    num = int(input("Enter how many numbers: "))
    for i in range(0, num):
        num1 = int(input())
        l1st.append(num1)
    print(l1st)

    maxnum1 = l1st[0]
    for i in l1st:
        if maxnum1 < i:
            maxnum1 = i
    print(maxnum1)
maxnum()