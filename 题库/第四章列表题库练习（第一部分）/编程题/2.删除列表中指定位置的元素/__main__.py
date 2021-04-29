arr = eval(input())
n, m = eval(input())

if m > len(arr) - 1 or n > len(arr) - 1:
    print("error")

else:
    max_ = m if m > n else n + 1
    min_ = n if m > n else m + 1
    for i in range(min_, max_):
        arr.pop(min_)
    print(arr)
