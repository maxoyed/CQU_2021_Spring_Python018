age = float(input())

if age > 0 and age <= 1:
    print("infant")
elif 1 < age < 13:
    print("child")
elif 13 <= age < 20:
    print("teenager")
elif age >= 20:
    print("adult")
else:
    print("Error")
