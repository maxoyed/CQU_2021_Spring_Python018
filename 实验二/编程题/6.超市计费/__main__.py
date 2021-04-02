# input amount
amount = float(input())

if amount < 50:
    print(amount)
elif amount >= 50 and amount < 100:
    print(amount * 0.9)
else:
    print(100 * 0.9 + (amount - 100) * 0.8)
