# /r/DailyProgrammer
# [2018-04-11] Challenge #356 [Intermediate] Goldbach's Weak Conjecture
# https://www.reddit.com/r/dailyprogrammer/comments/8bh8dh/20180411_challenge_356_intermediate_goldbachs/
# Author: CerzBbz

from math import floor, sqrt

primes = [2, 3]


def is_prime(n):
    for x in range(2, floor(sqrt(n)) + 1):
        if n % x == 0:
            return False
    return True


def find_primes(max_n):
    for n in range(3, max_n):
        if n in primes:
            continue
        if is_prime(n):
            primes.append(n)


def get_sum(n):
    find_primes(n)
    for i in primes:
        for j in primes:
            diff = n - i - j
            if diff in primes:
                return i, j, diff


for problem in [111, 17, 199, 287, 53]:
    a, b, c = get_sum(problem)
    print(str(problem) + " = " + str(a) + " + " + str(b) + " + " + str(c))
