price = float(input())
total_tax = None

if price < 1000:
    total_tax = 0
elif price >= 1000 and price < 5000:
    total_tax = price * 0.02
elif price >= 5000 and price < 10000:
    total_tax = price * 0.03
else:
    total_tax = price * 0.05

print("%.2f" % total_tax)
