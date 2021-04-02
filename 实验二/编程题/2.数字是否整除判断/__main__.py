# input an integer
number = int(input())
if number % 2 == 0 and number % 5 == 0:
    print(False)
elif number % 2 != 0 and number % 5 != 0:
    print(False)
else:
    print(True)
