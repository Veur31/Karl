def fibonacci_generator():
    a,b = 0,1
    yield a
    yield b
    while True:
        next_num = a+b
        yield next_num
        a,b = b, next_num
fibonacci = fibonacci_generator()
num = int(input("Enter a number: "))
for _ in range(num):
    print(next(fibonacci))