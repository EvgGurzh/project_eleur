"""
Problem 3.Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
import math
from time_check import timer


def if_prime(num):
    for i in range(2, math.trunc(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True


@timer
def largest_prime(num):
    for i in range(2, math.trunc(math.sqrt(num)+1)):
        if num % i == 0 and if_prime(i):
            result = i
    return result


if __name__ == "__main__":
    largest_prime(600851475143)
