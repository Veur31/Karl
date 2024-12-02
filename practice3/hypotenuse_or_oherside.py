import math

def calculate_hypotenuse(a,b):
    return math.hypot(a,b)

def calculate_sides(c, a_or_b):
    return math.sqrt(c**2 - a_or_b**2)
choice = input("Enter your choice find(H) or find(sides): ").strip().lower()
if choice == "h":
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    print(f"Hypotenuse is: {calculate_hypotenuse(a,b)}")
elif choice =="s":
    c = float(input("Enter hypotenuse: "))
    a_or_b = float(input("Enter one of the other side: "))
    print(f"The other side is: {calculate_sides(c, a_or_b)}")
else:
    print("Input valid choice")


