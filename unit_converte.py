import os
def clear():
    choice = input("Go back to main menu? (Y/N): ").upper()
    if choice == 'Y':
        os.system('cls')
        main()
    else:
        os.system('cls')
def line():
    print("-" * 50)
def length_converter():
    line()
    print("Length Converter\n\n1. Kilometers to Miles\n2.Miles to Kilometers")
    print()
    choice = int(input("Enter your choice: "))
    try:
        if choice == 1:
            line()
            km = float(input("Enter the value in Kilometers: "))
            result = km * 0.62137
            print(f"{km} Kilometers is equivalent to: {result} Miles")
            clear()
        elif choice == 2:
            line()
            miles = float(input("Enter the value in miles: "))
            result = miles * 1.609344
            print(f"{miles} Miles is equivalent to: {result} Kilometers")
            clear()
        else:
            print("Please, input valid choice.")
    except ValueError:
        print("Please input from numbers 1-2 only.")
def weight_converter():
    line()
    print("Weight Converter\n\n1. Kilograms to pounds\n2. Pounds to Kilograms")
    print()
    choice = int(input("Enter your choice: "))
    try:
        if choice == 1:
            line()
            kg = float(input("Enter the value in Kilograms"))
            result = kg * 2.20462
            print(f"{kg} Kilograms is equivalent to: {result} Pounds")
            clear()
        elif choice == 2:
            line()
            pounds = float(input("Enter the value in pounds: "))
            result = pounds * 0.453592
            print(f"{pounds} Pounds is equivalent to: {result} Kilograms")
            clear()
        else:
            print("Please, print valid choice.")
    except ValueError:
        print("Please input from numbers 1-2 only.")
def temperature_converter():
    line()
    print("Temperature Converter\n\n1. Celsius to Fahrenheit\n2. Fahrenheit to celsius")
    print()
    choice = int(input("Enter your choice: "))
    try:
        if choice == 1:
            line()
            celsius = float(input("Enter the value in Celsius: "))
            result = celsius * 9/5 + 32
            print(f"{celsius} Celsius is equivalent to: {result} Pounds")
            clear()
        elif choice == 2:
            line()
            fahrenheit = float(input("Enter the value in Fahrenheit: "))
            result = (fahrenheit -32) * 5/9
            print(f"{fahrenheit} Fahrenheit is equivalent to: {result} Pounds")
            clear()
        else:
            print("Please enter valid choice")
    except ValueError:
        print("Please input from numbers 1-2 only.")
def main():
    print("Welcome to Unit converter\n\n1. Length Converter\n2. Weight Converter\n3. Temperature Converter")
    print()
    choice = int(input("Enter your choice: "))
    try:
        if choice == 1:
            length_converter()
        elif choice == 2:
            weight_converter()
        elif choice == 3:
            temperature_converter()
        else:
            print("Please, print valid choice")
    except ValueError:
        print("Please input from numbers 1-4 only.")
main()