"""
Problem 4.Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers.
"""
from time_check import timer


def palindrome_check(num):
    reversed_num = 0
    while num > reversed_num:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10
    return True if reversed_num == num else False


@timer
def largest_palindrome():
    answer = 0
    for i in range(100, 999):
        for j in range(100, 999):
            if palindrome_check(i * j) and i * j > answer:
                answer = i * j
    return answer


if __name__ == "__main__":
    largest_palindrome()
