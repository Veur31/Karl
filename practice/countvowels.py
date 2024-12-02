vowels = ["a","e","i","o","u"]
word = input("Enter a word: ")
count = 0
for i in (word):
    if i not in vowels:
        count += 1
print(count)