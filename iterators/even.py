num = int(input("Enter how many numbers: "))
l1st = []
for i in range(num):
    num2 = int(input("Enter a number: "))
    l1st.append(num2)
print(f"These are the list of numbers: {l1st}")
def even(iterable):
    for i in iterable:
        if i % 2 == 0:
            yield i  
num3 = even(l1st)
print("Even numbers in the list")
for one in num3:
    print(one)