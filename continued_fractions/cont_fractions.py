# /r/DailyProgrammer
# [2018-04-20] Challenge #357 [Hard] Continued Fractions
# https://www.reddit.com/r/dailyprogrammer/comments/8dqzyi/20180420_challenge_357_hard_continued_fractions/
# Author: CerzBbz


def calculate_gauss(num, den):
    answer.append(int(den / num))
    if (den % num) != 0:
        calculate_gauss(den % num, num)


def calculate_fraction(gauss):
    a = 0
    b = 1
    for i in reversed(range(0, len(gauss))):
        c = b
        b = a + int(gauss[i]) * b
        a = c
    answer.append(a)
    answer.append(b)


challenge_inputs = ["67/29", "45/16", "[2;1,7]", "7/3", "23/8"]
for challenge in challenge_inputs:
    answer = []
    if "/" in challenge:
        values = challenge.split('/')
        calculate_gauss(int(values[0]), int(values[1]))
    else:
        calculate_fraction(challenge.replace(';', ',').replace('[', '').replace(']', '').split(','))
    print(answer)
