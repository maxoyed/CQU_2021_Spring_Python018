count = 0
summary = 0

while True:
    num = input()
    if num == "#":
        break
    num = int(num)
    count += 1
    summary += num

print(f"{count} {summary}")
