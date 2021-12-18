"""Problem 5.Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import math
from time_check import timer


def if_prime(num):
    for i in range(2, math.trunc(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


def primes_list(num):
    primes = []
    for i in range(2, num + 1):
        if if_prime(i):
            primes.append(i)
    return primes


@timer
def smallest_divisible_num(num_range):
    primes = primes_list(num_range)
    result = 1
    buf_result = 1
    j = 0
    for i in range(2, num_range + 1):
        if i in primes:
            result *= i
            buf_result = result
        else:
            while buf_result % i != 0:
                buf_result = result * primes[j]
                j += 1
            result = buf_result
            j = 0
    return result


if __name__ == "__main__":
    smallest_divisible_num(20)

