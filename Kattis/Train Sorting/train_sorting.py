import fileinput
from math import inf as infinity

test_file = fileinput.input()

train_count = int(test_file.readline().strip())

front = 0 # heaviest
back = 0 # lightest
count = 0

incoming_train_weights = []
mean_sorted_weights = []

for i in range(train_count):
    weight = int(test_file.readline().strip())
    incoming_train_weights.append(weight)

mean = sum(incoming_train_weights) / len(incoming_train_weights)

mean_sorted_weights = sorted(incoming_train_weights, key=lambda weight: abs(mean - weight), reverse=True)

def place(weight):
    global front, back, count

    if weight > front:
        count += 1
        front = weight
        if count == 1:
            back = weight
    elif weight < back:
        count += 1
        back = weight

for weight in incoming_train_weights:
    first_pair = mean_sorted_weights[0:2]
    lightest = min(first_pair)
    heaviest = max(first_pair)

    if len(mean_sorted_weights) == 1 or (weight >= lightest and weight <= heaviest):
        place(weight)

    mean_sorted_weights.remove(weight)

print(count)
