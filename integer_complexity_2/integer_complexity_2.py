# /r/DailyProgrammer
# [2018-03-14] Challenge #354 [Intermediate] Integer Complexity 2
# https://www.reddit.com/r/dailyprogrammer/comments/84f35x/20180314_challenge_354_intermediate_integer/
# Author: CerzBbz

complexity_map = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}


def get_complexity(n):
    try:
        return complexity_map[n]
    except KeyError:
        if n - 1 in complexity_map:
            complexity_map[n] = complexity_map[n-1] + 1
        for i in range(2,n):
            if n % i == 0:
                complexity = get_complexity(i) + get_complexity(n / i)
                if n not in complexity_map or complexity < complexity_map[n]:
                    complexity_map[n] = complexity
    return complexity_map[n]


def get_total(lower, upper):
    values = range(lower,upper+1)
    total = 0
    for value in values:
        total += get_complexity(value)
    return total


print(complexity_map)
print('Total from 1 to 100:\t' + str(get_total(1,100)))
print('Total from 1 to 1000:\t' + str(get_total(1,1000)))
print('Total from 1 to 10000:\t' + str(get_total(1,10000)))
print('Total from 1 to 100000:\t' + str(get_total(1,100000)))