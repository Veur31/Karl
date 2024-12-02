def word1(x,y):
    return len(x) > y
num1 = int(input("Enter how many words: "))
l1st = []
for i in range(num1):
    word = input("Enter a word: ")
    l1st.append(word)
print(f"This are the list of words: {l1st}")
min_length = int(input("Enter the length: "))
result = filter(lambda word: word1(word, min_length),l1st)
print(f"This ar ethe filtered word based on lenght: {list(result)}")