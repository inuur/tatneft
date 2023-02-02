import math


def is_prime(number: int) -> bool:
    for divider in range(2, math.ceil(number / 2) + 1):
        if number % divider == 0:
            return False
    return True


def get_prime_numbers(max_number: int) -> list[int]:
    result = list()
    if max_number < 2:
        return result
    for i in range(2, max_number + 1):
        if is_prime(i):
            result.append(i)
    return result


print(get_prime_numbers(5300))
