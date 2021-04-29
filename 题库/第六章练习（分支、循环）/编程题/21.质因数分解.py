def is_prime_factor(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def decompose(num: int) -> list:
    result = []
    for i in range(2, num + 1):
        if num % i == 0 and is_prime_factor(i):
            result.append(str(i))
            if is_prime_factor(num // i):
                result.append(str(num // i))
            else:
                result += decompose(num // i)
            return result
    return result


number = int(input())
factors = decompose(number)
print(f"{number}={'*'.join(factors)}")
