arr = eval(input())

result = []
for idx, val in enumerate(arr):
    if arr.count(val) > 1:
        if arr[idx:].count(val) == 1:
            result.append(val)
    else:
        result.append(val)

print(result)
