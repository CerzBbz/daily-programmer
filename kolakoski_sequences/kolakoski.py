# /r/DailyProgrammer
# [2018-04-19] Challenge #357 [Intermediate] Kolakoski Sequences
# https://www.reddit.com/r/dailyprogrammer/comments/8df7sm/20180419_challenge_357_intermediate_kolakoski/
# Author: CerzBbz

sequence = [1, 2, 2]


def calculate_kolakoski(length):
    pointer = 2
    next_is_two = False
    while len(sequence) < length:
        for i in range(0, sequence[pointer]):
            sequence.append(next_is_two + 1)
        next_is_two = not next_is_two
        pointer = pointer + 1
    return sequence


def get_ratio(length):
    ones = 0
    for i in sequence[:length]:
        if i == 1:
            ones = ones + 1
    return str(ones) + ":" + str(length - ones)


# Challenge inputs - 10^6, 10^8
max_pow = 8
calculate_kolakoski(10 ** max_pow)
for n in range(1, max_pow + 1):
    print("10^" + str(n) + ":\t" + get_ratio(10 ** n))
