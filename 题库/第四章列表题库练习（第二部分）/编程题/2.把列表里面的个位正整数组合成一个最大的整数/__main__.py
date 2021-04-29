arr = eval(input())
arr.sort(reverse=True)
result = "".join([str(i) for i in arr])
print(int(result))
