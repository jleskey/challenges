#!/usr/bin/env python3

import fileinput

test_file = fileinput.input()

string = test_file.readline().strip()

integers = [int(x) for x in test_file.readline().split()]

special_count = integers[0]
special_positions = integers[1:]
special_characters = [string[position - 1] for position in special_positions]

character_counts = {}

for character in string:
    if special_count == 0 or character in special_characters:
        character_counts[character] = character_counts.setdefault(character, 0) + 1

middle_length = 0
sides_length = 0

for position in special_positions:
    character = string[position - 1]

for character, count in character_counts.items():
    middle_length |= count % 2
    sides_length += count - (count % 2)

print(middle_length + sides_length)
