num = int(input())

flag = False
for i in range(100, num + 1):
    i = str(i)
    if int(i[0]) ** 3 + int(i[1]) ** 3 + int(i[2]) ** 3 == int(i):
        print(i)
        flag = True

if flag == False:
    print("none")
