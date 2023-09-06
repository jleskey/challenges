#!/usr/bin/env python3

n = 0

while n < 100000:
    n += 1
    word = input();
    encoding = ''
    lastCode = ''
    for character in word:
        code = ''
        if character in {'B', 'F', 'P', 'V'}:
            code = '1'
        elif character in {'C', 'G', 'J', 'K', 'Q', 'S', 'X', 'Z'}:
            code = '2'
        elif character in {'D', 'T'}:
            code = '3'
        elif character == 'L':
            code = '4'
        elif character in {'M', 'N'}:
            code = '5'
        elif character == 'R':
            code = '6'
        if code and lastCode != code:
            encoding += code
        lastCode = code
    print(encoding)
