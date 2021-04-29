string = input()

result = [0, 0, 0, 0]
char_range = [chr(code) for code in range(ord('a'), ord('z'))]
char_range += [chr(code) for code in range(ord('A'), ord('Z'))]
number_range = [str(num) for num in range(10)]

for char in string:
    if char in char_range:
        result[0] += 1
    elif char == ' ':
        result[1] += 1
    elif char in number_range:
        result[2] += 1
    else:
        result[3] += 1

print(' '.join([str(i) for i in result]))
