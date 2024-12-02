
def num(x):
    num = int(input("Enter a number: "))
    return x ** num
word = int(input("Enter how many numbers: "))
l1st = []
for i in range(word):
    num2 = int(input("Enter a number: "))
    l1st.append(num2)
print(l1st)

combine = map(num,l1st)
print(list(combine))