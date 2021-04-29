names = input().split(",")
grades = eval(input())

result = [list(student) for student in list(zip(names, grades))]
print(result)
