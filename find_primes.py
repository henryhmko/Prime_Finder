
import time

"""
Find large number primes.
Goal: Find prime numbers that are more than 6 digits.
"""

###################
##1. Brute Force ##
###################

def brute_prime_finder(num, digits):
    # "num": number of primes I want
    # "digits": number of digits I want my primes to be

    start_t = time.perf_counter()

    if digits == 1:
        return [2,3,5,7]

    total_primes = []
    number = 10
    while len(total_primes) < num or (number // (10 ** digits) != 0):
        if number // (10 ** (digits-1)) != 0: #if number is in the range for number of digits we want
            if is_prime(number):
                total_primes.append(number)
        number += 1

    end_t = time.perf_counter()
    return total_primes, (end_t - start_t)

def is_prime(num):
    if num == 1:
        return False
    i = 2
    while i != num:
        if num % i == 0:
            return False
        i += 1
    return True
