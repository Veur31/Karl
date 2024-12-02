def add(x, y):
    return x + y
num = int(input("Enter how many numbers: "))
l1st = []
for i in range(0, num):
    num2 = int(input("Enter a number: "))
    l1st.append(num2)
print(f"This is the first list: {l1st}")
num3 = int(input("Enter how many numbers: "))
l1st1 = []
for o in range(0, num):
    num4 = int(input("Enter a number: "))
    l1st1.append(num4)
print(f"This is the second list: {l1st1}")

add1 = map(add, l1st, l1st1)
print(f"This is the sum of two list: {list(add1)}")
