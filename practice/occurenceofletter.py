word = input("Enter a word: ")
chosen = input("Enter a letter: ")
count = 0
for i in word:
    if i == chosen:
        count += 1
print(count)