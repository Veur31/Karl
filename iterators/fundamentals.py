num = [1,2,3,4,5]
iterate = iter(num)
try:
    while True:
        num1 = next(iterate)
        print(num1)
except StopIteration:
    print("End of the list.")