#!/usr/bin/env python3

import fileinput

for line in fileinput.input():
    n, m, k = map(int, line.split())
    if n == m == k == 0:
        break

    player = 0
    player_direction = 1
    number = 0
    player_k_claps = 0

    while player_k_claps < k:
        if player == n:
            player_direction = -1
        elif player == 1:
            player_direction = 1

        number += 1
        player += player_direction

        if player == m and (number % 7 == 0 or "7" in str(number)):
            player_k_claps += 1
            if player_k_claps == k:
                print(number)