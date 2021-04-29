names = input().split(",")
grades = [int(item) for item in input().split(",")]

result = list(zip(names, grades))
result = [list(item) for item in result]
result.sort(key=lambda item: item[1])

print(result)
