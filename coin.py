def coin_changer(coins, amount):
    coins.sort(reverse=True)
    change = []

    for coin in coins:
        while amount >= coin:
            amount -= coin
            change.append(coin)
    if amount == 0:
        return change
    else:
        return []
coins = [1,10,20,50,100]
amount = int(input("Enter the amount: "))
change = coin_changer(coins, amount)
if change != []:
    print(f'Minimum number of coins: {len(change)}')
    print(f"change: {change}")
else:
    print("Invalid input")