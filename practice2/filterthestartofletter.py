
def start_with(word, letter):
    return word.startswith(letter)
word1 = int(input("Enter how many numbers: "))
l1st = []
for i in range(0, word1):
    word2 = input("Enter a word: ")
    l1st.append(word2)
print(f"This are the list of words: {l1st}")
word2 = input("What is the letter to be filtered")
result = filter(lambda word: start_with(word, word2), l1st)
print(f"This is filtered words that starts with letter: {word2}:  {list(result)}")

