h = float(input())
N = int(input())

s = h
prev_h = h
for i in range(1, N):
    s += prev_h
    prev_h /= 2.

print("%.2f" % s)
