# input an integer
number = int(input())

if number % (5*7*11) == 0:
    print(f"{number} can divided by 5,7 and 11.")
elif number % 5 != 0 and number % 7 != 0 and number % 11 != 0:
    print(f"{number} can not divided by 5,7 or 11.")
else:
    if number % 5 == 0:
        print(f"{number} can divided by 5.")
    if number % 7 == 0:
        print(f"{number} can divided by 7.")
    if number % 11 == 0:
        print(f"{number} can divided by 11.")
