"""Problem 7.10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

import math
from time_check import timer


def if_prime(num):
    for i in range(2, math.trunc(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


@timer
def find_prime(seq_num):
    i, count = 2, 0
    while count < seq_num:
        i += 1
        if if_prime(i):
            count += 1
    return i


if __name__ == "__main__":
    find_prime(10001)
