n, m = [int(i) for i in input().split(' ')]

if n < 0 or m < 0 or n > 9 or m >9 or n >= m or len(range(n, m)) < 3:
    print('illegal input')
else:
    for i in range(n, m):
        if i != 0:
            for j in range(n, m):
                for k in range(n, m):
                    if i != j and j != k and i != k:
                        print(f'{i}{j}{k}', end=' ')
