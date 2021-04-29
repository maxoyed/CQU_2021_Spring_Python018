from math import sqrt
def f(x):
    if x < 20:
        return 6. * (x**2) + 1.
    elif 20 <= x and x < 40:
        return sqrt(3.*x - 60.)
    else:
        return 100. / (x + 1.)

x = float(input())
f_x = f(x)

print("%.2f" % f_x)
