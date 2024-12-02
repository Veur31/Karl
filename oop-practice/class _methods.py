class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError ("Invalid name")
        if house not in["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError ("Invalid house")
        
        self.name = name
        self.house = house


def student_info():
    name = input("Enter the name: ")
    house = input("Enter the house: ")
    return Student(name, house)
def main():
    student1 = student_info()
    print(f"{student1.name} from {student1.house}")
if __name__ == "__main__":
    main()