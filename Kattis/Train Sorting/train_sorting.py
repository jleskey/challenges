import fileinput
from math import inf as infinity

test_file = fileinput.input()

train_count = int(test_file.readline().strip())

front = 0 # heaviest
back = 0 # lightest
count = 0

for i in range(train_count):
    weight = int(test_file.readline().strip())
    if weight > front:
        count += 1
        front = weight
        if count == 1:
            back = weight
    elif weight < back:
        count += 1
        back = weight

print(count)
