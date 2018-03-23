# /r/DailyProgrammer
# [2018-03-14] Challenge #354 [Intermediate] Integer Complexity 2
# https://www.reddit.com/r/dailyprogrammer/comments/84f35x/20180314_challenge_354_intermediate_integer/
# Author: CerzBbz
from math import floor

complexity_map = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}


def get_total_complexity(n):
    """
    Calculates all complexities from 1 to n and returns the total
    :param n: The upper bound
    :return: total: The total of the complexities from 1 to n
    """
    total = 0
    for i in range(1, n + 1):
        total += get_complexity(i)
    return total


def get_complexity(n):
    """
    Calculates the complexity of a given number and stores it in the complexity_map
    :param n: The number to determine the complexity of
    :return: complexity_map[n]: The calculated complexity of the integer n
    """
    try:
        return complexity_map[n]
    except KeyError:
        if n - 1 in complexity_map:
            complexity_map[n] = complexity_map[n - 1] + 1
        for i in range(2, int(floor(n / 2) + 1)):
            if n % i == 0:
                complexity = get_complexity(i) + get_complexity(n / i)
                if n not in complexity_map or complexity < complexity_map[n]:
                    complexity_map[n] = complexity
        return complexity_map[n]


print(get_total_complexity(10000))
