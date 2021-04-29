raw_list = list(eval(input()))
raw_list.reverse()
result = []

for i in raw_list:
    if i not in result:
        result.append(i)

result.reverse()
print(result)
