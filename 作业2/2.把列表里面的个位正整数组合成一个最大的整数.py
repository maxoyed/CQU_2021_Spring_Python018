raw_list = list(eval(input()))
raw_list.sort(reverse=True)

raw_list = [str(item) for item in raw_list]
result = int("".join(raw_list))

print(result)
