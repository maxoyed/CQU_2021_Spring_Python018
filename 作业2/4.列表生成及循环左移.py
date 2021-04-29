n = int(input())

arr = list(range(1, n+1))
first_el = arr.pop(0)
arr.append(first_el)
arr = [str(item) for item in arr]
result = f"[{', '.join(arr)}]"

print(result)
