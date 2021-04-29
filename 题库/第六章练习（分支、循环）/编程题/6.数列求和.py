n = int(input())

result = 0.
a = 2.
b = 1.

for i in range(n):
    result += a / b
    t = a
    a = a + b
    b = t

print("%.4f" % result)
