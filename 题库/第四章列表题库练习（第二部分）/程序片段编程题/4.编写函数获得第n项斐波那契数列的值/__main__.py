# blank start
def Fibonacci(num, n):
    for i in range(2, n+1):
        num.append(num[i-1] + num[i-2])
    return num[n-1]
# blank end

num  =  [1,  1]
n  =  int(input())
print(Fibonacci(num,  n))
