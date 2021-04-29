num = int(input())

while True:
    if num == 1:
        break
    if num % 2 == 1:
        num = num * 3 + 1
    else:
        num = num // 2
    end = "," if num != 1 else "\n"
    print(num, end=end)
