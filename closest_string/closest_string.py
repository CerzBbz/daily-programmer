# /r/DailyProgrammer
# [2018-03-05] Challenge #353 [Easy] Closest String
# https://www.reddit.com/r/dailyprogrammer/comments/826coe/20180305_challenge_353_easy_closest_string/
# Author: CerzBbz

def get_input():
    with open('inputs.txt', 'r') as file:
        data = [line.strip() for line in file.readlines()]
        data.pop(0)
    return data


def calculate_hamming_distance(string1, string2):
    distance = 0
    length = len(string1)
    i = 0
    while i < length:
        if string1[i] != string2[i]:
            distance += 1
        i += 1
    return distance


def determine_closest(strings):
    closest_string = ''
    closest_string_total = -1
    for string1 in strings:
        total = 0
        for string2 in strings:
            total += calculate_hamming_distance(string1, string2)
        if closest_string_total == -1 or total < closest_string_total:
            closest_string = string1
            closest_string_total = total
    return closest_string


input_values = get_input()
print(determine_closest(input_values))