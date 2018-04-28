# /r/DailyProgrammer
# [2018-03-28] Challenge #355 [Intermediate] Possible Number of Pies
# https://www.reddit.com/r/dailyprogrammer/comments/87rz8c/20180328_challenge_355_intermediate_possible/
# Author: CerzBbz

pumpkin_pie = (1, 0, 3, 4, 3)
apple_pie = (0, 1, 4, 3, 2)


def can_bake(ingredients, pie_type):
    for i, j in zip(ingredients, pie_type):
        if i < j:
            return False
    return True


def bake(ingredients, pie_type):
    after = ()
    for i, j in zip(ingredients, pie_type):
        after = after + ((i - j),)
    return after


def determine_max(ingredients):
    p = [0, 0]
    a = [0, 0]
    if can_bake(ingredients, pumpkin_pie):
        p_ingredients = bake(ingredients, pumpkin_pie)
        p = determine_max(p_ingredients)
        p[0] = p[0] + 1
    if can_bake(ingredients, apple_pie):
        a_ingredients = bake(ingredients, apple_pie)
        a = determine_max(a_ingredients)
        a[1] = a[1] + 1
    if (p[0] + p[1]) >= (a[0] + a[1]):
        return p
    return a


inputs = [[10, 14, 10, 42, 24], [12, 4, 40, 30, 40], [12, 14, 20, 42, 24]]
for values in inputs:
    pp, ap = determine_max(values)
    print("Pumpkin: " + str(pp) + "\tApple: " + str(ap))
