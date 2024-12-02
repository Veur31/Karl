word = input("Enter a word: ")
word1 = input("Enter anohter word: ")

convert = list(word.lower())
convert1 = list(word1.lower())

convert.sort(), convert1.sort()

if convert == convert1:
    print("True")
else:
    print("False")
            