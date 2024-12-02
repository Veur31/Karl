word = input("Enter a word: ").lower()
word1= input("Enter another word: ").lower()

if word == word1[::-1]:
    print("Anagram")
else:
    print("No")