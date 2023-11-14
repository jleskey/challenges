import fileinput

file = fileinput.input()

p, q = map(int, file.readline().split(' '))

order = file.readline().strip()

first_a_index = order.index('A')
first_a_value = min(p, q)
second_a_index = order.index('A', first_a_index + 1)
second_a_value = max(p, q)

first_b_index = order.index('B')
second_b_index = order.index('B', first_b_index + 1)

#cards = [(alice_cards.pop() if value == 'A' else value) for value in order]

lower_bound = [1, 1, 1, 1]
upper_bound = [9, 9, 9, 9]

lower_bound[first_a_index] = upper_bound[first_a_index] = first_a_value
lower_bound[second_a_index] = upper_bound[second_a_index] = second_a_value

for i, value in enumerate(lower_bound):
    if i < 3:
        lower_bound[i + 1] = max(value + 1, lower_bound[i + 1])

for i in range(3, -1, -1):
    value = upper_bound[i]
    if i > 0:
        upper_bound[i - 1] = min(value - 1, upper_bound[i - 1])

if (lower_bound[first_b_index] == upper_bound[first_b_index] and lower_bound[second_b_index] == upper_bound[second_b_index]):
    print(lower_bound[first_b_index], lower_bound[second_b_index])
else:
    print(-1)
