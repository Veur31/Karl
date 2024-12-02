class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self. year = year
    def displayinfo(self):
        print(f"This is the name of the book: {self.name} ")
        print(f"Author of the book: {self.author}")
        print(f"Year published: {self.year}")

name = input("Enter the name of the book: ")
author = input("Enter the author of the book: ")
year = int(input("Enter the what year it was published: "))
book1 = Book(name, author, year)

book1.displayinfo()
name = input("Enter the name of the book: ")
author = input("Enter the author of the book: ")
year = int(input("Enter the what year it was published: "))
book2 = Book(name, author, year)
print(f"Second book {book2.displayinfo()}")
