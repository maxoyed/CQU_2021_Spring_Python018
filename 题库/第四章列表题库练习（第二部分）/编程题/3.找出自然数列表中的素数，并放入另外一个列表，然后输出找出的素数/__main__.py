def is_prime(num):
    if num in [0, 1]:
        return False
    elif num in [2, 3]:
        return True
    else:
        flag = True
        for i in range(2, num):
            if num % i == 0:
                flag = False
                break
        return flag


arr = eval(input())
result = [x for x in arr if is_prime(x)]
print(result)
