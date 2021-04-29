names = input().split(",")
grades = [int(grade) for grade in input().split(",")]

result = [list(student) for student in list(zip(names, grades))]
result = sorted(result, key=(lambda x:x[1]))

print(result)
