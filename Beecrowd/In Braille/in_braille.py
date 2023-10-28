#!/usr/bin/env python3

import fileinput

test_file = fileinput.input()

digits = ['.***..', '*.....', '*.*...', '**....', '**.*..', '*..*..', '***...', '****..', '*.**..', '.**...']

n = 0

def brailleToNumerals(length):
    line1 = test_file.readline().strip()
    line2 = test_file.readline().strip()
    line3 = test_file.readline().strip()
    for i in range(length):
        value = line1[3 * i : 3 * i + 2] + line2[3 * i : 3 * i + 2] + line3[3 * i : 3 * i + 2]
        print(digits.index(value), end='' if i + 1 < length else '\n')

def numeralsToBraille(length):
    input_line = test_file.readline().strip()
    integers = [int(numeral) for numeral in list(input_line)]
    for row in range(3):
        for i in range(length):
            print(digits[integers[i]][2 * row : 2 * row + 2], end=' ' if i + 1 < length else '\n')

def readTestCase():
    global n

    length = int(test_file.readline().strip())
    if length:
        conversion = test_file.readline().strip()
        if conversion == 'B':
            brailleToNumerals(length)
        elif conversion == 'S':
            numeralsToBraille(length)
        return True
    return False

while True:
    if not readTestCase():
        break
