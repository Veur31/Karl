def convert(x):
    return str(x)
num = int(input("Enter how many numbers: "))
l1st = []
for i in range(0, num):
    num2 = int(input("Enter a number: "))
    l1st.append(num2)
print(f"List of numbers: {l1st}")
result = map(convert, l1st)
print(f"This is the converted string of numbers: {list(result)}")