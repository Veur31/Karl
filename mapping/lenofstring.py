def l3n(x):
    return len(x)
word = int(input("Enter how many words: "))
l1st = []
for i in range(0, word):
    word1 = input("Enter a word: ")
    l1st.append(word1)
print(f"List of words: {l1st}")

result = map(l3n, l1st)
print(f"This is the lenght of every word: {list(result)}")