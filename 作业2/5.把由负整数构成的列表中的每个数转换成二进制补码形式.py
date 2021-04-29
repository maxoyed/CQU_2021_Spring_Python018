raw_list = eval(input())
result = [bin(item+(1 << 32)) for item in raw_list]
print(result)
