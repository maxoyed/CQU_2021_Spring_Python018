num = int(input())

result = ''
if num < 0 or num > 36:
    result = 'error'
elif num == 0:
    result = 'green'
elif (num >= 1 and num <= 10) or (num >= 19 and num <= 28):
    result = 'red' if num % 2 == 1 else 'black'
else:
    result = 'black' if num % 2 == 1 else 'red'

print(result)
