arr = eval(input())
flag = True
result = []

for el in set(arr):
    if arr.count(el) > 1:
        flag = False
    else:
        flag = True
        result.append(str(el))

if flag:
    result.sort()
    print(",".join(result))
else:
    print(False)
