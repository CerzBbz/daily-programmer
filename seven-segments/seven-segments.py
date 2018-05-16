# /r/DailyProgrammer
# [2018-04-23] Challenge #358 [Easy] Decipher The Seven Segments
# https://www.reddit.com/r/dailyprogrammer/comments/8eger3/20180423_challenge_358_easy_decipher_the_seven/
# Author: CerzBbz


values = {
    1: """   
  |
  |""",
    2: """ _ 
 _|
|_ """,
    3: """ _ 
 _|
 _|""",
    4: """   
|_|
  |""",
    5: """ _ 
|_ 
 _|""",
    6: """ _ 
|_ 
|_|""",
    7: """ _ 
  |
  |""",
    8: """ _ 
|_|
|_|""",
    9: """ _ 
|_|
 _|""",
    0: """ _ 
| |
|_|""",

}

map = {}

inputs = ["""    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|
""",
"""    _  _  _  _  _  _  _  _ 
|_| _| _||_|| ||_ |_| _||_ 
  | _| _||_||_| _||_||_  _|
""",
""" _  _  _  _  _  _  _  _  _ 
|_  _||_ |_| _|  ||_ | ||_|
 _||_ |_||_| _|  ||_||_||_|
""",
""" _  _        _  _  _  _  _ 
|_||_ |_|  || ||_ |_ |_| _|
 _| _|  |  ||_| _| _| _||_ 
""",
]


def make_map():
    for value, segment in values.items():
        merged = ''
        for column in zip(*segment.splitlines()):
            merged = merged + ''.join(column)
        map[merged] = value


def parse_display():
    merged = ''
    i = 1
    for challenge in inputs:
        output = []
        for column in zip(*challenge.splitlines()):
            merged = merged + ''.join(column)
            if i % 3 == 0:
                output.append(map[merged])
                i = 1
                merged = ''
                continue
            i = i + 1
        print(output)

make_map()
parse_display()
