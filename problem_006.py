"""
Problem 6.Sum square difference
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 − 385 = 2640. Find the difference between the sum of the squares of the first one hundred natural numbers and
the square of the sum.
"""
from time_check import timer


@timer
def find_difference(num_range):
    sum1 = sum(map(lambda i: pow(i, 2), range(num_range + 1)))
    sum2 = pow(sum([*range(num_range + 1)]), 2)
    return sum2 - sum1


if __name__ == "__main__":
    find_difference(100)
