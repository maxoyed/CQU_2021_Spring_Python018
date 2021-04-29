n = int(input())
arr = [x for x in range(1, n + 1)]

result = [None] * n

for idx, val in enumerate(arr):
    if idx == 0:
        result[n-1] = val
    else:
        result[idx - 1] = val

print(result)
