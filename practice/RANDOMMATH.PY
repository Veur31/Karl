import random
operator = ['+', '-', '*']
attemps = 10

def generator():
    first = random.randint(1, 100)
    second = random.randint(1,100)
    operaotrs = random.choice(operator)

    result = str(first) + ' ' + operaotrs + ' ' + str(second)
    result1 = eval(result)
    return result, result1
for i in range(attemps):
    result, result1 = generator()
    choice = input("Problem #" + str(i +1) + ':' + result + '= ' )
    if choice == result1:
        break
