import math
def quadratic(a,b,c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
       return "no real roots"
    elif discriminant == 0:
        one = -b / (2*a)

        return f"one real roots: {one}"
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Two roots: {root1},{root2}"
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
result = quadratic(a,b,c)
print(result)