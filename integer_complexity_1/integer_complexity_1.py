# /r/DailyProgrammer
# [2018-03-12] Challenge #354 [Easy] Integer Complexity 1
# https://www.reddit.com/r/dailyprogrammer/comments/83uvey/20180312_challenge_354_easy_integer_complexity_1/
# Author: CerzBbz


from math import sqrt, floor


def get_smallest_sum(number):
    low = floor(sqrt(number))

    while (number%low != 0):
        low -= 1
    return number/low + low


values = [1, 100, 500, 2258, 249258, 5296863]
for value in values:
    print(str(value) + "\t" + str(get_smallest_sum(value)))