# import time
# start_time = time.time()
def is_palindrome(num: int) -> bool:
    num = list(str(num))
    num_copy = num.copy()
    num.reverse()
    if num == num_copy:
        return True
    return False


def is_prime(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


n = int(input())
number = 2
result = []

while True:
    if len(result) == n:
        break
    if is_palindrome(number) and is_prime(number):
        result.append(number)
    number += 1

counter = 0
for i in result:
    if counter == 10 or counter == len(result):
        counter = 0
        print('\n')
    print(f'{i:6}', end='')
    counter += 1

# end_time = time.time()
# print(f'\nTime Cost: {(end_time - start_time)*1000:.0f}ms')
